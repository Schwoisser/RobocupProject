import argparse
from naoqi import ALProxy
import time
import essentia
from essentia.standard import *
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt
# from playsound import playsound
from thread import start_new_thread
from pydub import AudioSegment
from pydub.playback import play



rate = 44000
tts = audio = record = aup = None 

def main(robot_IP, robot_PORT=9559, song="song"):
	global tts, audio, record, aup 
	# ----------> Connect to robot <----------
	# tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)

	# audio = ALProxy("ALAudioDevice", robot_IP, robot_PORT)
	# record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
	# aup = ALProxy("ALAudioPlayer", robot_IP, robot_PORT)
	# ----------> recording <----------
	# print 'start recording...'
	# record.stopMicrophonesRecording()
	# record.startMicrophonesRecording(record_path, 'wav', 16000, [0,0,1,0])
	# record.stopMicrophonesRecording()
	# print 'record over'
	# ----------> playing the recorded file <----------
	record_path = song;
	# start_new_thread(playsound,(record_path,))
	# fileID = aup.playFile(record_path,0.7, 0)	
	#print(record_path)
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
	audio = AudioSegment.from_wav(record_path)
	time.sleep(2)
	print("play")
	print("if error -> alsa reload")
	start_new_thread(play, (audio,))
	time.sleep(10)


	

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--song", type=str, help="Patho to Song")
	parser.add_argument("--ip", type=str, default="nao5.local", help="Robot ip address")
	parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	args = parser.parse_args()
	#ip = 'nao5.local'
	#port = 9559
	main(args.ip,args.port, args.song)