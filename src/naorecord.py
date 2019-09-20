import argparse
from naoqi import ALProxy
import time as time
import essentia #beat detection
from essentia.standard import * #beat detection
import threading
from thread import start_new_thread
from pydub import AudioSegment #musicplayer 
from pydub.playback import play #musicplayer
import keyframes as kf #python code with the keyframes for the moviment
from choreographies import choreography 


def beatDetection(song="song"):
	record_path = song;
	loader = essentia.standard.MonoLoader(filename=record_path)
	audio = loader()
	rate = 44000 # sampling rate
	# Compute beat positions and BPM, Danceability, Intensity and Duration of the music
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
	return bpm, intensity, beats, duration, danceab
	

def musicPlayer(song="song"):
	#load a music file and play
	record_path = song
	music = AudioSegment.from_mp3(record_path)
	print("play")
	print("if error -> alsa reload")
	start_new_thread(play, (music,))


	
def doDance(bpm, intensity, duration, beats, song, ip, port):
	robotIP = ip
	port = port
	motionProxy = ALProxy("ALMotion", robotIP, port)
	posture = ALProxy("ALRobotPosture", robotIP, port)
	ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	start = time.time()
	posture.goToPosture("Stand", 1.0)
	#posture.goToPosture("StandInit",1.0)
	if (duration <25.0):
		return ttsProxy.say("Music is not long enough, please choose another music.")
	if (bpm<69):
		return ttsProxy.say("Music is too slow, please choose another music")
	if (bpm>170):
		return ttsProxy.say("This music is too fast for a robot, please choose another one")
	musicThread = threading.Thread(target=musicPlayer(song))
	time.sleep(2)
	musicThread.start()
	while (start + duration) > time.time():
		choreography(motionProxy, bpm, intensity, start, duration, beats, posture)
	posture.goToPosture("Rest", 1.0)
			

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--song", type=str, help="Patho to Song")
	parser.add_argument("--ip", type=str, help="Robot IP")
	parser.add_argument("--port", type=str, help="Robot Port")
	args = parser.parse_args()
	bpm, intensity, beats, duration, danceab = beatDetection(args.song)

	doDance(bpm, intensity, duration,beats, args.song, args.ip, args.port)
