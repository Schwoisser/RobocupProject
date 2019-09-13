import argparse
from naoqi import ALProxy
import time
import essentia
from essentia.standard import *
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt
# from playsound import playsound
import threading
from thread import start_new_thread
from pydub import AudioSegment
from pydub.playback import play
import keyframes as kf
import sys
from naoqi import ALProxy
import numpy as np
import almath
import motion




rate = 44000
robotIP = "localhost" #"nao12.local"
port = 46335 #9559
motionProxy = ALProxy("ALMotion", robotIP, port)
posture = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)



def BeatDetection(song="song"):
	global bpm
	global intensity
	global beats	
	record_path = song;
	loader = essentia.standard.MonoLoader(filename=record_path)
	audio = loader()
	# Compute beat positions and BPM and Danceability
	rhythm_extractor = RhythmExtractor2013(method="multifeature")
	bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
	danceability = Danceability(sampleRate=rate)
	danceab, dance = danceability(audio)
	intensity = Intensity(sampleRate=rate)
	intensity = intensity(audio)
	print("Danceability",danceab)
	print("BPM:", bpm)
	print("Intensity(relaxed (-1), moderate (0), or aggressive (1)): ", intensity)
	

def MusicPlayer(song="song"):
	record_path = song;
	music = AudioSegment.from_wav(record_path)
	#time.sleep(2)
	print("play")
	print("if error -> alsa reload")
	start_new_thread(play, (music,))
	
	
def doDance():
	global intensity
    	global bpm
            	#do a move at the next beat, if we have enough beat info
	#Dance 1 with intensity -1,0 or 1        
	if bpm >=80 and bpm <=120 and intensity ==0:
                kf.dance4(motionProxy,((60.0)/bpm),1)
		kf.macarena(motionProxy,((60.0)/bpm),1)
                kf.dance6(motionProxy,((60.0)/bpm),1)
                kf.dance4(motionProxy,((60.0)/bpm),1)
	elif bpm >=80 and bpm <=120 and intensity ==1:
                kf.dance4(motionProxy,((60.0)/bpm*1.5),1)
		kf.macarena(motionProxy,((60.0)/bpm*1.5),1)
                kf.dance6(motionProxy,((60.0)/bpm*1.5),1)
                kf.dance4(motionProxy,((60.0)/bpm*1.5),1)
	elif bpm >=80 and bpm <=120 and intensity ==-1:
                kf.dance4(motionProxy,((60.0*1.5)/bpm),1)
		kf.macarena(motionProxy,((60.0*1.5)/bpm),1)
                kf.dance6(motionProxy,((60.0*1.5)/bpm),1)
                kf.dance4(motionProxy,((60.0*1.5)/bpm),1)
	#Dance 2 with 
        elif bpm>120 and bpm <=150 and intensity ==1:
		kf.macarena(motionProxy,(60.0/(bpm*1.2)),1)
                kf.dance5(motionProxy,(60.0/(bpm*1.2)),1)
                kf.dance6(motionProxy,(60.0/(bpm*1.2)),1)
#                kf.dance4(motionProxy,(60.0/(bpm*1.5)),1)
	elif bpm>120 and bpm <=150 and intensity ==0:
		kf.macarena(motionProxy,(60.0/(bpm)),1)
                kf.dance5(motionProxy,(60.0/(bpm)),1)
                kf.dance6(motionProxy,(60.0/(bpm)),1)
#                kf.dance4(motionProxy,(60.0/(bpm*1.5)),1)
	elif bpm>120 and bpm <=150 and intensity ==-1:
		kf.macarena(motionProxy,(60.0*1.2/(bpm)),1)
                kf.dance5(motionProxy,(60.0*1.2/(bpm)),1)
                kf.dance6(motionProxy,(60.0*1.2/(bpm)),1)
#                kf.dance4(motionProxy,(60.0/(bpm*1.5)),1)
	#Dance 3
	elif bpm>150 and bpm<=180 and intensity ==-1:
                kf.dance5(motionProxy,((60.0*1.1)/bpm),1)
                kf.dance4(motionProxy,((60.0*1.1)/bpm),1)
		kf.macarena(motionProxy,((60.0*1.1)/bpm),1)
                kf.dance6(motionProxy,((60.0*1.1)/bpm),1)
	elif bpm>150 and bpm<=180 and intensity ==0:
                kf.dance5(motionProxy,((60.0)/bpm),1)
                kf.dance4(motionProxy,((60.0)/bpm),1)
		kf.macarena(motionProxy,((60.0)/bpm),1)
                kf.dance6(motionProxy,((60.0)/bpm),1)
	elif bpm>150 and bpm<=180 and intensity ==-1:
                kf.dance5(motionProxy,((60.0)/bpm*1.1),1)
                kf.dance4(motionProxy,((60.0)/bpm*1.1),1)
		kf.macarena(motionProxy,((60.0)/bpm*1.1),1)
                kf.dance6(motionProxy,((60.0)/bpm*1.1),1)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--song", type=str, help="Patho to Song")
	#parser.add_argument("--ip", type=str, default="nao5.local", help="Robot ip address")
	#parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	args = parser.parse_args()
	#start up all the threads
	#time.sleep(1)
	#ttsProxy.say("3")
	#time.sleep(0.5)
	#ttsProxy.say("2")
	#time.sleep(0.5)
	#ttsProxy.say("1")
	#time.sleep(0.5)
	#ttsProxy.say("Go!")
	bThread = threading.Thread(target=BeatDetection(args.song))
	musThread = threading.Thread(target=MusicPlayer(args.song))
	DThread = threading.Thread(target=doDance())
	bThread.start()
	DThread.start()
	musThread.start()
