import sys
from naoqi import ALProxy
import numpy as np
import almath
import motion
import time
import keyframes as kf

robotIP = "localhost"
port = 40531
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
# kf.dance4(motionProxy)
kf.dance1(motionProxy)
# kf.macarena(motionProxy)
# kf.up_and_down(motionProxy)
# kf.dance5(motionProxy)
# kf.dance6(motionProxy)
# kf.dance7(motionProxy)
#motionProxy.angleInterpolation(names, keys, times, True)
