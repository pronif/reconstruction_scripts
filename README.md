#Scripts for photogrammetry pipelines

These scripts automate the process of running reconstruction pipelines.

Some steps common to all pipelines are: Structure From Motion, Multi View Stereo,
 mesh reconstruction, mesh cleaning and optionally texturing. 
 
## MVE
One of the few open source projects that offer the whole pipeline in one solution.

The quality is not the best achievable however (based on experience and benchmarks)

## Colmap + openMVS
Colmap also provides a complete pipeline, but for dense reconstruction requires a CUDA enabled GPU which I do not have at the moment.
Therefore I use it until sparse reconstruction.

OpenMVS is the best tool for dense reconstruction, according to benchmarks. 
It is especially good to be run in an automated way.