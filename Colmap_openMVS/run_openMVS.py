#!/usr/bin/python3
import os

#######
#CONFIG
#######

# WORKSPACE STRUCTURE
# The workspace directory must contain the VisualSFM database (model.nvm) and an images subdirectory

# Set the model directory (where the VisualSFM model is stored)
workspace_dir = "/home/v4rl/reconstruction/Styrac_Colmap/"

model_dir = workspace_dir + "model.nvm"
image_dir = workspace_dir + "images"

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


colmap_database_file = workspace_dir + "database.db"
cmd = "colmap feature_extractor --database_path {} --image_path {} --SiftExtraction.use_gpu 0".format(colmap_database_file, image_dir)
execute_command(cmd, dry_run)

cmd = "colmap exhaustive_matcher --database_path {} --SIFTMatching.use_gpu 0".format(colmap_database_file)
execute_command(cmd, dry_run)

colmap_sparse_recon_dir = workspace_dir + "sparse"
cmd = "colmap mapper --database_path {} --image_path {} --export_path {}".format(colmap_database_file, image_dir, colmap_sparse_recon_dir)
execute_command(cmd, dry_run)

sparse_recon_nvm = workspace_dir + "model.nvm"
cmd = "colmap model_converter {} --output_path {} --output_type NVM".format(colmap_sparse_recon_dir + "/0", sparse_recon_nvm)
execute_command(cmd, dry_run)

cmd = openMVS_InterfaceSFM_bin + " -i {} -w {}".format(model_dir, image_dir)
execute_command(cmd, dry_run)

mvs_sparse_file = workspace_dir + "/model.mvs"
cmd = openMVS_Densify_bin + " {} -w {}".format(mvs_sparse_file, image_dir)
execute_command(cmd, dry_run)

mvs_dense_file = workspace_dir + "/model_dense.mvs"
cmd = openMVS_Mesh_bin + " {} -w {}".format(mvs_dense_file, image_dir)
execute_command(cmd, dry_run)

unrefined_mesh_file = workspace_dir + "/model_dense_mesh.mvs"
cmd = openMVS_Refine_bin + " {} -w {} --resolution-level 1".format(unrefined_mesh_file, image_dir)
execute_command(cmd, dry_run)

refined_mesh_file = workspace_dir + "/model_dense_mesh_refined.mvs"
cmd = openMVS_Texture_bin + " {} -w {} --export-type obj".format(refined_mesh_file, image_dir)
execute_command(cmd, dry_run)


