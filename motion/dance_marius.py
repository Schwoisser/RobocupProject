import sys
from naoqi import ALProxy
import numpy as np
import almath
import motion
import time
import keyframes as kf

robotIP = "nao34.local"
port = 9559
motionProxy = ALProxy("ALMotion", robotIP, port)
posture = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)

time.sleep(1)
ttsProxy.say("3")
time.sleep(0.5)
ttsProxy.say("2")
time.sleep(0.5)
ttsProxy.say("1")
time.sleep(0.5)
ttsProxy.say("Go!")
posture.goToPosture("Stand", 1.0)
time.sleep((2))
# kf.dance3(motionProxy) # begin with Stand
# kf.dance1(motionProxy) # bein with Stand and endposition ist stand
# kf.macarena(motionProxy)
# kf.up_and_down(motionProxy)
kf.dance5(motionProxy, 0.8) # endposition and beginposition ist Stand
# kf.dance6(motionProxy, 0.7)  # begin with Stand and endposition ist Stand
# posture.goToPosture("Stand", 1.0)
# kf.dance7(motionProxy)  # begin with Stand posture
# posture.goToPosture("StandInit", 1.0)
# time.sleep(1)
# kf.dance_test(motionProxy, 0.5) # begin with standInit
#motionProxy.angleInterpolation(names, keys, times, True)
