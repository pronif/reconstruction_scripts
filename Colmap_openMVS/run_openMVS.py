#!/usr/bin/python3
import os

#######
#CONFIG
#######

# Set the model folder (where the VisualSFM model is stored)
workspace_dir = "/home/v4rl/reconstruction/Styrac_Colmap/"

# TODO from workspace folder?
model_dir = "/home/v4rl/reconstruction/Styrac_Colmap/model.nvm"
image_dir = "/home/v4rl/reconstruction/Styrac_Colmap/images"

# Set the binary folder with the openMVS apps
openMVS_bin = "/home/v4rl/repo/openMVS_build/bin"

InterfaceSFM_bin = openMVS_bin + "/" + "InterfaceVisualSFM"
Densify_bin = openMVS_bin + "/" + "DensifyPointCloud"
Mesh_bin= openMVS_bin + "/" + "ReconstructMesh"
Refine_bin= openMVS_bin + "/" + "RefineMesh"
Texture_bin= openMVS_bin + "/" + "TextureMesh"

assert os.path.exists(InterfaceSFM_bin)
assert os.path.exists(Densify_bin)
assert os.path.exists(Mesh_bin)
assert os.path.exists(Refine_bin)
assert os.path.exists(Texture_bin)

##########
#EXECUTION
##########
dry_run = True

cmd = InterfaceSFM_bin + " -i {} -w {}".format(model_dir, image_dir)
print()
print(cmd)
print()
if not dry_run:
    retval = os.system(cmd)
    assert retval == 0

mvs_sparse_file = workspace_dir + "/model.mvs"
cmd = Densify_bin + " {} -w {}".format(mvs_sparse_file, image_dir)
print()
print(cmd)
print()
if not dry_run:
    retval = os.system(cmd)
    assert retval == 0

mvs_dense_file = workspace_dir + "/model_dense.mvs"
cmd = Mesh_bin + " {} -w {}".format(mvs_dense_file, image_dir)
print()
print(cmd)
print()
if not dry_run:
    retval = os.system(cmd)
    assert retval == 0

unrefined_mesh_file = workspace_dir + "/model_dense_mesh.mvs"
cmd = Refine_bin + " {} -w {} --resolution-level 1".format(unrefined_mesh_file, image_dir)
print()
print(cmd)
print()
if not dry_run:
    retval = os.system(cmd)
    assert retval == 0

refined_mesh_file = workspace_dir + "/model_dense_mesh_refined.mvs"
cmd = Texture_bin + " {} -w {} --export-type obj".format(refined_mesh_file, image_dir)
print()
print(cmd)
print()
if not dry_run:
    retval = os.system(cmd)
    assert retval == 0

