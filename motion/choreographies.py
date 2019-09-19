import keyframes as kf
import time as time

def wait_for_sync(start, duration, beats):
    now = time.time()
    time_past = now - start
    for i in range(len(beats)):
        # print("beat " + str(i) + " " + str(beats[i]))
        if(i == 0):
            if(time_past < beats[0]):
                wait_time = beats[0] - time_past
                time.sleep(wait_time)
                return beats[0]
        elif(time_past > beats[i - 1] and time_past < beats[i]):
            wait_time = beats[i] - time_past
            print(wait_time)
            time.sleep(wait_time)
            return beats[i] - beats[i - 1]
    return 0


def low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats):
    # wait_for_sync(start, duration, beats)
    # kf.dance8(motionProxy, ((60.0)/bpm), 1)
    # wait_for_sync(start, duration, beats)
    # kf.dance1(motionProxy)
    # wait_for_sync(start, duration, beats)
    # kf.dance5(motionProxy, ((60.0)/bpm), 1)
    #wait_for_sync(start, duration, beats)
    #kf.dance7(motionProxy, ((60.0)/bpm), 1)
    # wait_for_sync(start, duration, beats)
    # kf.macarena(motionProxy, ((60.0)/bpm), 1)
    wait_for_sync(start, duration, beats)
    kf.dance_test(motionProxy, ((60.0)/bpm*1.1), 1)

def low_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats):
	low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)

def low_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats):
    low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)

def medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats):
    wait_for_sync(start, duration, beats)
    kf.dance4(motionProxy, ((60.0)/bpm), 1)
    time.sleep(0.5)
    wait_for_sync(start, duration, beats)
    kf.dance1(motionProxy)
    time.sleep(0.5)
    #kf.up_and_down(motionProxy)
    wait_for_sync(start, duration, beats)
    kf.nod(motionProxy, 0.4)
    time.sleep(0.5)

def medium_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats):
    medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)

def medium_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats):
    medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)

def high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats):
    wait_for_sync(start, duration, beats)
    kf.dance6(motionProxy,((60.0)/bpm*1.1),1)
    wait_for_sync(start, duration, beats)
    kf.dance5(motionProxy,((60.0)/bpm*1.1),1)
    wait_for_sync(start, duration, beats)
    kf.dance4(motionProxy,((60.0)/bpm*1.1),1)
    wait_for_sync(start, duration, beats)
    kf.macarena(motionProxy,((60.0)/bpm*1.1),1)

def high_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats):
    high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)
    
def high_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats):
    high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)

def choreography(motionProxy, bpm, intensity, start, duration, beats):
    if (bpm >= 69 and bpm <= 120 and intensity == 0):
        low_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats)
    elif (bpm >=69 and bpm <=120 and intensity == -1):
    	low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)
    elif bpm >= 69 and bpm <= 120 and intensity == 1:
        low_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats)
    elif bpm>120 and bpm <=150 and intensity == -1:
        medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)
    elif bpm>120 and bpm <=150 and intensity == 0:
        medium_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats)
    elif bpm>120 and bpm <=150 and intensity == 1:
        medium_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats)
	#Dance 3
    elif bpm>150 and bpm<=170 and intensity ==-1:
        high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats)
    elif bpm>150 and bpm<=170 and intensity == 0:
        high_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats)
    elif bpm>150 and bpm<=170 and intensity == 1:
        high_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats)
