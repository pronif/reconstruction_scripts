#!/usr/bin/python3
import argparse
import os

import config


parser = argparse.ArgumentParser()
parser.add_argument("--dataset_dir")
parser.add_argument("--workspace_dir")
parser.add_argument("--dry_run", dest="dry_run", action="store_true")
parser.add_argument("--manual_cleaning", dest="manual_cleaning", action="store_true")
parser.set_defaults(dataset_dir=config.input_folder)
parser.set_defaults(workspace_dir=config.output_folder)
parser.set_defaults(dry_run=False)
parser.set_defaults(manual_cleaning=False)

args = parser.parse_args()

cmd = config.mve_makescene_bin + " -i {} {}".format(args.dataset_dir, args.workspace_dir)
print()
print(cmd)
print()
if not args.dry_run:
    retval = os.system(cmd)
    assert retval == 0

cmd = config.mve_sfmrecon_bin + " {}".format(args.workspace_dir)
print()
print(cmd)
print()
if not args.dry_run:
    retval = os.system(cmd)
    assert retval == 0

cmd = config.mve_dmrecon_bin + " -s2 {}".format(args.workspace_dir)
print()
print(cmd)
print()
if not args.dry_run:
    retval = os.system(cmd)
    assert retval == 0

pointcloud_file = args.workspace_dir + "/" + "pset-L2.ply"
cmd = config.mve_scene2pset_bin + " -F2 {} {}".format(args.workspace_dir, pointcloud_file)
print()
print(cmd)
print()
if not args.dry_run:
    retval = os.system(cmd)
    assert retval == 0

if(args.manual_cleaning):
    print("Clean the point cloud pset-L2.ply (see README for more information)")
    input("Press Enter to continue...")
mesh_file = args.workspace_dir + "/" + "surface-L2.ply"
cmd = config.mve_fssrecon_bin + " {} {}".format(pointcloud_file, mesh_file)
print()
print(cmd)
print()
if not args.dry_run:
    retval = os.system(cmd)
    assert retval == 0

clean_mesh_file = args.workspace_dir + "/" + "surface-L2-clean.ply"
cmd = config.mve_meshclean_bin + " {} {}".format(mesh_file, clean_mesh_file)
print()
print(cmd)
print()
if not args.dry_run:
    retval = os.system(cmd)
    assert retval == 0
