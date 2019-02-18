from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import csv
import random


###### Log writing #######
def logwrite(values,filename,**new_directory):
    # Appends a new row 'values' to filename_log.csv
    # Optional (*directory): write log in a non-current path by adding newPath = 'desired path'
    # File will be created in pwd unless 'filename' contains path info or newPath is called
    if 'newPath' in new_directory:
        print 'new path selected: ' + new_directory['newPath']
        filename = os.path.join(new_directory['newPath'],filename)
        with open(filename+'_log.csv','a') as logfile:
            logwriter = csv.writer(logfile, delimiter=',')
            logwriter.writerow(values)
            logfile.close()


##### new function to pick options only
def pickvalues():
    a1 = 5 
    a2 = 15 
    w = 60 # width of each range
    # derived params
    b1 = a1 + w 
    b2 = a2 + w 
    #pick options 
    optionA = random.choice(range(a1, b1, 1))
    optionB = random.choice(range(a2, b2, 1))
    #end values 
    endA = random.choice(range(a1, b1, 1))
    endB = random.choice(range(a2, b2, 1))
    optionValues = {'optionA':optionA, 'optionB':optionB, 'endA':endA, 'endB':endB}
    return optionValues

###### Pick to play or not routine ######
def pickoptions(win):
    pickoptionsClock = core.Clock()
    response = 0
    RT = 0
    choice_1 = 0 #choice_1 refers to the pick or play routine
    ### start routine "pick options ###
    core.wait(1)
    win.flip()
    #record responses
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: #pick play
            response = 1
            RT = pickoptionsClock.getTime()
            win.flip()
        elif '2' in theseKeys: #pick pick
            response = 2
            RT = pickoptionsClock.getTime()
            win.flip()
        else: #did not pick
            response = 3
            RT = pickoptionsClock.getTime()
            win.flip()
    if response == 0: 
        response = 3
        RT = pickoptionsClock.getTime()
    choice_1 ={'play':response == 1, 'pick':response == 2, 'miss': response ==3}
    return choice_1

#### precommitment (pick) routine ####
def precomm_pick(win):
    pickClock = core.Clock()
    response = 0
    RT = 0
    choice_2 = 0 #choice_2 refers to the precommitment routine 
    #record responses
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: #pick right
            response = 1
            win.flip()
        elif '2' in theseKeys: #pick left
            response = 2
            win.flip()
        else: #did not pick
            response = 3
            RT = pickClock.getTime()
            win.flip()
    if response == 0:
        response = 3
    choice_2 ={'right':response == 1, 'left':response == 2, 'miss':response == 3}
    return choice_2 

#### play routine (MID routine) ####
def play_routine(win):
    playClock = core.Clock()
    playClock.reset()
    response = 0
    RT = 0 
    choice_3 = 0 #choice_3 refers to the play routine 
    ### start routine "play" ###
    theseKeys = event.getKeys(keyList=['1','2','escape'])
    while playClock.getTime() < 2.0:
        if len(theseKeys) > 0:
            if '1' in theseKeys: #pick right 
                response = 1
                win.flip()
                print('got right')
            elif '2' in theseKeys: # pick left 
                response = 2
                win.flip()
                print('got left')
            else: #did not pick
                response = 3
                win.flip()
                print('missed girly')
    if response == 0: 
        response = 3
        print('you need to fix this')
    choice_3 = {'win_right':response == 1, 'win_left':response == 2, 'loose':response == 3}
    return choice_3 


