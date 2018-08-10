#!/usr/bin/python3
import os
import argparse

import config

parser = argparse.ArgumentParser()
parser.add_argument("--workspace_dir")
parser.add_argument("--dry_run", dest="dry_run", action="store_true")
parser.add_argument("--no_gpu", dest="no_gpu", action="store_true")
parser.set_defaults(workspace_dir=config.workspace_dir)
parser.set_defaults(dry_run=False)
parser.set_defaults(no_gpu=False)
args = parser.parse_args()

#input
image_dir = config.image_dir

# output
colmap_database_file = config.workspace_dir + "database.db"
colmap_sparse_recon_dir = config.workspace_dir + "sparse"
sparse_nvm_file = config.workspace_dir + "model.nvm"
sparse_mvs_file = config.workspace_dir + "model.mvs"
dense_mvs_file = config.workspace_dir + "model_dense.mvs"
unrefined_mesh_file = config.workspace_dir + "model_dense_mesh.mvs"
refined_mesh_file = config.workspace_dir + "model_dense_mesh_refined.mvs"


def execute_command(command, dry_run=True):
    print()
    print(command)
    print()
    if not dry_run:
        retval = os.system(command)
        assert retval == 0

# Use no gpu mode in any case for feature extraction because it requires CUDA. The matcher below can use OpenGL
cmd = config.colmap_bin + " feature_extractor --database_path {} --image_path {} --SiftExtraction.use_gpu 0".format(colmap_database_file, image_dir)
execute_command(cmd, args.dry_run)

cmd = config.colmap_bin + " exhaustive_matcher --database_path {}".format(colmap_database_file)
if(args.no_gpu):
    cmd = cmd + " --SiftMatching.use_gpu 0"
execute_command(cmd, args.dry_run)

cmd = "mkdir -p " + colmap_sparse_recon_dir
execute_command(cmd, args.dry_run)

cmd = config.colmap_bin + " mapper --database_path {} --image_path {} --export_path {}".format(colmap_database_file, image_dir, colmap_sparse_recon_dir)
execute_command(cmd, args.dry_run)

cmd = config.colmap_bin + " model_converter --input_path {} --output_path {} --output_type NVM".format(colmap_sparse_recon_dir + "/0", sparse_nvm_file)
execute_command(cmd, args.dry_run)

cmd = config.openMVS_InterfaceSFM_bin + " -i {} -w {}".format(sparse_nvm_file, image_dir)
execute_command(cmd, args.dry_run)

cmd = config.openMVS_Densify_bin + " {} -w {}".format(sparse_mvs_file, image_dir)
execute_command(cmd, args.dry_run)

cmd = config.openMVS_Mesh_bin + " {} -w {}".format(dense_mvs_file, image_dir)
execute_command(cmd, args.dry_run)

cmd = config.openMVS_Refine_bin + " {} -w {} --resolution-level 1".format(unrefined_mesh_file, image_dir)
execute_command(cmd, args.dry_run)

cmd = config.openMVS_Texture_bin + " {} -w {} --export-type obj".format(refined_mesh_file, image_dir)
execute_command(cmd, args.dry_run)
