import aubio
import numpy as np

class BeatDetector:
    def __init__(self, src, stateMachine):
        self.src = src
        self.stateMachine = stateMachine

    def detect(src)
        self.src = src
        samplerate = 0  # use original source samplerate
        hop_size = 256  # number of frames to read in one block
        total_frames = 0

        while True:
            samples, read = self.src()  # read hop_size new samples from source
            total_frames += read   # increment total number of frames
            if read < hop_size:    # end of file reached
                break

        fmt_string = "read {:d} frames at {:d}Hz from {:s}"
        print(fmt_string.format(total_frames, src.samplerate, src.uri))