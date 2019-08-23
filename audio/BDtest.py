import numpy as np
import sys
import threading
import time 
import librosa #beat detection
from collections import Counter #to compute the mode of the estimated bpm's
import random
import wave
import pyaudio
import datetime
import naoqi


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 10
filename = "output.wav"
p = pyaudio.PyAudio()  # Create an interface to PortAudio
#initialize the audio capture device
print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = np.array([])  # Initialize array to store frames

# Store data in chunks for 10 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    samps = np.frombuffer(data,dtype = np.int16)
    frames=np.append(frames,samps)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(map(str,frames)))
wf.close()
print('Finished recording')
print datetime.datetime.now()
#y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=frames, sr=fs,hop_length=300,units='time')
print datetime.datetime.now()
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
