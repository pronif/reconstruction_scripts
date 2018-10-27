# Scripts to automate photogrammetry pipelines

These scripts automate the process of running reconstruction pipelines.

Some steps common to all pipelines are: Structure From Motion, Multi View Stereo,
 mesh reconstruction, mesh cleaning and optionally texturing. 
 
## Colmap + openMVS
Colmap provides a complete reconstruction pipeline, but for dense reconstruction requires a CUDA enabled GPU which I do not have at the moment.
Therefore I use it until sparse reconstruction.

OpenMVS is the best tool for dense reconstruction, according to benchmarks. 
It is especially good to be run in an automated way.

### How to use
Set the configs in *Colmap_openMVS/config.py* and run with
```
python3 run_pipeline.py
```

## MVE
One of the few open source projects that offer the whole pipeline in one solution.

The quality is not the best achievable however (based on experience and benchmarks)


