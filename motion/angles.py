import sys
from naoqi import ALProxy
import numpy as np
import almath
import motion
import time

robotIP = "nao2.local"

motionProxy = ALProxy("ALMotion", robotIP, 9559)
posture = ALProxy("ALRobotPosture", robotIP, 9559)
ttsProxy = ALProxy("ALTextToSpeech", robotIP, 9559)

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def StiffnessOffHand(proxy):

    print "Left_Hand_Angles: ", motionProxy.getAngles("LArm", True)

    pNames = "LArm"
    pStiffnessLists = 0
    pTimeLists = 0.5

    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists, True)


def choreography_1():
    effector_names = ["HeadYaw", "HeadPitch"]
    times = [[0.9], [0.9]]

    for i in range(1):
        motionProxy.post.angleInterpolation(effector_names, [0.0, 0.5], times, True)
        motionProxy.post.angleInterpolation(effector_names, [0.0, -0.5], times, True)

    effector = ["RArm"]
    angleList1 = [1.385, 0, -1.454, 0]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList1, times, True)

    effector = ["LArm"]
    angleList1 = [1.385, 0, 1.454, 0]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList1, times, True)

    effector = ["RArm"]
    angleList2 = [1.489, -1.222, 0, 1.342]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList2, times, True)

    effector = ["LArm"]
    angleList2 = [1.489, 1.222, 0, -1.342]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList2, times, True)
def headMove():
    names = ["HeadYaw", "HeadPitch"]
    times = [[0.9], [0.9]]

    for i in range(3):
        motionProxy.angleInterpolation(names, [0.0, 0.5], times, True)
        motionProxy.angleInterpolation(names, [0.0, -0.5], times, True)


def choreography_2():
    effector = ["RArm"]
    times = 1.0
    angleList1 = [-1.615344047546386719e+00, 2.458596229553222656e-02, -1.581512093544006348e+00,
                  -3.490658476948738098e-02]

    angleList2 = [-1.621479988098144531e+00, -9.571740627288818359e-01, -1.509414076805114746e+00,
                  -3.490658476948738098e-02]
    for i in range(3):
        motionProxy.post.angleInterpolation(effector, angleList1, times, True)
        motionProxy.post.angleInterpolation(effector, angleList2, times, True)

    names = ["RHipRoll","LHipRoll", "LKneePitch", "LAnklePitch", "LHipPitch"]
    angleList1 = [[0.2], [0.2], [1], [-0.5], [-0.5]]
    angleList2 = [[0.0], [0.0], [0.0], [0.0], [0.0]]
    times = [[1.0], [1.0], [1.0], [1.0], [1.0]]
    isAbsolute = True
    for i in range(3):
        motionProxy.angleInterpolation(names, angleList1, times, isAbsolute)
        motionProxy.angleInterpolation(names, angleList2, times, isAbsolute)

    names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RHipRoll", "LHipRoll", "LKneePitch",
             "LAnklePitch", "LHipPitch", "RKneePitch", "RAnklePitch", "RHipPitch"]
    angleLists = [[1.45], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0],[0.0], [0.0], [0.0]]
    times = [[1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0],[1.0], [1.0], [1.0], [1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

    effector = ["LArm"]
    times = 1.0
    angleList1 = [-1.615344047546386719e+00, -2.458596229553222656e-02, 1.581512093544006348e+00,
                  -3.490658476948738098e-02]

    angleList2 = [-1.621479988098144531e+00, 9.571740627288818359e-01, 1.509414076805114746e+00,
                  -3.490658476948738098e-02]
    for i in range(3):
        motionProxy.post.angleInterpolation(effector, angleList1, times, True)
        motionProxy.post.angleInterpolation(effector, angleList2, times, True)

    names = ["LHipRoll", "RHipRoll", "RKneePitch", "RAnklePitch", "RHipPitch"]
    times = [[1.0], [1.0], [1.0], [1.0], [1.0]]
    isAbsolute = True
    angleList1 = [[-0.2], [-0.2], [1], [-0.5], [-0.5]]

    angleList2 = [[0.0], [0.0], [0.0], [0.0], [0.0]]

    for i in range(3):
        motionProxy.angleInterpolation(names, angleList1, times, isAbsolute)
        motionProxy.angleInterpolation(names, angleList2, times, isAbsolute)


def main(robotIP):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
    try:
        posture = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    StiffnessOn(motionProxy)
    posture.goToPosture("Stand", 0.5)

    for i in range(1):
        choreography_1()

    posture.goToPosture("Stand", 0.5)
    choreography_2()
    posture.goToPosture("Stand", 0.5)
    ttsProxy.say("Thank you")
    motionProxy.rest()

    time.sleep(5)


if __name__ == "__main__":
    robotIp = "nao2.local"

    if len(sys.argv) <= 1:
        print "Usage python motion_setFootStepDance.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
