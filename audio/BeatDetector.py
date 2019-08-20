#import aubio

import numpy as np

# first, we need to import our essentia module. It is aptly named 'essentia'!
import essentia

# as there are 2 operating modes in essentia which have the same algorithms,
# these latter are dispatched into 2 submodules:
#import essentia.standard
#import essentia.streaming

# we start by instantiating the audio loader:
loader = essentia.standard.MonoLoader(filename='samples/dubstep.wav')

# and then we actually perform the loading:
audio = loader()

# This is how the audio we want to process sounds like
import IPython
IPython.display.Audio('samples/dubstep.wav')

