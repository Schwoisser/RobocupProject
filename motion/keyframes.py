def set_timeline(names, keys, timestep, time_start):
    new_times = list()
    for i, name in enumerate(names):
        i_times = [ (time_start+k*timestep) for k in range(len(keys[i]))]
        new_times.append(i_times)   
    return new_times

# KEYFRAMES ###############################################################################

def nod(motionProxy, timestep=0.5):
    names = ["HeadYaw", "HeadPitch"]
    keys = [[0.0, 0.0, 0.0, 0.0], [0.5, -0.5, 0.5, -0.5]]
    times = [[timestep*(i+1) for i in range(4)],  # for "HeadPitch" in seconds
             [timestep*(i+1) for i in range(4)]]  # for "HeadYaw" in seconds
    # times = [[0.5, 1.5, 2.5, 3.5], [0.5, 1.5, 2.5, 3.5]]
    motionProxy.angleInterpolation(names, keys, times, True)

def macarena(motionProxy, timestep=0.538, time_start=1):
    #timestep = 0.538
    isAbsolute = True

    angleList1_right = [-1.257460117340087891e-01, -7.213997840881347656e-02, -2.454819679260253906e-01,
                  2.765393257141113281e-02, 8.893013000488281250e-02, 3.539999723434448242e-01]
    angleList2_right = [2.918791770935058594e-02, -1.565098762512207031e-01, 1.667416095733642578e+00,
                  1.231384277343750000e-02, 1.435782074928283691e+00, 3.539999723434448242e-01]
    angleList1_left = [-1.257460117340087891e-01, 7.213997840881347656e-02, 2.454819679260253906e-01,
                  2.765393257141113281e-02, 8.893013000488281250e-02, 3.539999723434448242e-01]
    angleList2_left = [2.918791770935058594e-02, 1.565098762512207031e-01, -1.667416095733642578e+00,
                  1.231384277343750000e-02, -1.435782074928283691e+00, 3.539999723434448242e-01]
    angleList3_right = [1.060036182403564453e+00, -7.946538925170898438e-01, -2.102000713348388672e-01,
                        1.285533905029296875e+00, -1.538205146789550781e-02, 3.371999859809875488e-01]
    angleList3_left = [1.060036182403564453e+00, 7.946538925170898438e-01, 2.102000713348388672e-01,
                        -1.285533905029296875e+00, -1.538205146789550781e-02, 3.371999859809875488e-01]
    angleList4_right = [-7.991721630096435547e-01, -5.875639915466308594e-01, 7.040641307830810547e-01,
                        1.560120105743408203e+00, 1.306926012039184570e+00, 3.651999831199645996e-01]
    angleList4_left = [-9.679961204528808594e-01, 6.902580261230468750e-01, -5.798940658569335938e-01,
                       -1.561570048332214355e+00, -1.380641937255859375e+00, 3.072000145912170410e-01]

    motionProxy.angleInterpolation("RArm", angleList1_right, timestep, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList1_left, timestep, isAbsolute)
    motionProxy.angleInterpolation("RArm", angleList2_right, timestep, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList2_left, timestep, isAbsolute)
    motionProxy.angleInterpolation("RArm", angleList4_right, timestep, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList4_left, timestep, isAbsolute)
    motionProxy.angleInterpolation("RArm", angleList3_right, timestep, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList3_left, timestep, isAbsolute)

    joint_names = ["HeadPitch", "HeadYaw"]

    angleList_head = [[0.5, -0.5, 0.5, -0.5], [0.8, -0.8, 0.8, -0.8]]

    times = [[0.5, 1.5, 2.5, 3.5], [0.5, 1.5, 2.5, 3.5]]
    motionProxy.angleInterpolation(joint_names, angleList_head, times, True)


def choreography_3(motionProxy):
    names_rechte = ["RHipRoll", "LHipRoll", "LKneePitch", "LAnklePitch", "LHipPitch"]
    angleList1 = [[0.2], [0.2], [1], [-0.5], [-0.5]]
    angleList2 = [[0.0], [0.0], [0.0], [0.0], [0.0]]
    isAbsolute = True

    names_linke = ["LHipRoll", "RHipRoll", "RKneePitch", "RAnklePitch", "RHipPitch"]
    times = [[0.7]]*5
    angleList_left1 = [[-0.2], [-0.2], [1], [-0.5], [-0.5]]
    angleList_left2 = [[0.0], [0.0], [0.0], [0.0], [0.0]]

    for i in range(3):
        motionProxy.angleInterpolation(names_rechte, angleList1, times, isAbsolute)
        motionProxy.angleInterpolation(names_rechte, angleList2, times, isAbsolute)
        motionProxy.angleInterpolation(names_linke, angleList_left1, times, isAbsolute)
        motionProxy.angleInterpolation(names_linke, angleList_left2, times, isAbsolute)

######################################################
# headmmove_1 FEHLERHAFT, da 
# Body Max Velocity is not respected. LShoulderPitch: 
#            Max velocity  : +8.26797 rad.s-1
#            Given velocity: +9.21377 rad.s-1

def headmmove_1(motionProxy):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.76, 1.96, 3.16, 4.36])
    keys.append([-0.0106666, -0.0141376, -0.0141376, -0.0141376])

    names.append("HeadYaw")
    times.append([0.76, 1.96, 3.16, 4.36])
    keys.append([-0.674338, 0.638078, -0.683508, 0.638078])

    names.append("LAnklePitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([0.0828387, -0.488692, 0.0836714, -0.495674, 0.0836714, -0.48885, 0.0836714, -0.504072, 0.0836714])

    names.append("LAnkleRoll")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([-0.103341, -0.102974, -0.103341, -0.101229, -0.103341, -0.102378, -0.103341, -0.102378, -0.103341])

    names.append("LElbowRoll")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([-0.41295, -0.420158, -0.41295, -0.41295, -0.417546, -0.41295, -0.41295])

    names.append("LElbowYaw")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([-1.21064, -1.22097, -1.20062, -1.20062, -1.21724, -1.20062, -1.20062])

    names.append("LHand")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([0.292284, 0.3, 0.292284, 0.292284, 0.3, 0.292284, 0.292284])

    names.append("LHipPitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([0.122436, -0.596903, 0.123575, -0.612611, 0.123575, -0.610563, 0.123575, -0.606502, 0.123575])

    names.append("LHipRoll")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([0.121781, 0.122173, 0.121781, 0.122173, 0.121781, 0.114832, 0.121781, 0.114832, 0.121781])

    names.append("LHipYawPitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([-0.174015, 0.0872665, -0.174015, 0.0785398, -0.174015, 0.0802851, -0.174015, 0.0872665, -0.174015])

    names.append("LKneePitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([-0.0829613, 1.02451, -0.0851616, 1.02974, -0.0851616, 1.03448, -0.0851616, 1.03673, -0.0851616])

    names.append("LShoulderPitch")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([1.42708, 1.38749, 1.44722, 1.44722, 1.40547, 1.44722, 1.44722])

    names.append("LShoulderRoll")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([0.257591, 0.338173, 0.227903, 0.227903, 0.320011, 0.227903, 0.227903])

    names.append("LWristYaw")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([-0.109248, -0.0966509, -0.109248, -0.109248, -0.106531, -0.109248, -0.109248])

    names.append("RAnklePitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([0.0828387, -0.488692, 0.0836714, -0.502655, 0.0836714, -0.488692, 0.0836714, -0.504072, 0.0836714])

    names.append("RAnkleRoll")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([0.103341, 0.102974, 0.103341, 0.10472, 0.103341, 0.102974, 0.103341, 0.0996395, 0.103341])

    names.append("RElbowRoll")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([0.41295, 0.415691, 0.41295, 0.41295, 0.41295, 0.41295, 0.41295])

    names.append("RElbowYaw")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([1.21064, 1.21447, 1.20062, 1.20062, 1.21064, 1.20062, 1.20062])

    names.append("RHand")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([0.292284, 0.292284, 0.292284, 0.292284, 0.292284, 0.292284, 0.292284])

    names.append("RHipPitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([0.122436, -0.596903, 0.123575, -0.610865, 0.123575, -0.607375, 0.123575, -0.606502, 0.123575])

    names.append("RHipRoll")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([-0.121781, -0.122173, -0.121781, -0.120428, -0.121781, -0.122173, -0.121781, -0.117404, -0.121781])

    names.append("RHipYawPitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([-0.174015, 0.0872665, -0.174015, 0.0785398, -0.174015, 0.0802851, -0.174015, 0.0872665, -0.174015])

    names.append("RKneePitch")
    times.append([0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96])
    keys.append([-0.0829613, 1.02451, -0.0851616, 1.03498, -0.0851616, 1.02451, -0.0851616, 1.03673, -0.0851616])

    names.append("RShoulderPitch")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([1.42708, 1.3873, 1.44722, 1.44722, 1.40547, 1.44722, 1.44722])

    names.append("RShoulderRoll")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([-0.257591, -0.338594, -0.227903, -0.227903, -0.320011, -0.227903, -0.227903])

    names.append("RWristYaw")
    times.append([0.16, 0.76, 1.36, 2.56, 3.16, 3.76, 4.96])
    keys.append([0.109248, 0.109171, 0.109248, 0.109248, 0.109248, 0.109248, 0.109248])

    motionProxy.angleInterpolation(names, keys, times, True)
    #return names, times, keys

def dance4(motionProxy, timestep=0, time_start=1):
    names = list()
    keys = list()

    names.append("HeadPitch")
    keys.append([-0.161711, -0.161711, -0.161711, -0.160616, -0.161711, -0.160616, -0.160616])

    names.append("HeadYaw")
    keys.append([-0.0788623, -0.922569, -0.0848661, 0.758922, -0.0848661, -0.124136, -0.077879])

    names.append("LAnklePitch")
    keys.append([0.0809129, 0.0809129, 0.0809129, 0.0845001, 0.0809129, 0.0845001])

    names.append("LAnkleRoll")
    keys.append([-0.109096, -0.109096, -0.109096, -0.110361, -0.109096, -0.110361])

    names.append("LElbowRoll")
    keys.append([-1.29904, -1.31249, -1.3075, -1.38153, -1.3075, -1.38845, -1.31136])

    names.append("LElbowYaw")
    keys.append([-1.20239, -1.18508, -1.19552, -1.20218, -1.19552, -1.3705, -1.15993])

    names.append("LHand")
    keys.append([0.0198864, 0.02, 0.0106246, 0.992796, 0.0106246, 0.965946, 0.00719799])

    names.append("LHipPitch")
    keys.append([0.11994, 0.11994, 0.11994, 0.121665, 0.11994, 0.121665])

    names.append("LHipRoll")
    keys.append([0.11865, 0.11865, 0.11865, 0.109498, 0.11865, 0.109498])

    names.append("LHipYawPitch")
    keys.append([-0.176013, -0.176278, -0.176013, -0.173871, -0.176013, -0.173871])

    names.append("LKneePitch")
    keys.append([-0.0872551, -0.0872551, -0.0872551, -0.0872551, -0.0872551, -0.0872551])

    names.append("LShoulderPitch")
    keys.append([-0.0991988, -0.10472, -0.106185, -0.240072, -0.106185, -0.106534, -0.11276])

    names.append("LShoulderRoll")
    keys.append([-0.138368, -0.176278, -0.151091, 1.06044, -0.151091, 1.07142, -0.217529])

    names.append("LWristYaw")
    keys.append([-0.122806, -0.122173, -0.122806, -0.123708, -0.122806, -0.123708, -0.123708])

    names.append("RAnklePitch")
    keys.append([0.0881388, 0.0872665, 0.0881388, 0.0844999, 0.0881388, 0.0844999])

    names.append("RAnkleRoll")
    keys.append([0.112412, 0.111701, 0.112412, 0.110356, 0.112412, 0.110356])

    names.append("RElbowRoll")
    keys.append([1.30214, 1.39012, 1.31074, 1.30332, 1.31074, 1.38746, 1.31542])

    names.append("RElbowYaw")
    keys.append([1.21074, 1.38484, 1.21126, 1.21659, 1.21126, 1.38824, 1.15929])

    names.append("RHand")
    keys.append([0.0199652, 0.981179, 0.01, 0.0167444, 0.01, 0.964357, 0.00719799])

    names.append("RHipPitch")
    keys.append([0.11994, 0.120428, 0.115192, 0.121665, 0.115192, 0.121665])

    names.append("RHipRoll")
    keys.append([-0.118644, -0.118682, -0.118645, -0.109492, -0.118645, -0.109492])

    names.append("RHipYawPitch")
    keys.append([-0.176013, -0.176278, -0.176013, -0.173871, -0.176013, -0.173871])

    names.append("RKneePitch")
    keys.append([-0.0872551, -0.0872665, -0.0872551, -0.0872551, -0.0872551, -0.0872551])

    names.append("RShoulderPitch")
    keys.append([-0.0977814, -0.110644, -0.10821, -0.101841, -0.10821, -0.101647, -0.116931])

    names.append("RShoulderRoll")
    keys.append([0.129466, -1.2131, 0.137881, 0.119137, 0.137881, -1.19888, 0.220723])

    names.append("RWristYaw")
    keys.append([0.114776, 0.114776, 0.115192, 0.123077, 0.115192, 0.123077, 0.123077])

    if timestep == 0:
        times = list()
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # HeadPitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # HeadYaw
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # LAnklePitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # LAnkleRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # LElbowRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # LElbowYaw
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # LHand
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # LHipPitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # LHipRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # LHipYawPitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # LKneePitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # LShoulderPitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # LShoulderRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # LWristYaw
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # RAnklePitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # RAnkleRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # RElbowRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # RElbowYaw
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # RHand
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # RHipPitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # RHipRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # RHipYawPitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76]) # RKneePitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # RShoulderPitch
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # RShoulderRoll
        times.append([0.96, 1.56, 2.36, 3.16, 3.96, 4.76, 5.56]) # RWristYaw
    else:
        times = set_timeline(names, keys, timestep, time_start)

    motionProxy.angleInterpolation(names, keys, times, True)
    #return names, times, keys

def dance5(motionProxy,timestep=0, time_start=1):
    names = list()
    keys = list()

    names.append("HeadPitch")
    keys.append(
        [-0.019984, -0.000672507, -0.000672507, -0.231865, -0.222498, -0.228495, -0.228495, -0.222816, -0.228495,
         -0.230342, -0.228495, -0.226552, -0.170989])

    names.append("HeadYaw")
    keys.append(
        [-0.00464392, 0, 0, 0.0181209, 0.0173867, 0.0171171, 0.0167786, 0.016399, 0.0167786, 0.0167786, 0.016399,
         0.016399, 0.00558785])

    names.append("LAnklePitch")
    keys.append(
        [-0.349794, -0.174185, -0.171502, -0.164061, -0.167552, -0.404916, -0.161303, -0.407489, -0.40182, -0.167108,
         -0.172115, -0.395586, 0.078972])

    names.append("LAnkleRoll")
    keys.append(
        [-0.00149202, -0.0485521, -0.0522367, -0.0628318, -0.0610865, -0.0616461, -0.061869, -0.061869, -0.0616281,
         -0.0611527, -0.0616281, -0.070956, -0.107509])

    names.append("LElbowRoll")
    keys.append(
        [-0.977116, -0.942478, -0.947551, -1.26422, -1.26141, -1.34842, -1.27056, -1.33812, -1.3374, -1.32876, -1.32994,
         -1.33012, -1.26388, -0.419876])

    names.append("LElbowYaw")
    keys.append(
        [-1.35456, -1.37183, -1.36987, 0.457252, 0.450838, -1.30851, 0.449817, -1.30209, -1.30316, -1.29725, -1.54985,
         -1.5493, 0.315294, -1.2006])

    names.append("LHand")
    keys.append(
        [0.2728, 0.26, 0.262901, 0.267093, 0.271569, 0.272798, 0.263606, 0.263606, 0.263606, 0.263606, 0.26, 0.263606,
         0.260375, 0.293589])

    names.append("LHipPitch")
    keys.append(
        [-0.361982, -0.21201, -0.208418, -0.197222, -0.204204, -1.11177, -0.203015, -1.10724, -1.10724, -0.176278,
         -0.179532, -1.10174, 0.12602])

    names.append("LHipRoll")
    keys.append(
        [0.00771189, 0.0546468, 0.0584526, 0.0680678, 0.0680678, 0.0687065, 0.0674716, 0.0677568, 0.0675128, 0.0671775,
         0.0669856, 0.0763273, 0.110183])

    names.append("LHipYawPitch")
    keys.append(
        [-0.00609398, -0.191061, -0.190223, -0.188496, -0.181514, -0.141372, -0.175975, -0.148155, -0.151908, -0.150098,
         -0.155616, -0.148661, -0.162735])

    names.append("LKneePitch")
    keys.append(
        [0.699462, 0.363943, 0.363941, 0.361283, 0.359538, 1.43117, 0.358737, 1.42615, 1.42615, 0.415388, 0.418919,
         1.43093, -0.0905938])

    names.append("LShoulderPitch")
    keys.append([0.317496, 0.911062, 0.914764, 0.675238, 0.677544, -0.303813, 0.666206, -0.301066, -0.301525, -0.300513,
                 -0.300197, -0.300736, -0.363447, 1.44072])

    names.append("LShoulderRoll")
    keys.append(
        [0.282214, 0.312414, 0.316482, 1.24704, 1.24337, 1.23506, 1.23648, 1.23952, 1.23648, 1.24319, -0.0750492,
         -0.0653032, 0.114485, 0.215601])

    names.append("LWristYaw")
    keys.append(
        [0.0152981, -0.015708, 0.009239, -1.59378, -1.59267, -1.24433, -1.57769, -1.25507, -1.2585, -1.26482, 0.197222,
         0.197679, -0.47319, 0.0984275])

    names.append("RAnklePitch")
    keys.append(
        [-0.346642, -0.174185, -0.171502, -0.164981, -0.167552, -0.404916, -0.161303, -0.407489, -0.40182, -0.167108,
         -0.172115, -0.395586, 0.0789718])

    names.append("RAnkleRoll")
    keys.append(
        [0.00310993, 0.0482817, 0.0519815, 0.0605263, 0.0610865, 0.0611668, 0.0608167, 0.0608167, 0.0605905, 0.0604224,
         0.0603441, 0.0609399, 0.110732])

    names.append("RElbowRoll")
    keys.append(
        [0.975666, 0.946649, 1.27002, 1.26547, 1.35748, 1.26463, 1.34772, 1.27133, 1.35423, 1.33495, 1.31867, 1.32496,
         1.31337, 0.42031])

    names.append("RElbowYaw")
    keys.append(
        [1.35601, 1.37368, -0.459238, -0.458732, 1.3189, -0.390214, 1.3137, -0.384081, 1.4671, 0.161477, 0.160371,
         1.54074, 1.52927, 1.20332])

    names.append("RHand")
    keys.append(
        [0.2736, 0.261572, 0.262901, 0.267093, 0.26883, 0.274328, 0.265166, 0.265166, 0.265166, 0.265166, 0.265166,
         0.265166, 0.270586, 0.291594])

    names.append("RHipPitch")
    keys.append(
        [-0.368202, -0.211993, -0.208401, -0.20735, -0.204204, -1.11177, -0.203015, -1.10729, -1.10729, -0.176278,
         -0.179532, -1.10174, 0.12602])

    names.append("RHipRoll")
    keys.append(
        [-0.0199001, -0.0546389, -0.0584451, -0.067236, -0.0680678, -0.0683314, -0.0675905, -0.0675905, -0.0675631,
         -0.067236, -0.0672847, -0.0762079, -0.110153])

    names.append("RHipYawPitch")
    keys.append(
        [-0.00609398, -0.191061, -0.190223, -0.188496, -0.181514, -0.141372, -0.175975, -0.148155, -0.151908, -0.150098,
         -0.155616, -0.148661, -0.162735])

    names.append("RKneePitch")
    keys.append(
        [0.699546, 0.363927, 0.363926, 0.362414, 0.359538, 1.43117, 0.358737, 1.42616, 1.42616, 0.415388, 0.418919,
         1.43093, -0.0905938])

    names.append("RShoulderPitch")
    keys.append([0.329852, 0.908001, 0.669714, 0.673362, -0.307077, 0.610288, -0.297753, 0.608492, 0.0943403, 0.0903883,
                 0.0956723, -0.298265, -0.293671, 1.4391])

    names.append("RShoulderRoll")
    keys.append([-0.280764, -0.314782, -1.25623, -1.25512, -1.25141, -1.24295, -1.24338, -1.24876, 0.0713389, 0.0563975,
                 0.0313276, 0.0705488, 0.0609141, -0.223964])

    names.append("RWristYaw")
    keys.append([0.053648, 0.00836283, 1.6006, 1.5994, 1.2422, 1.5775, 1.25662, 1.56129, 0.149215, 0.154147, 0.156871,
                 -0.192939, -0.187583, 0.0939441])
    if timestep == 0:
        times = list()
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # HeadPitch
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # HeadYaw
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LAnklePitch
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LAnkleRoll
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LElbowRoll
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LElbowYaw
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LHand
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LHipPitch
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LHipRoll
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LHipYawPitch
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LKneePitch
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LShoulderPitch
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LShoulderRoll
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # LWristYaw
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RAnklePitch
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RAnkleRoll
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RElbowRoll
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RElbowYaw
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RHand
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RHipPitch
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RHipRoll
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RHipYawPitch
        times.append([0.96, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RKneePitch
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RShoulderPitch
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RShoulderRoll
        times.append([0.96, 1.72, 2.52, 3.32, 4.12, 4.92, 6.12, 7.32, 8.52, 9.32, 10.52, 11.72, 12.52, 13.72]) # RWristYaw
    else:
        times = set_timeline(names, keys, timestep, time_start)

    #return names, times, keys
    motionProxy.angleInterpolation(names, keys, times, True)

def dance6(motionProxy, timestep=0, time_start=1):
    # Arms left to right
    names = list()
    keys = list()

    names.append("HeadPitch")
    keys.append([-0.160616, -0.160616, -0.160616, -0.160616, -0.160616, -0.160616])

    names.append("HeadYaw")
    keys.append([-0.634909, 0.806347, -0.621554, 0.802415, -0.622761, 0.802851])

    names.append("LElbowRoll")
    keys.append([-0.420624, -1.0472, -0.420624, -1.20253, -0.420624, -1.0472, -0.420624, -1.20253, -0.420624, -1.0472,
                 -0.420624, -1.20253])

    names.append("LElbowYaw")
    keys.append([-1.19381, -0.940732, -1.19381, -1.68424, -1.19381, -0.940732, -1.19381, -1.68424, -1.19381, -0.940732,
                 -1.19381, -1.68424])

    names.append("LHand")
    keys.append([0.3, 0.38, 0.3, 0.37, 0.3, 0.38, 0.3, 0.37, 0.3, 0.38, 0.3, 0.37])

    names.append("LShoulderPitch")
    keys.append(
        [0.237365, 0.0453786, 0.237365, -0.0471239, 0.237365, 0.0453786, 0.237365, -0.0471239, 0.237365, 0.0453786,
         0.237365, -0.0471239])

    names.append("LShoulderRoll")
    keys.append(
        [0.0471239, 0.0820305, 0.0471239, 0.0872665, 0.0471239, 0.0820305, 0.0471239, 0.0872665, 0.0471239, 0.0820305,
         0.0471239, 0.0872665])

    names.append("LWristYaw")
    keys.append(
        [-0.0959931, -0.0680678, -0.0959931, -0.0698132, -0.0959931, -0.0680678, -0.0959931, -0.0698132, -0.0959931,
         -0.0680678, -0.0959931, -0.0698132])

    names.append("RElbowRoll")
    keys.append(
        [0.420624, 1.1973, 0.420624, 1.06989, 0.420624, 1.1973, 0.420624, 1.06989, 0.420624, 1.1973, 0.420624, 1.06989])

    names.append("RElbowYaw")
    keys.append(
        [1.19381, 1.70519, 1.19381, 1.11352, 1.19381, 1.70519, 1.19381, 1.11352, 1.19381, 1.70519, 1.19381, 1.11352])

    names.append("RHand")
    keys.append([0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])

    names.append("RShoulderPitch")
    keys.append(
        [0.237365, 0.0523599, 0.237365, 0.0558505, 0.237365, 0.0523599, 0.237365, 0.0558505, 0.237365, 0.0523599,
         0.237365, 0.0558505])

    names.append("RShoulderRoll")
    keys.append(
        [-0.0471239, -0.16057, -0.0471239, -0.00523599, -0.0471239, -0.16057, -0.0471239, -0.00523599, -0.0471239,
         -0.16057, -0.0471239, -0.00523599])

    names.append("RWristYaw")
    keys.append(
        [0.0959931, 0.0959931, 0.0959931, 0.0959931, 0.0959931, 0.0959931, 0.0959931, 0.0959931, 0.0959931, 0.0959931,
         0.0959931, 0.0959931])

    if timestep == 0:
        times = list()
        times.append([1.16, 2.36, 3.56, 4.76, 5.96, 7.16]) # HeadPitch
        times.append([1.16, 2.36, 3.56, 4.76, 5.96, 7.16]) # HeadYaw
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # LElbowRoll
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # LElbowYaw
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # LHand
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # LShoulderPitch
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # LShoulderRoll
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # LWristYaw
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # RElbowRoll
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # RElbowYaw
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # RHand
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # RShoulderPitch
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # RShoulderRoll
        times.append([0.56, 1.16, 1.76, 2.36, 2.96, 3.56, 4.16, 4.76, 5.36, 5.96, 6.56, 7.16]) # RWristYaw
    else:
        times = set_timeline(names, keys, timestep, time_start)

    motionProxy.angleInterpolation(names, keys, times, True)
    #return names, times, keys
