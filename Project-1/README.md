# Lidar based 3D object detection using Voxelnet

reference - VoxelNet: End-to-end learning for point cloud-based 3D object detection.
Authors: Yin Zhou, Oncel Tuzel - Apple Inc

Challenges - Replacing Manual feaeture extraction
- In the manual feature extraction the point clouds are projected in top-view, and then apply the image based feature extraction methods are used for the detection. But these techniques cause an information bottleneck and cannot extract the 3D information required to detect the tasks.

The paper introduced: 
- FLN feateure learning network, A machine - learned feature extractor introduced to effectively extract the 3D shape information.
- Reducing computation and focus on memory constraints. Voxel grouping and random sampling technique is used to process the voxeks containing more than a T number of points in the voxel.
- END-to-END 3D detection architecture: that simultaneously learns the feeature representation from the raw point cloud data and predicts accureate 3D bounding boxes in an end-to-end fashion.
