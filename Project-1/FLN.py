# __cfg__.MAX_POINT_NUMBER indicates the point cloud threshold value, the threshold value used to process the selective voxel grids containing more than 35 point clouds
# X, Y, Z min, max values define the 3D space in meters
# Voxel_X_size indicate the voxel grid dimensions (fixed)



if __cfg__.DETECT_OBJECT == 'Car':
    #cfg - Config
    
    #Random sampling threshold value (T)
    __cfg__.MAX_POINT_NUMBER = 35
    
    #[Z_MIN, Z_MAX], [Y_MIN, Y_MAX], [X_MIN, X_MAX] indicates 3D space of range Z,H,W respectively
    __cfg__.Z_MIN = -3
    __cfg__.Z_MAX = 1
    __cfg__.Y_MIN = -40
    __cfg__.Y_MAX = 40
    __cfg__.X_MIN = 0
    __cfg__.X_MAX = 70.4
    
    # [VOXEL_X_SIZE, VOXEL_Y_SIZE, VOXEL_Z_SIZE] represents voxel dimesions 𝑣_𝐷,𝑣_(𝐻,) 𝑣_𝑊
    __cfg__.VOXEL_X_SIZE = 0.2
    __cfg__.VOXEL_Y_SIZE = 0.2
    __cfg__.VOXEL_Z_SIZE = 0.4
    __cfg__.VOXEL_POINT_COUNT = 35
    
    #Dividing the 3D spaces into voxel grids
    __cfg__.INPUT_WIDTH = int((__cfg__.X_MAX - __cfg__.X_MIN) / __cfg__.VOXEL_X_SIZE)
    __cfg__.INPUT_HEIGHT = int((__cfg__.Y_MAX - __cfg__.Y_MIN) / __cfg__.VOXEL_Y_SIZE)
    __cfg__.INPUT_DEPTH = int((__cfg__.Z_MAX - __cfg__.Z_MIN) / __cfg__.VOXEL_Z_SIZE)
    __cfg__.LIDAR_COORD = [0, 40, 3]
    __cfg__.FEATURE_RATIO = 2
    __cfg__.FEATURE_WIDTH = int(__cfg__.INPUT_WIDTH / __cfg__.FEATURE_RATIO)
    __cfg__.FEATURE_HEIGHT = int(__cfg__.INPUT_HEIGHT / __cfg__.FEATURE_RATIO)
view rawConfig.py hosted with ❤ by GitHub
