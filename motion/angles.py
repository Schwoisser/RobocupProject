import sys
from naoqi import ALProxy
import time
import keyframes as kf
robotIP = "nao34.local"
port = 9559
motionProxy = ALProxy("ALMotion", robotIP, port)
posture = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)


def set_timeline(names, keys, timestep, time_start):
    new_times = list()
    for i, name in enumerate(names):
        i_times = [(time_start + k * timestep) for k in range(len(keys[i]))]
        new_times.append(i_times)
    return new_times


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def arm_walk(motionProxy, timestep=0, time_start=1):
    # Choregraphe simplified export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-1.17518, -1.34913, -1.18313, -1.34525, -1.18174, -1.34981, -1.01257])

    names.append("LElbowYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-1.21223, -1.63349, -1.21306, -1.63311, -1.20993, -1.62605, -1.3866])

    names.append("LHand")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.292217, 0.292217, 0.292217, 0.292217, 0.292217, 0.292217, 0.255429])

    names.append("LShoulderPitch")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.762257, 1.97824, 0.762047, 1.98611, 0.762047, 1.98159, 1.39335])

    names.append("LShoulderRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.172085, 0.305619, 0.16926, 0.301335, 0.16926, 0.296921, 0.291206])

    names.append("LWristYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-0.2004, -0.378869, -0.209581, -0.371364, -0.205663, -0.371364, -0.003358])

    names.append("RElbowRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([1.31343, 1.17115, 1.32003, 1.17115, 1.31961, 1.16891, 1.00668])

    names.append("RElbowYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([1.63269, 1.2209, 1.62785, 1.21659, 1.63527, 1.21839, 1.38994])

    names.append("RHand")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.288039, 0.288039, 0.288039, 0.288039, 0.288039, 0.288039, 0.253956])

    names.append("RShoulderPitch")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([1.99577, 0.766917, 1.98966, 0.765486, 1.98966, 0.764463, 1.39663])

    names.append("RShoulderRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-0.301237, -0.170942, -0.302123, -0.170945, -0.300738, -0.168488, -0.296894])

    names.append("RWristYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.378756, 0.199865, 0.37171, 0.207483, 0.375686, 0.207483, 0.00800279])

    motionProxy.angleInterpolation(names, keys, times, True)


def arm_snap(motionProxy, timestep=0, time_start=1):

    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([-1.51957, -0.459482, -1.51957, -0.459482, -1.00344])

    names.append("LElbowYaw")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([-0.644494, -1.22978, -0.644494, -1.22978, -1.38021])

    names.append("LHand")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([0.990369, 0.3, 0.990369, 0.3, 0.250802])

    names.append("LShoulderPitch")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([-0.156044, 1.3486, -0.156044, 1.3486, 1.39686])

    names.append("LShoulderRoll")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([0.250514, 0.338163, 0.250514, 0.338163, 0.306721])

    names.append("LWristYaw")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([-0.20794, -0.0937725, -0.20794, -0.0937725, -0.0057317])

    names.append("RElbowRoll")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([0.433524, 1.48392, 0.433524, 1.48392, 1.01286])

    names.append("RElbowYaw")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([1.22942, 0.634755, 1.22942, 0.634755, 1.381])

    names.append("RHand")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([0.288039, 0.999456, 0.288039, 0.999456, 0.251382])

    names.append("RShoulderPitch")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([1.37289, -0.141201, 1.37289, -0.141201, 1.39664])

    names.append("RShoulderRoll")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([-0.315364, -0.270196, -0.315364, -0.270196, -0.290009])

    names.append("RWristYaw")
    times.append([0.96, 1.76, 2.56, 3.36, 4.16])
    keys.append([0.0973897, 0.192698, 0.0973897, 0.192698, 0.0011637])

    motionProxy.angleInterpolation(names, keys, times, True)


def arm_yeah(motionProxy, timestep=0, time_start=1):
    # Choregraphe simplified export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-0.545569, -1.40801, -0.545569, -0.463039, -0.440982, -0.451639, -1.00963])

    names.append("LElbowYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-0.537282, -0.537282, -0.537282, -1.24362, -1.23283, -1.24309, -1.38043])

    names.append("LHand")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.987244, 0.307534, 0.987244, 0.307534, 0.307534, 0.307534, 0.25017])

    names.append("LShoulderPitch")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-1.02853, -1.09495, -1.02853, 1.31624, 1.35992, 1.3266, 1.39681])

    names.append("LShoulderRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.432157, 1.29735, 0.432157, 0.343055, 0.321179, 0.332374, 0.306169])

    names.append("LWristYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-0.210057, -0.210057, -0.210057, -0.104743, -0.104743, -0.104743, -0.00682389])

    names.append("RElbowRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.436903, 0.436903, 0.436903, 0.544134, 1.39202, 0.551582, 1.00103])

    names.append("RElbowYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([1.22571, 1.22571, 1.22571, 0.542696, 0.542696, 0.542696, 1.38692])

    names.append("RHand")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.297176, 0.297176, 0.297176, 0.998175, 0.319835, 0.99517, 0.252205])

    names.append("RShoulderPitch")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([1.38221, 1.39447, 1.38221, -1.01137, -1.09713, -1.01967, 1.39121])

    names.append("RShoulderRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([-0.316882, -0.264505, -0.316882, -0.426075, -1.28717, -0.43562, -0.302653])

    names.append("RWristYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96, 4.56])
    keys.append([0.0935765, 0.0935765, 0.0935765, 0.202907, 0.202907, 0.202907, 0.00204323])

    motionProxy.angleInterpolation(names, keys, times, True)


def arm_yeahboth(motionProxy, timestep=0, time_start=1):

    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([-1.39885, -0.546803, -1.39885, -0.552262, -1.39885, -1.01518])

    names.append("LElbowYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([-0.539438, -0.539438, -0.539438, -0.540155, -0.539438, -1.38895])

    names.append("LHand")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([0.314189, 0.982447, 0.314189, 0.982173, 0.314189, 0.259753])

    names.append("LShoulderPitch")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([-1.09885, -1.03326, -1.09885, -1.02983, -1.09885, 1.39391])

    names.append("LShoulderRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([1.28887, 0.433358, 1.28887, 0.429557, 1.28887, 0.302412])

    names.append("LWristYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([-0.208769, -0.208769, -0.208769, -0.202734, -0.208769, -0.00050914])

    names.append("RElbowRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([1.39371, 0.545054, 1.39371, 0.550538, 1.39371, 1.01511])

    names.append("RElbowYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([0.542696, 0.542696, 0.542696, 0.54341, 0.542696, 1.38895])

    names.append("RHand")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([0.314212, 0.972582, 0.314212, 0.994792, 0.314212, 0.259757])

    names.append("RShoulderPitch")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([-1.09607, -1.02819, -1.09607, -1.02477, -1.09607, 1.39391])

    names.append("RShoulderRoll")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([-1.28718, -0.431613, -1.28718, -0.42786, -1.28718, -0.302408])

    names.append("RWristYaw")
    times.append([0.96, 1.56, 2.16, 2.76, 3.36, 3.96])
    keys.append([0.202907, 0.202907, 0.202907, 0.197226, 0.202907, 0.000250858])

    motionProxy.angleInterpolation(names, keys, times, True)


def main(robotIP):
    StiffnessOn(motionProxy)
    posture.goToPosture("StandInit", 0.5)
    arm_walk(motionProxy)
    arm_snap(motionProxy)
    arm_yeah(motionProxy)
    arm_yeahboth(motionProxy)
    # ttsProxy.say("Thank you")
    # motionProxy.rest()

    time.sleep(5)


if __name__ == "__main__":

    robotIp = "nao34.local"

    if len(sys.argv) <= 1:
        print("Usage python  robotIP (optional default: 127.0.0.1)")
    else:
        robotIp = sys.argv[1]

    main(robotIp)
