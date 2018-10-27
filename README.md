# Reconstruction scripts
These scripts automate the process of running full reconstruction pipelines.
The input of the pipeline is in general a set of images and the output a 3D mesh.

Some steps common to all pipelines are: Structure From Motion, Multi View Stereo,
 mesh reconstruction, mesh cleaning. 
 
## Colmap + openMVS
Colmap provides a complete reconstruction pipeline, but for dense reconstruction requires a CUDA enabled GPU which I do not have at the moment.
Therefore I use it until sparse reconstruction and then use OpenMVS which is the best tool for dense reconstruction, according to benchmarks. 

### Installation 
See the install instruction of the respective web pages for info on how to install Colmap and openMVS.
The scripts where tested on MacOs High Sierra and Ubuntu 16.

### How to use
Set the configs in *Colmap_openMVS/config.py* and run with
```
python3 run_pipeline.py
```

## MVE
Multi-View Environment offers a full reconstruction pipeline, however the quality is not anymore at the state of the art.
See the *MVE/README.md* for info on how to run.
