import argparse
from naoqi import ALProxy
import time as time
import essentia
from essentia.standard import *
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt
import threading
from thread import start_new_thread
from pydub import AudioSegment
from pydub.playback import play
import keyframes as kf
from choreographies import choreography
import sys
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
	#print("Beats:", beats)
	print("Intensity(relaxed (-1), moderate (0), or aggressive (1)): ", intensity)
	print("Duration", duration)
	print("beats : ", beats)
	return bpm, intensity, beats, duration, danceab
	

def musicPlayer(song="song"):
	record_path = song
	music = AudioSegment.from_mp3(record_path)
	#time.sleep(2)
	print("play")
	print("if error -> alsa reload")
	start_new_thread(play, (music,))




	
def doDance(bpm, intensity, duration, beats):
    #do a move at the next beat, if we have enough beat info
	#Dance 1 with intensity -1,0 or 1 
	robotIP = "nao34.local" #"nao12.local"
	port = 9559 #9559
	motionProxy = ALProxy("ALMotion", robotIP, port)
	posture = ALProxy("ALRobotPosture", robotIP, port)
	ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	start = time.time()
	posture.goToPosture("StandInit",1.0)
	time.sleep(2)
	if (duration <25.0):
		return ttsProxy.say("Music is not long enough, please choose another music.")
	if (bpm<70):
		return ttsProxy.say("Music is too slow, please choose another music")
	if (bpm>170):
		return ttsProxy.say("This music is too fast for a robot, please choose another one")
	while (start + duration) > time.time():
		choreography(motionProxy, bpm, intensity, start, duration, beats)
			

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--song", type=str, help="Patho to Song")
	#parser.add_argument("--ip", type=str, default="nao34.local", help="Robot ip address")
	#parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	args = parser.parse_args()
	bpm, intensity, beats, duration, danceab = beatDetection(args.song)
	musicThread = threading.Thread(target=musicPlayer(args.song))
	musicThread.start()
	doDance(bpm, intensity, duration,beats)
