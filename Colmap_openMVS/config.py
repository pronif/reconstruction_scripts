import os

# Set the workspace directory, which must contain an images subdirectory
workspace_dir = "/Users/federicoproni/Desktop/recon/"

# Set the binary folder of Colmap
colmap_bin = "/Users/federicoproni/repo/colmap/build/src/exe/colmap"
# Set the binary folder with the openMVS apps
openMVS_bin = "/Users/federicoproni/repo/openMVS_build/bin"

# Path assertions for inputs and executables
image_dir = workspace_dir + "images"
assert os.path.exists(image_dir)

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
