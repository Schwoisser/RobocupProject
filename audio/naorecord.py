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



rate = 44000

def BeatDetection(song="song"):
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
	time.sleep(2)
	print("play")
	print("if error -> alsa reload")
	start_new_thread(play, (music,))
	time.sleep(10)
	
def doDance():
	global intensity
	global beats
    global bpm
    while True:
        try:
            #do a move at the next beat, if we have enough beat info
            if len(beats) > 2 and bpm !=1:
                choreography_1() #cycle through all of our moves for demo
                choreography_2()
                choreography_3()
				makarina()
                dance4()
                dance5()
                dance6()
            else: #wait for enough beats
                time.sleep(0.01)
        except NameError: # if beats isn't defined yet
            pass



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--song", type=str, help="Patho to Song")
	#parser.add_argument("--ip", type=str, default="nao5.local", help="Robot ip address")
	#parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	args = parser.parse_args()
	#start up all the threads.
	bThread = threading.Thread(target=BeatDetection(args.song))
	musThread = threading.Thread(target=MusicPlayer(args.song))
	musThread.start()
	bThread.start()