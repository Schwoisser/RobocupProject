import argparse
from naoqi import ALProxy
import time
import essentia
from essentia.standard import *
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt



tts = audio = record = aup = None 

def main(robot_IP, robot_PORT=9559):
	global tts, audio, record, aup 
	# ----------> Connect to robot <----------
	tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
	audio = ALProxy("ALAudioDevice", robot_IP, robot_PORT)
	record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
	aup = ALProxy("ALAudioPlayer", robot_IP, robot_PORT)
	# ----------> recording <----------
	print 'start recording...'
	record_path = "/home/nao/out1.wav";
	record.stopMicrophonesRecording()
	record.startMicrophonesRecording(record_path, 'wav', 16000, [0,0,1,0])
	time.sleep(10)
	record.stopMicrophonesRecording()
	print 'record over'
	# ----------> playing the recorded file <----------
	fileID = aup.loadFile(record_path)
	time.sleep(5)
	print aup.getFileLength(fileID)
	aup.play(fileID,1,0)
	##print(record_path)
	#loader = essentia.standard.MonoLoader(filename=record)
	#audio = loader()
	#
	## Compute beat positions and BPM and Danceability
	#rhythm_extractor = RhythmExtractor2013(method="multifeature")
	#bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
	#danceability = Danceability(sampleRate=rate)
	#danceab, dance = danceability(audio)
	#print("Danceability",danceab)
	#print("BPM:", bpm)


	

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao5.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
	#ip = 'nao5.local'
	#port = 9559
    main(args.ip,args.port)