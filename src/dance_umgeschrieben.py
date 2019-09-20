def dance8(motionProxy, timestep=0, time_start=1):
    names = ["LAnklePitch", "LAnkleRoll", "LElbowRoll", "LElbowYaw", "LHand", "LHipPitch", "LHipRoll", "LHipYawPitch",
             "LKneePitch", "LShoulderPitch", "LShoulderRoll", "LWristYaw",
             "RAnklePitch", "RAnkleRoll", "RElbowRoll", "RElbowYaw", "RHand", "RHipPitch", "RHipRoll", "RHipYawPitch",
             "RKneePitch", "RShoulderPitch", "RShoulderRoll", "RWristYaw"]
    keys = [
        [-0.338789, -0.345963, -0.343821, -0.335337, -0.335337, -0.335337, -0.325914, -0.325914, -0.325914, -0.325914],
        [-0.00832588, -0.0065871, -0.00450932, -0.00451108, -0.00451108, -0.00451108, -0.00832588, -0.00832588,
         -0.00832588, -0.00832588],
        [-0.502655, -1.17518, -1.34913, -1.18313, -1.34525, -1.18174, -1.34981, -1.51957, -0.459482, -1.51863,
         -0.462734, -0.545569, -1.40801, -0.545569, -0.463039, -0.440982, -0.451639, -0.545389, -1.39885,
         -0.546803, -1.39885, -0.552262, -1.00672],
        [-1.21649, -1.21223, -1.63349, -1.21306, -1.63311, -1.20993, -1.62605, -0.644494, -1.22978, -0.648383, -1.23643,
         -0.537282, -0.537282, -0.537282, -1.24362, -1.23283, -1.24309, -0.539438, -0.539438, -0.539438, -0.539438,
         -0.540155, -1.38391],
        [0.28, 0.292217, 0.292217, 0.292217, 0.292217, 0.292217, 0.292217, 0.990369, 0.3, 1, 0.300347, 0.987244,
         0.307534,
         0.987244, 0.307534, 0.307534, 0.307534, 0.98253, 0.314189, 0.982447, 0.314189, 0.982173, 0.25848],
        [-0.442996, -0.447216, -0.444169, -0.444085, -0.444085, -0.444085, -0.442996, -0.442996, -0.442996, -0.442996],
        [-0.00851005, -0.0139635, -0.01307, -0.0226896, -0.0226896, -0.0226896, -0.0314114, -0.0314114, -0.0314114,
         -0.0314114],
        [-0.0151067, -0.00646016, -0.0141672, -0.0217896, -0.0217896, -0.0217896, -0.0287527, -0.0287527, -0.0287527,
         -0.0287527],
        [0.68703, 0.692461, 0.688271, 0.688147, 0.688147, 0.688147, 0.686536, 0.686536, 0.686536, 0.686536],
        [1.45211, 0.762257, 1.97824, 0.762047, 1.98611, 0.762047, 1.98159, -0.156044, 1.3486, -0.150818, 1.34717,
         -1.02853, -1.09495, -1.02853, 1.31624, 1.35992, 1.3266, -1.01882, -1.09885, -1.03326, -1.09885, -1.02983,
         1.39681],
        [0.225147, 0.172085, 0.305619, 0.16926, 0.301335, 0.16926, 0.296921, 0.250514, 0.338163, 0.253996, 0.336627,
         0.432157, 1.29735, 0.432157, 0.343055, 0.321179, 0.332374, 0.43099, 1.28887, 0.433358, 1.28887, 0.429557,
         0.30093],
        [0.0959931, -0.2004, -0.378869, -0.209581, -0.371364, -0.205663, -0.371364, -0.20794, -0.0937725, -0.205607,
         -0.0925806, -0.210057, -0.210057, -0.210057, -0.104743, -0.104743, -0.104743, -0.20774, -0.208769, -0.208769,
         -0.208769, -0.202734, -0.00694184],
        [-0.36169, -0.355017, -0.361798, -0.368392, -0.368392, -0.368392, -0.374469, -0.374469, -0.374469, -0.374469],
        [-0.00778286, -0.00805185, -0.00861058, -0.013757, -0.013757, -0.013757, -0.0185005, -0.0185005, -0.0185005,
         -0.0185005],
        [0.427606, 1.31343, 1.17115, 1.32003, 1.17115, 1.31961, 1.16891, 0.433524, 1.48392, 0.436842, 1.4877, 0.436903,
         0.436903, 0.436903, 0.544134, 1.39202, 0.551582, 0.551582, 1.39371, 0.545054, 1.39371, 0.550538, 1.00671],
        [1.20951, 1.63269, 1.2209, 1.62785, 1.21659, 1.63527, 1.21839, 1.22942, 0.634755, 1.22063, 0.633239, 1.22571,
         1.22571, 1.22571, 0.542696, 0.542696, 0.542696, 0.542696, 0.542696, 0.542696, 0.542696, 0.54341, 1.38393],
        [0.29, 0.288039, 0.288039, 0.288039, 0.288039, 0.288039, 0.288039, 0.288039, 0.999456, 0.294948, 0.999106,
         0.297176, 0.297176, 0.297176, 0.998175, 0.319835, 0.99517, 0.984693, 0.314212, 0.972582, 0.314212, 0.994792,
         0.258626],
        [-0.461552, -0.466003, -0.460132, -0.461748, -0.461748, -0.461748, -0.461797, -0.461797, -0.461797, -0.461797],
        [-0.00729717, -0.0134847, -0.0120429, -0.0212925, -0.0212925, -0.0212925, -0.0296896, -0.0296896, -0.0296896,
         -0.0296896],
        [-0.0151067, -0.00646016, -0.0141672, -0.0217896, -0.0217896, -0.0217896, -0.0287527, -0.0287527, -0.0287527,
         -0.0287527],
        [0.711593, 0.709981, 0.711381, 0.711414, 0.711414, 0.711414, 0.711838, 0.711838, 0.711838, 0.711838],
        [1.42244, 1.99577, 0.766917, 1.98966, 0.765486, 1.98966, 0.764463, 1.37289, -0.141201, 1.37047, -0.143125,
         1.38221, 1.39447, 1.38221, -1.01137, -1.09713, -1.01967, -1.01967, -1.09607, -1.02819, -1.09607, -1.02477,
         1.39682],
        [-0.251327, -0.301237, -0.170942, -0.302123, -0.170945, -0.300738, -0.168488, -0.315364, -0.270196, -0.316425,
         -0.269601, -0.316882, -0.264505, -0.316882, -0.426075, -1.28717, -0.43562, -0.43562, -1.28718, -0.431613,
         -1.28718, -0.42786, -0.304378],
        [0.0994838, 0.378756, 0.199865, 0.37171, 0.207483, 0.375686, 0.207483, 0.0973897, 0.192698, 0.101698, 0.184773,
         0.0935765, 0.0935765, 0.0935765, 0.202907, 0.202907, 0.202907, 0.202907, 0.202907, 0.202907, 0.202907,
         0.197226, 0.00675324]]
    if timestep == 0:
        times = [
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 4.56, 5.76, 6.36, 6.96, 7.56, 8.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16],
            [0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56, 5.16, 5.76, 6.36, 6.96, 7.56, 8.16, 8.76, 9.36, 9.96, 10.56,
             11.16,
             11.76, 12.36, 12.96, 13.56, 14.16]]
    else:
        times = set_times(names, keys, timestep, time_start)
        
    return keys