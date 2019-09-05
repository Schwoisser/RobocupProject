import sys
from naoqi import ALProxy
import numpy as np
import almath
import motion
import time

robotIP = "nao6.local"

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

    pNames = ["LLeg", "RLeg"]
    pStiffnessLists = 0
    pTimeLists = 0.5

    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists, True)


def sit_test():
    names = ["LHipYawPitch", "LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch", "LAnkleRoll",
             "RHipYawPitch", "RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll"]
    times = [[0.5]] * 12
    angleLists3 = [-1.625621318817138672e-01, 2.151799201965332031e-02, -2.975540161132812500e-01,
                   4.954400062561035156e-01, -9.208202362060546875e-02, -2.296805381774902344e-02,
                   -1.625621318817138672e-01, -6.131792068481445312e-02, -3.007059097290039062e-01,
                   4.970579147338867188e-01, -7.665801048278808594e-02, 5.219793319702148438e-02]
    angleLists1 = [-1.702320575714111328e-01, 1.012859344482421875e-01, 1.304318904876708984e-01,
                   -8.901405334472656250e-02, 9.046411514282226562e-02, -1.288139820098876953e-01,
                   -1.702320575714111328e-01, -9.966802597045898438e-02, 1.303479671478271484e-01,
                   -8.125996589660644531e-02, 8.901405334472656250e-02, 1.304318904876708984e-01]

    for i in range(3):
        motionProxy.angleInterpolation(names, angleLists3, times, True)
        time.sleep(1)
        motionProxy.angleInterpolation(names, angleLists1, times, True)
        time.sleep(1)


def sit():
    names = ["LHipYawPitch", "LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch", "LAnkleRoll",
             "RHipYawPitch", "RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll"]

    times = [[0.9]] * 12
    angleLists1 = [-1.702320575714111328e-01, 1.012859344482421875e-01, 1.304318904876708984e-01,
                   -8.901405334472656250e-02, 9.046411514282226562e-02, -1.288139820098876953e-01,
                  -1.702320575714111328e-01, -9.966802597045898438e-02, 1.303479671478271484e-01,
                   -8.125996589660644531e-02, 8.901405334472656250e-02, 1.304318904876708984e-01]
    angleLists2 = [-2.453980445861816406e-01, 2.040638923645019531e-01, -6.841220855712890625e-01,
                   1.794738054275512695e+00, -1.006345748901367188e+00, -1.181260347366333008e-01,
                  -2.453980445861816406e-01, -1.150081157684326172e-01, -7.225558757781982422e-01,
                   1.820899963378906250e+00, -9.893879890441894531e-01, 1.104898452758789062e-01]

    for i in range(3):
        motionProxy.angleInterpolation(names, angleLists1, times, True)
        time.sleep(1)
        motionProxy.angleInterpolation(names, angleLists2, times, True)
        time.sleep(1)


def headMove_1():
    names = ["HeadPitch", "HeadYaw", "LAnklePitch", "LAnkleRoll", "LHipPitch", "LHipRoll", "LHipYawPitch", "LKneePitch",
             "RAnklePitch", "RAnkleRoll", "RHipPitch", "RHipRoll", "RHipYawPitch", "RKneePitch"]
    times = ([[0.76, 1.96, 3.16, 4.36]]*2) + [[0.16, 0.76, 1.36, 1.96, 2.56, 3.16, 3.76, 4.36, 4.96]]*12
    keys = [[-0.0141376, -0.0141376, -0.0141376, -0.0141376], [-0.683508, 0.638078, -0.683508, 0.638078],
            [0.0828387, -0.498408, 0.0836714, -0.5079, 0.0836714, -0.498408, 0.0836714, -0.5079, 0.0836714],
            [-0.103341, -0.106182, -0.103341, -0.103341, -0.103341, -0.106182, -0.103341, -0.103341, -0.103341],
            [0.122436, -0.610599, 0.123575, -0.611738, 0.123575, -0.610598, 0.123575, -0.611738, 0.123575],
            [0.121781, 0.119108, 0.121781, 0.121781, 0.121781, 0.119108, 0.121781, 0.121781, 0.121781],
            [-0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015],
            [-0.0829613, 1.03453, -0.0851616, 1.03673, -0.0851616, 1.03452, -0.0851616, 1.03673, -0.0851616],
            [0.0828387, -0.498408, 0.0836714, -0.5079, 0.0836714, -0.498408, 0.0836714, -0.5079, 0.0836714],
            [0.103341, 0.103341, 0.103341, 0.103341, 0.103341, 0.103341, 0.103341, 0.103341, 0.103341],
            [0.122436, -0.610599, 0.123575, -0.611738, 0.123575, -0.610598, 0.123575, -0.611738, 0.123575],
            [-0.121781, -0.121781, -0.121781, -0.121781, -0.121781, -0.121781, -0.121781, -0.121781, -0.121781],
            [-0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015, -0.174015],
            [-0.0829613, 1.03453, -0.0851616, 1.03673, -0.0851616, 1.03452, -0.0851616, 1.03673, -0.0851616]
            ]

    motion.angleInterpolation(names, keys, times, True)


def headMove():
    joint_names = ["HeadPitch", "HeadYaw"]

    angleList_head = [[0.5, -0.5, 0.5, -0.5], [0.8, -0.8, 0.8, -0.8]]

    times = [[0.5, 1.5, 2.5, 3.5], [0.5, 1.5, 2.5, 3.5]]
    motionProxy.angleInterpolation(joint_names, angleList_head, times, True)


def choreography_1():
    effector_names = ["HeadYaw", "HeadPitch"]
    times = [[0.6], [0.6]]

    for i in range(4):
        motionProxy.post.angleInterpolation(effector_names, [0.0, 0.5], times, True)
        motionProxy.post.angleInterpolation(effector_names, [0.0, -0.5], times, True)

    effector = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RHand"]
    angleList1 = [[1.385, 0, -1.454, 0, 0.292284], [1.385, 0, 1.454, 0, 0.292284]]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList1, times, True)

    effector = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LHand"]
    angleList1 = [1.385, 0, 1.454, 0, 0.292284]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList1, times, True)

    effector = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RHand"]
    angleList2 = [1.489, -1.222, 0, 1.342, 0.292284]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList2, times, True)

    effector = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LHand"]
    angleList2 = [1.489, 1.222, 0, -1.342, 0.292284]
    times = 0.6
    motionProxy.angleInterpolation(effector, angleList2, times, True)

    effector = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RHand"]
    times = [[0.5, 1.0]] * 5
    angleList1 = [[1.489, 1.489], [-1.222, -1.222], [0, 0], [0, 1.342], [0.292284, 0.292284]]

    for i in range(3):
        motionProxy.post.angleInterpolation(effector, angleList1, times, True)

    effector = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LHand"]
    times = [[0.5, 1.0]] * 5
    angleList1 = [[1.489, 1.489], [1.222, 1.222], [0, 0], [0, -1.342]]

    for i in range(3):
        motionProxy.angleInterpolation(effector, angleList1, times, True)


def choreography_2():
    effector = "RArm"
    times = 1.0
    angleList1 = [-1.421976089477539062e+00, -4.295620918273925781e-01, 3.527779579162597656e-01,
                  3.378987312316894531e-02, 8.432793617248535156e-02, 2.924000024795532227e-01, ]

    angleList2 = [-1.621479988098144531e+00, -9.571740627288818359e-01, 3.527779579162597656e-01,
                  3.378987312316894531e-02, 8.432793617248535156e-02, 2.924000024795532227e-01]

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

    effector = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll"]
    times = 1.0
    angleList1 = [-1.421976089477539062e+00, 4.295620918273925781e-01, 3.527779579162597656e-01,
                  -3.378987312316894531e-02, 8.432793617248535156e-02, 2.924000024795532227e-01, ]

    angleList2 = [-1.621479988098144531e+00, 9.571740627288818359e-01, 3.527779579162597656e-01,
                  -3.378987312316894531e-02, 8.432793617248535156e-02, 2.924000024795532227e-01]

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

    names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "RHipRoll", "LHipRoll", "LKneePitch",
             "LAnklePitch", "LHipPitch", "RKneePitch", "RAnklePitch", "RHipPitch"]
    angleLists = [[1.45], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]
    times = [[1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0], [1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)


def choreography_3():
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


def makarina():
    timeList = 0.7
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

    motionProxy.angleInterpolation("RArm", angleList1_right, timeList, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList1_left, timeList, isAbsolute)
    motionProxy.angleInterpolation("RArm", angleList2_right, timeList, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList2_left, timeList, isAbsolute)
    motionProxy.angleInterpolation("RArm", angleList4_right, timeList, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList4_left, timeList, isAbsolute)
    motionProxy.angleInterpolation("RArm", angleList3_right, timeList, isAbsolute)
    motionProxy.angleInterpolation("LArm", angleList3_left, timeList, isAbsolute)

    joint_names = ["HeadPitch", "HeadYaw"]

    angleList_head = [[0.5, -0.5, 0.5, -0.5], [0.8, -0.8, 0.8, -0.8]]

    times = [[0.5, 1.5, 2.5, 3.5], [0.5, 1.5, 2.5, 3.5]]
    motionProxy.angleInterpolation(joint_names, angleList_head, times, True)



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
    # sit_test()
    # headMove()
    choreography_1()
    time.sleep(0.5)
    makarina()
    posture.goToPosture("Stand", 0.5)
    sit()
    posture.goToPosture("Stand", 0.5)
    time.sleep(0.5)
    choreography_2()
    choreography_3()

    # ttsProxy.say("Thank you")
    motionProxy.rest()

    time.sleep(5)


if __name__ == "__main__":
    robotIp= "nao6.local"

    if len(sys.argv) <= 1:
        print "Usage python motion_setFootStepDance.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
