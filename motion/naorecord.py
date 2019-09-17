import argparse
from naoqi import ALProxy
import time as time
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




def beatDetection(song="song"):
	record_path = song;
	loader = essentia.standard.MonoLoader(filename=record_path)
	audio = loader()
	rate = 44000
	# Compute beat positions and BPM and Danceability
	rhythm_extractor = RhythmExtractor2013(method="multifeature")
	bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
	danceability = Danceability(sampleRate=rate)
	danceab, dance = danceability(audio)
	intensity = Intensity(sampleRate=rate)
	intensity = intensity(audio)
	duration = Duration(sampleRate=rate)
	duration = duration(audio)
	print("Danceability",danceab)
	print("BPM:", bpm)
	print("Beats:", beats)
	print("Intensity(relaxed (-1), moderate (0), or aggressive (1)): ", intensity)
	print("Duration", duration)
	return bpm, intensity, beats, duration
	

def musicPlayer(song="song"):
	record_path = song;
	music = AudioSegment.from_wav(record_path)
	#time.sleep(2)
	print("play")
	print("if error -> alsa reload")
	start_new_thread(play, (music,))
	
	
def doDance(bpm, intensity, duration):
    #do a move at the next beat, if we have enough beat info
	#Dance 1 with intensity -1,0 or 1 
	robotIP = "nao34.local" #"nao12.local"
	port = 9559 #9559
	motionProxy = ALProxy("ALMotion", robotIP, port)
	posture = ALProxy("ALRobotPosture", robotIP, port)
	ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	now = time.time()
	while (now + duration) > time.time():
			if (bpm >= 80 and bpm <= 120 and intensity == 0):
				kf.dance4(motionProxy,((60.0)/bpm),1)
				kf.dance1(motionProxy)
				kf.dance5(motionProxy,((60.0)/bpm),1)
				kf.dance7(motionProxy,((60.0)/bpm),1)
			elif (bpm >=80 and bpm <=120 and intensity == -1):
				kf.dance4(motionProxy,((60.0)/bpm),1)
				kf.dance1(motionProxy)
				kf.dance5(motionProxy,((60.0)/bpm),1)
				kf.dance7(motionProxy,((60.0)/bpm),1)
			elif bpm >= 80 and bpm <= 120 and intensity == 1:
				kf.dance4(motionProxy,((60.0)/bpm),1)
				kf.dance1(motionProxy)
				kf.dance5(motionProxy,((60.0)/bpm),1)
				kf.dance7(motionProxy,((60.0)/bpm),1)
			#Dance 2 
			elif bpm>120 and bpm <=150 and intensity == 1:
				kf.macarena(motionProxy,(60.0/(bpm*1.2)),1)
				kf.dance5(motionProxy,(60.0/(bpm*1.2)),1)
				kf.dance6(motionProxy,(60.0/(bpm*1.2)),1)
		#       kf.dance4(motionProxy,(60.0/(bpm*1.5)),1)
			elif bpm>120 and bpm <=150 and intensity == 0:
				kf.macarena(motionProxy,(60.0/(bpm)),1)
				kf.dance5(motionProxy,(60.0/(bpm)),1)
				kf.dance6(motionProxy,(60.0/(bpm)),1)
		#       kf.dance4(motionProxy,(60.0/(bpm*1.5)),1)
			elif bpm>120 and bpm <=150 and intensity ==-1:
				kf.dance4(motionProxy,((60.0)*1.5/bpm),1)
				#kf.dance1(motionProxy)
				#kf.up_and_down(motionProxy)
				kf.nod(motionProxy,0.5)
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
	parser.add_argument("--ip", type=str, default="nao34.local", help="Robot ip address")
	parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	args = parser.parse_args()
	bpm, intensity, beats, duration = beatDetection(args.song)
	#musicThread = threading.Thread(target=musicPlayer(args.song))
	#musicThread.start()
	#doDance(bpm, intensity, duration)