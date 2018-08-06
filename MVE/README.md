# Run the MVE pipeline
Run the full MVE photogrammetry pipeline


**Input:** images

**Output:** clean mesh


Set the parameters in *config.py* and run: ```./run_mve.py```

### Manual cleaning
It is sometimes useful to manually clean the dense point cloud before applying the meshing step.
To do so I use CloudCompare. On importing the mesh one has to specify the two scalar properties *confidence* and *value*.

After saving the cleaned mesh, it is necessary to edit the ply file before continuing with the mve pipeline.
In the ply header, change *scalar_value* into *value* and *scalar_confidence* into *confidence*.
