import alsaaudio #for listening to the microphone. Has a good non-blocking call
import numpy as np
import sys
import threading
import RPi.GPIO as GPIO #servo control
import time 
GPIO.setmode(GPIO.BCM) #servo setup
import librosa #beat detection
from collections import Counter #to compute the mode of the estimated bpm's
import random

sys.setswitchinterval(0.01) #set switch interval to be 1/100th of a second by default
#initialize the audio capture device
inp = alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE,mode=alsaaudio.PCM_NONBLOCK,device='hw:CARD=Snowball,DEV=0')
inp.setchannels(1) #single channel
sr = 22050 #sampling rate
inp.setrate(sr)
inp.setformat(alsaaudio.PCM_FORMAT_FLOAT_LE) #16 bit little endian samples
inp.setperiodsize(1000) #acquire 1000 samples at a time
sArr = np.array([]) # sound array of stuff being tracked the current time
secondsKept = 3 #number of seconds of audio saved
##    For not continous rotation servos -- speed between .6 ans 2.4 (1.5 = dead center
def setPos(p,speed):
    p.ChangeDutyCycle((speed)/(20)*100)
    p.ChangeFrequency(1/(0.020))

#limits for servos are listed in the follow fashion
#[[[],[],[]],[[],[],[]]] # right left for the first dim, top middle bottom for the second dim,
# backward max, middle, forward max for last dimension
# Other servo arrays are listed similarly, except for the ones that aren't limits there are only the first two dimensions

servoList = [] 
outputs = [[27, 18, 16],[26,17,22]] 
limits = [[[1.2,1.7, 2.6],[0.8,1.3, 2.4],[0.5, 1.6, 2.5]],[[0.7,1.3,2.25],[1.1,1.7,2.7],[0.8,1.5,2.6] ]]#18,17,22, low then middle then high
for j in range(len(outputs)):
    for i in range(len(outputs[0])):
        GPIO.setup(outputs[j][i], GPIO.OUT)
        p = GPIO.PWM(outputs[j][i], 1/(0.020))
        p.start(1.5/(20)*100)
        time.sleep(0.25) #initialize all servos, and sleep a little in between for a cool startup jerk into place dance
        setPos(p,0)
        servoList.append(p)
servoList = [[servoList[0],servoList[1], servoList[2]],[servoList[3],servoList[4], servoList[5]]]


##o = tempo("default", 512, 256, sr)
beatArray = []
beats = []
global bpm
bpm=1
def mic(): # microphone capture thread
    global sArr
    global captureTime #the time that was last captured, used to determine the last beat. 
    while True:
        # Read data from device
        flag,data = inp.read()
        try:
            captureTime = time.time()
            samps = np.frombuffer(data,dtype = np.int16)
            if len(sArr)+len(samps) > sr*secondsKept:
                sArr = np.delete(sArr,np.arange(len(sArr)+len(samps)-sr*secondsKept),0)
            if len(samps) > 0:
                sArr=np.append(sArr,samps)
        except ValueError:
            pass #sometimes, np.frombuffer errors if the number of bytes wasn't evenly divisible, just throw out this data, happens rarely enough anyway
            
        
def beatDetect(): #beat detection thread
    global bpm #current best bpm estimate
    global beats # array of the estimated beat times in sArr
    global sArr #sound array
    global lastCheck #to make sure that you're not doing beat detection too often
    global lastCap #to make sure that you're not doing beat detection too often
    bpm = 0 #init to 0
    lastCheck = time.time()
    bpmEstimates = []
    while True:
        if time.time()-lastCheck > 1:
            lastCheck = time.time()
            lastCap = captureTime
            bpmEstimate,beats = librosa.beat.beat_track(y=sArr, sr=sr, hop_length = 300, units='time') #bpm estimate, beat locations esimate
            if len(bpmEstimates) >= 10:
                del bpmEstimates[0] #keep 10 bpm esimates at a time
            #put the bpm in the 100-200 range
            if bpmEstimate >=200:
                bpmEstimate/=2
            elif bpmEstimate < 100:
                bpmEstimate*=2
            bpmEstimates.append(bpmEstimate)
            bpmDict = Counter(bpmEstimates).most_common()
            #if there is a tie for the most common bpm, use avg of top 2
            if len(bpmDict)>=2 and bpmDict[0][1] == bpmDict[1][1]:
                bpm = (bpmDict[0][0] +bpmDict[1][0])/2
            else:
                bpm = bpmDict[0][0] #otherwise, use the mode of the last 10 bpm esimates
            print('predicted bpm: '+str(bpm))
        else:
            time.sleep(0.02)

def howLong(space): #space is the number of beats tat we are trying to wait
    global sr
    lastBeatTime = lastCap  - (len(sArr)-1000)/sr + beats[-1] #the time the last beat occured, in absolute time
    curTime = time.time()
    timeToWait = curTime - lastBeatTime #the before the current time that the last beat is
    print('orig time to wait is ' + str(timeToWait))
    if timeToWait < 0:
        timeToWait -= space
        freq = 60/bpm # seconds / beat
        addTime1 = (int(-timeToWait/freq)+1)*freq # higher number of beats to wait
        addTime2 = (int(-timeToWait/freq))*freq #lower number of beats to wait
        #wait the number of beats that's closer to space number of beats
        addTime = addTime1 if abs(addTime1 - timeToWait) < abs(addTime1 - timeToWait) else addTime2 
        timeToWait += addTime
    timeToWait += space
    return timeToWait

#take in an array of dance moves, dArr, a number of beats between moves, space, and do this iter number of times
def danceFromArray(dArr, space = 2, iter = 1): #of shape n, 2, 3 and has values 0,1,2 for low middle high servos
    space *= 60/bpm #convert space number of beats into an amount of time
    for n in range(len(dArr)):
        dArr[n][0][2] = 2 - dArr[n][0][2] #flip one of the servos, one of the servos was placed in upside down
    for _ in range(iter):
        for n in range(len(dArr)):
            timeToWait = howLong(space)
            if abs(timeToWait - space) < 0.05 and timeToWait > 0:
                print('time to wait is ' + str(timeToWait)) # if the adjustment is close to the time we were supposed to wait, wait that long
            else:
                timeToWait = space #otherwise, just wait space number of beats
                print('time to wait is the regular ' + str(space))
            time.sleep(timeToWait/2) #split the wait time between this wait and the next
            for j in range(2): #for all servos
                for i in range(3):
                    if dArr[n][j][i] <= 2 and dArr[n][j][i] >1: #if we are moving between limits, take a weighted average
                        val = limits[j][i][2]*(dArr[n][j][i]-1) + limits[j][i][1]*(2-dArr[n][j][i])
                    else:
                        val = limits[j][i][1]*(dArr[n][j][i]) + limits[j][i][0]*(1-dArr[n][j][i])
                    setPos(servoList[j][i],val) #set the servo position
            time.sleep(timeToWait/2) #sleep for half this time,this way we can stop and the motions look less jerky
            for j in range(2):
                for i in range(3):
                    setPos(servoList[j][i],0)

# for the shoulder rotation servo, 0 is oriented upward, 2 is downward
# for the armpit hinge servo, 0 is full extend on one side, 2 is the close to full extend on the other
# for elbow servo, 2 is full extension, 0 is closed
def danceList(which):
    global bpm
    if which == 0: #move everythng from max to the middle, one time
        danceFromArray([[[2,2,2],[2,2,2]],[[1,1,1],[1,1,1]]],iter = 4)
    if which == 1: # "egyption", extend arms outward and inward in rhythm
        danceFromArray([[[1,2,2],[1,2,0]],[[1.75,1.25,2],[1.75,1.25,0]]], iter = 2)
        danceFromArray([[[1,2,0],[1,2,2]],[[1.75,1.25,0],[1.75,1.25,2]]], iter = 2)
    if which == 2: # 1 arm robot
        danceFromArray([[[2,2,0],[1.4,1,2]],[[2,2,0],[0.5,1,2]]], iter = 4)
    if which == 3: # 2 arm robot
        danceFromArray([[[0,1,2],[2,1,2]],[[2,1,2],[0,1,2]]], iter = 4)
    if which == 4: # "progressive wave upward"
        dArr = []
        for i in range(6):
            dArr.append([[0,1,2-i/5*2],[2,1,2-i/5*2]])
            dArr.append([[2,1,2-i/5*2],[0,1,2-i/5*2]])
        for i in range(6):
            dArr.append([[0,1,i/5*2],[2,1,i/5*2]])
            dArr.append([[2,1,i/5*2],[0,1,i/5*2]])
        danceFromArray(dArr, space = 1)
    if which == 5: # the waaaaaaaaaaaaaaaaaaaaave
        dArr  = []
        each = 3
        for i in range(each+1):
            dArr.append([[2,1,2],[2,1,2]])
        #leftward wave
        for i in range(each+1):
            dArr.append([[2-i*1.5/each,1+i/each/2,2],[2,1,2]])
        for i in range(each+1):
            dArr.append([[0.5+i*1.5/each,1.5-i/each/2,2],[2-i*1.5/each,1+i/each/2,2]])
        for i in range(each+1):
            dArr.append([[2,1,2],[0.5+i*1.5/each,1.5-i/each/2,2]])
        for i in range(each+1):
            dArr.append([[2,1,2],[2,1,2]])
        #rightward wave
        for i in range(each+1):
            dArr.append([[2,1,2],[2-i*1.5/each,1+i/each/2,2]])
        for i in range(each+1):
            dArr.append([[2-i*1.5/each,1+i/each/2,2],[0.5+i*1.5/each,1.5-i/each/2,2]])
        for i in range(each+1):
            dArr.append([[0.5+i*1.5/each,1.5-i/each/2,2],[2,1,2]])
        danceFromArray(dArr, space = 1/4)
    if which == 6: #whip+naenae
        for _ in range(2):
            dArr = []
            #the whip
            dArr.append([[2,0,2],[2,0,2]]) #both arms down
            dArr.append([[2,0,2],[0,2,0]]) #scrunch right arm
            dArr.append([[2,0,2],[1.5,0,1]]) #whip right arm
            danceFromArray(dArr, space = 2)
            #now, the naenae
            dArr=[]
            dArr.append([[2,0,2],[2,0,2]]) #both arms down
            dArr.append([[2,2,2],[2,0,2]]) #left arm up
            dArr.append([[2,1.5,2],[2,0,2]]) #wave left arm
            dArr.append([[2,2,2],[2,0,2]]) #wave left arm
            dArr.append([[2,1.5,2],[2,0,2]]) #wave left arm
            dArr.append([[2,2,2],[2,0,2]]) #left arm up
            dArr.append([[2,1.5,2],[2,0,2]]) #wave left arm
            dArr.append([[2,2,2],[2,0,2]]) #wave left arm
            dArr.append([[2,1.5,2],[2,0,2]]) #wave left arm
            dArr.append([[2,2,2],[2,0,2]]) #wave left arm
            danceFromArray(dArr, space = 1)
    if which == 7: #cat daddy
        dArr = []
        dArr.append([[0,0,1],[0,0,1]])
        dArr.append([[0.2,0.3,0.7],[0.2,0.3,0.7]])
        dArr.append([[0.5,0.5,0.8],[0.5,0.5,0.8]])
        dArr.append([[0.7,0.25,1.1],[0.7,0.25,1.1]])
        dArr.append([[1.25,0,1.5],[1.25,0,1.5]])
        dArr.append([[1.5,0,1.75],[1.5,0,1.75]])
        dArr.append([[1,0,2],[1,0,2]])
        dArr.append([[0.5,0,1.5],[0.5,0,1.5]]) # 8 moves
##        newDarr = np.zeros((32,2,3))
##        npdarr = np.array(dArr)
        danceFromArray(dArr, space = 1/4, iter = 4)
def dance():
    #calls a specific move
    global beats
    global bpm
    while True:
        try:
            #do a move at the next beat, if we have enough beat info
            if len(beats) > 2 and bpm !=1:
##                danceList(random.randint(0,6))
                danceList(1) #cycle through all of our moves for demo
                danceList(2)
                danceList(4)
                danceList(5)
                danceList(6)
                danceList(7)
##                danceList(6)
            else: #wait for enough beats
                time.sleep(0.01)
        except NameError: # if beats isn't defined yet
            pass


#start up all the threads.
bThread = threading.Thread(target=beatDetect)
micThread = threading.Thread(target=mic)
dThread = threading.Thread(target=dance)

bThread.start()
micThread.start()
dThread.start()