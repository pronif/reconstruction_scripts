import os

# Set the input folder (where the images are stored)
input_folder = "/home/v4rl/reconstruction/lawnmower_fixed_height/images"
# Set the output folder (where the mve workspace will be)
output_folder = "/home/v4rl/reconstruction/fixed_height_mve"
# Set the folder with the mve binaries
mve_bin = "/home/v4rl/repo/mve/apps/"

mve_makescene_bin = mve_bin + "makescene/makescene"
mve_sfmrecon_bin = mve_bin + "sfmrecon/sfmrecon"
mve_dmrecon_bin = mve_bin + "dmrecon/dmrecon"
mve_scene2pset_bin = mve_bin + "scene2pset/scene2pset"
mve_fssrecon_bin = mve_bin + "fssrecon/fssrecon"
mve_meshclean_bin = mve_bin + "meshclean/meshclean"

assert os.path.exists(mve_makescene_bin)
assert os.path.exists(mve_sfmrecon_bin)
assert os.path.exists(mve_dmrecon_bin)
assert os.path.exists(mve_scene2pset_bin)
assert os.path.exists(mve_fssrecon_bin)
assert os.path.exists(mve_meshclean_bin)
