import sys
from naoqi import ALProxy
import numpy as np
import almath
import motion
import time

robotIP = "nao2.local"

motionProxy = ALProxy("ALMotion", robotIP, 9559)
posture = ALProxy("ALRobotPosture", robotIP, 9559)


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


def headMove():
    names = ["HeadYaw", "HeadPitch"]
    times = [[0.9], [0.9]]

    for i in range(3):
        motionProxy.angleInterpolation(names, [0.0, 0.5], times, True)
        motionProxy.angleInterpolation(names, [0.0, -0.5], times, True)


def rigth_arm():
    effector = ["RArm"]
    angleList1 = [1.385, 0, -1.454, 0]
    times = 1.0
    motionProxy.angleInterpolation(effector, angleList1, times, True)
    effector = ["RArm"]
    angleList2 = [1.489, -1.222, 0, 1.342]
    times = 1.0
    motionProxy.angleInterpolation(effector, angleList2, times, True)


def left_arm():
    effector = ["LArm"]
    angleList1 = [1.374, 0, 1.567, 0]
    times = 1.0
    motionProxy.angleInterpolation(effector, angleList1, times, True)
    effector = ["LArm"]
    angleList2 = [1.155, 1.210, 0, -1.178]
    times = 1.0
    motionProxy.angleInterpolation(effector, angleList2, times, True)

def dance1():

    names = ["RHipRoll","LHipRoll", "LKneePitch"
                  , "LAnklePitch", "LHipPitch"]
    angleLists = [[0.2], [0.2], [1], [-0.5], [-0.5]]
    times = [[1.0], [1.0], [1.0], [1.0], [1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)
    posture.goToPosture("Stand", 0.5)
    names = ["LHipRoll", "RHipRoll", "RKneePitch"
        , "RAnklePitch", "RHipPitch"]
    angleLists = [[0.2], [0.2], [1], [-0.5], [-0.5]]
    times = [[1.0], [1.0], [1.0], [1.0], [1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)


def naeNae(motion_proxy):
    motion_proxy.openHand("RHand")

    names = ["RKneePitch", "LKneePitch","LHipPitch", "RHipPitch",
            "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
            "RWristYaw"]
    angleLists = [25*almath.TO_RAD, 25*almath.TO_RAD, -32*almath.TO_RAD, -32*almath.TO_RAD,
                  -100*almath.TO_RAD, -76*almath.TO_RAD, 20*almath.TO_RAD, 60*almath.TO_RAD,
                  10*almath.TO_RAD]

    timeLists = 1.0
    isAbsolute = True

    motion_proxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    motion_proxy.waitUntilMoveIsFinished()

    names2 = ["LHipRoll", "RHipRoll", "RElbowRoll"]
    angleLists2 = [-10 * almath.TO_RAD, -10 * almath.TO_RAD, 88.5 * almath.TO_RAD]
    timeLists = 0.6
    motion_proxy.angleInterpolation(names2, angleLists2, timeLists, isAbsolute)

    names3 = ["LHipRoll", "RHipRoll", "RElbowRoll"]
    angleLists3 = [10 * almath.TO_RAD, 10 * almath.TO_RAD, 30 * almath.TO_RAD]
    timeLists = 0.6
    motion_proxy.angleInterpolation(names3, angleLists3, timeLists, isAbsolute)

def arm_move():
    effectorList = ["RArm", "LArm"]

    pathList = [
        [
            [1.385, 0.0, -1.454, 0.0],  # target 1 for "LArm"
            [1.489, -1.222, 0.0, 1.342]  # target 2 for "LArm"
        ],
        [
            [1.374, 0.0, 1.567, 0.0],  # target 1 for "RArm"
            [1.155, 1.210, 0.0, -1.178]  # target 2 for "RArm"
        ]
    ]

    coef = 1.0
    timesList = [[coef * (i + 1) for i in range(5)],  # for "LArm" in seconds
                 [coef * (i + 1) for i in range(6)]]  # for "RArm" in seconds

    isAbsolute = False

    # called cartesian interpolation
    motionProxy.angleInterpolation(effectorList, pathList, timesList, isAbsolute)


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

    # headMove()
    naeNae(motionProxy)
    # dance1()
    # left_arm()
    rigth_arm()
    posture.goToPosture("Stand", 0.5)
    time.sleep(5)


if __name__ == "__main__":
    robotIp = "nao2.local"

    if len(sys.argv) <= 1:
        print "Usage python motion_setFootStepDance.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
