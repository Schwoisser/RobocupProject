import essentia
from essentia.standard import *
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt

loader = essentia.standard.MonoLoader(filename='./ModernPop_Mini_SP/7.wav')
#rate=8000
rate=44100
#rate=11025 
audio = loader()

print(audio)

#plt.rcParams['figure.figsize'] = (15, 6) # set plot sizes to something larger than default

#plot(audio[1*44100:2*44100])
#plt.title("This is how the 2nd second of this audio looks like:")
#show() # unnecessary if you started "ipython --pylab"

# Compute beat positions and BPM
rhythm_extractor = RhythmExtractor2013(method="multifeature")
bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
danceability = Danceability(sampleRate=rate)
danceab, dance = danceability(audio)
print("Danceability",dance)
print("Danceability",danceab)
print("BPM:", bpm)
#print("Beat positions (sec.):", beats)
#print("Beat estimation confidence:", beats_confidence)

# Mark beat positions on the audio and write it to a file
# Let's use beeps instead of white noise to mark them, as it's more distinctive
#marker = AudioOnsetsMarker(onsets=beats, type='beep')
#marked_audio = marker(audio)
#MonoWriter(filename='./organfinale.wav')(marked_audio)