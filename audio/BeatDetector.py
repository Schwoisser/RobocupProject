from __future__ import print_function
import numpy as np
import pyaudio
import wave
import sys
import librosa
import IPython.display as ipd 

CHUNK = 1024

wf = wave.open('c:\\projects\\RobocupProject\\audio\\test.wav','rb')
p = pyaudio.PyAudio()
tempo=[]

data = wf.readframes(CHUNK)
y, sr = librosa.load('c:\\projects\\RobocupProject\\audio\\test.wav')
ipd.Audio(y, rate=sr)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr,hop_length=300,units='time')
clicks = librosa.clicks(beat_frames, sr=sr, length=len(y))
ipd.Audio(y + clicks, rate=sr)
    
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))


    # 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    


stream.stop_stream()
stream.close()

p.terminate()

