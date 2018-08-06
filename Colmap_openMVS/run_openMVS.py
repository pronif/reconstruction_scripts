#!/usr/bin/python3
import os

#######
#CONFIG
#######

# Set the workspace directory (which must contain an images subdirectory)
workspace_dir = "/home/v4rl/reconstruction/Styrac_Colmap/"

# Colmap is assumed to be system installed
# Set the binary folder with the openMVS apps
openMVS_bin = "/home/v4rl/repo/openMVS_build/bin"

openMVS_InterfaceSFM_bin = openMVS_bin + "/" + "InterfaceVisualSFM"
openMVS_Densify_bin = openMVS_bin + "/" + "DensifyPointCloud"
openMVS_Mesh_bin= openMVS_bin + "/" + "ReconstructMesh"
openMVS_Refine_bin= openMVS_bin + "/" + "RefineMesh"
openMVS_Texture_bin= openMVS_bin + "/" + "TextureMesh"

assert os.path.exists(openMVS_InterfaceSFM_bin)
assert os.path.exists(openMVS_Densify_bin)
assert os.path.exists(openMVS_Mesh_bin)
assert os.path.exists(openMVS_Refine_bin)
assert os.path.exists(openMVS_Texture_bin)

# input
image_dir = workspace_dir + "images"
assert os.path.exists(image_dir)

# output
colmap_database_file = workspace_dir + "database.db"
colmap_sparse_recon_dir = workspace_dir + "sparse"
sparse_nvm_file = workspace_dir + "model.nvm"
sparse_mvs_file = workspace_dir + "/model.mvs"
dense_mvs_file = workspace_dir + "/model_dense.mvs"
unrefined_mesh_file = workspace_dir + "/model_dense_mesh.mvs"
refined_mesh_file = workspace_dir + "/model_dense_mesh_refined.mvs"

##########
#EXECUTION
##########
dry_run = True


def execute_command(command, dry_run = True):
    print()
    print(command)
    print()
    if not dry_run:
        retval = os.system(command)
        assert retval == 0


cmd = "colmap feature_extractor --database_path {} --image_path {} --SiftExtraction.use_gpu 0".format(colmap_database_file, image_dir)
execute_command(cmd, dry_run)

cmd = "colmap exhaustive_matcher --database_path {} --SIFTMatching.use_gpu 0".format(colmap_database_file)
execute_command(cmd, dry_run)

cmd = "colmap mapper --database_path {} --image_path {} --export_path {}".format(colmap_database_file, image_dir, colmap_sparse_recon_dir)
execute_command(cmd, dry_run)

cmd = "colmap model_converter {} --output_path {} --output_type NVM".format(colmap_sparse_recon_dir + "/0", sparse_nvm_file)
execute_command(cmd, dry_run)

cmd = openMVS_InterfaceSFM_bin + " -i {} -w {}".format(sparse_nvm_file, image_dir)
execute_command(cmd, dry_run)

cmd = openMVS_Densify_bin + " {} -w {}".format(sparse_mvs_file, image_dir)
execute_command(cmd, dry_run)

cmd = openMVS_Mesh_bin + " {} -w {}".format(dense_mvs_file, image_dir)
execute_command(cmd, dry_run)

cmd = openMVS_Refine_bin + " {} -w {} --resolution-level 1".format(unrefined_mesh_file, image_dir)
execute_command(cmd, dry_run)

cmd = openMVS_Texture_bin + " {} -w {} --export-type obj".format(refined_mesh_file, image_dir)
execute_command(cmd, dry_run)
