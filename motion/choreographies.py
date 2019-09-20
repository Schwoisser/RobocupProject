import keyframes as kf
import time as time


def wait_for_sync(start, duration, beats):
    now = time.time()
    time_past = now - start
    for i in range(len(beats)):
        # print("beat " + str(i) + " " + str(beats[i]))
        if (i == 0):
            if (time_past < beats[0]):
                wait_time = beats[0] - time_past
                time.sleep(wait_time)
                return float(beats[0])
        elif (time_past > beats[i - 1] and time_past < beats[i]):
            wait_time = beats[i] - time_past
            time.sleep(wait_time)
            return float(beats[i] - beats[i - 1])
    return 0.0


#
#
# macarena
# dance7
# nod

# low bpm
# dance5 intensity maybe > -1
# macarena
# stand + dance7
# stand + dab
# posture.goToPosture("Stand", 1.0)

# med bpm
# dance4
# stand + dance7
# stand + dab

# high bpm
# dance4
# nod
# stand + dab

# Test
# arm_yeahboth
# arm_yeah
# arm_snap
# arm_walk
# arm_leg_both
# dab
# up_and_down

def low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture):
    # print("low bpm")
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.dance5(motionProxy, current_beat_duration * 2, current_beat_duration * 2)
    # macarena
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.macarena(motionProxy, current_beat_duration, current_beat_duration * 2)
    kf.macarena(motionProxy, current_beat_duration, current_beat_duration * 2)

    # stand + dance7
    posture.goToPosture("Stand", 1.0)
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.dance7(motionProxy, current_beat_duration * 2, current_beat_duration * 2)
    # stand + dab
    posture.goToPosture("Stand", 1.0)
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.dab(motionProxy, current_beat_duration, current_beat_duration * 2)
    posture.goToPosture("Stand", 1.0)


def low_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats, posture):
    low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)


def low_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats, posture):
    low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)


# med bpm
# dance4
# stand + dance7
# stand + dab

def medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture):
    # dance 4
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.dance4(motionProxy, current_beat_duration, current_beat_duration * 2)

    # stand + dance7
    posture.goToPosture("Stand", 1.0)
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.dance7(motionProxy, current_beat_duration * 2, current_beat_duration * 2)
    # stand + dab
    posture.goToPosture("Stand", 1.0)
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.dab(motionProxy, current_beat_duration, current_beat_duration * 2)


def medium_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats, posture):
    medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)


def medium_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats, posture):
    medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)


# high bpm
# dance4
# nod
# stand + dab

def high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture):
    # dance 4
    current_beat_duration = wait_for_sync(start, duration, beats)
    # kf.dance4(motionProxy, current_beat_duration * 2, current_beat_duration * 2)
    # nod
    # posture.goToPosture("Stand", current_beat_duration * 2)
    # current_beat_duration = wait_for_sync(start, duration, beats)
    # kf.nod(motionProxy, current_beat_duration, current_beat_duration * 2, 5)

    # stand + dab
    posture.goToPosture("StandInit", current_beat_duration * 2)
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.nod(motionProxy, current_beat_duration, current_beat_duration * 2, 5)
    kf.dab(motionProxy, current_beat_duration * 2, current_beat_duration * 2)
    #standInit + dance1 + arm_leg_both
    posture.goToPosture("StandInit", current_beat_duration*2)
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.dance1(motionProxy, current_beat_duration, current_beat_duration)
    current_beat_duration = wait_for_sync(start, duration, beats)
    kf.arm_leg_both(motionProxy,current_beat_duration, current_beat_duration * 2)


def high_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats, posture):
    high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)


def high_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats, posture):
    high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)


def choreography(motionProxy, bpm, intensity, start, duration, beats, posture):
    if (bpm >= 65 and bpm <= 110 and intensity == 0):
        low_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats, posture)
    elif (bpm >= 65 and bpm <= 110 and intensity == -1):
        low_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)
    elif bpm >= 65 and bpm <= 110 and intensity == 1:
        low_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats, posture)
    elif bpm > 110 and bpm <= 140 and intensity == -1:
        medium_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)
    elif bpm > 110 and bpm <= 140 and intensity == 0:
        medium_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats, posture)
    elif bpm > 110 and bpm <= 140 and intensity == 1:
        medium_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats, posture)
    # Dance 3
    elif bpm > 140 and bpm <= 170 and intensity == -1:
        high_bpm_relax(motionProxy, bpm, intensity, start, duration, beats, posture)
    elif bpm > 140 and bpm <= 170 and intensity == 0:
        high_bpm_neutral(motionProxy, bpm, intensity, start, duration, beats, posture)
    elif bpm > 140 and bpm <= 170 and intensity == 1:
        high_bpm_aggressive(motionProxy, bpm, intensity, start, duration, beats, posture)
