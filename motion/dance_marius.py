import sys
from naoqi import ALProxy
import numpy as np
import almath
import motion
import time
import keyframes as kf

robotIP = "localhost" #"nao12.local"
port = 49435 #9559
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

kf.macarena(motionProxy)
#motionProxy.angleInterpolation(names, keys, times, True)