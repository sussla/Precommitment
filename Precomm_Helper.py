from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import csv
import random


##### new function to pick options only
def pickvalues():
    a1 = 5 
    a2 = 15 
    w = 60 # width of each range
    # derived params
    b1 = a1 + w 
    b2 = a2 + w 
    # pick options
    optionA = random.choice(range(a1, b1, 1))
    optionB = random.choice(range(a2, b2, 1))
    # end values
    endA = random.choice(range(a1, b1, 1))
    endB = random.choice(range(a2, b2, 1))
    #differnce between values
    A_difference = optionA - endA
    B_difference = optionB - endB
    #largest of options
    max_option = max(optionA, optionB)
    #largest of end values
    max_end = max(endA, endB)
    #if the best option changes or stays the same
    change = 0
    if (optionA >= optionB) and (endA >= endB):
        change = 1
    if (optionA <= optionB) and (endA <= endB):
        change = 2
    if (optionA >= optionB and endA <= endB) or (optionA <= optionB and endA >= endB):
        change = 3
    optionValues = {'optionA':optionA, 'optionB':optionB, 'endA':endA, 'endB':endB,
                    'A_difference':A_difference, 'B_difference':B_difference,
                   'max_option':max_option, 'max_end':max_end,
                    'A_always':change ==1, 'B_always':change ==2, 'changes':change ==3}
    return optionValues

###### Pick to play or not routine ######
def pickoptions(win):
    pickoptionsClock = core.Clock()
    pickoptionsClock.reset()
    response = 0
    RT_choice = 0
    choice_1 = 0 # choice_1 refers to the pick or play routine
    ### start routine "pick options ###
    core.wait(1)
    win.flip()
    # record responses
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: # pick play
            response = 1
            RT_choice = pickoptionsClock.getTime()
            win.flip()
        elif '2' in theseKeys: # pick pick
            response = 2
            RT_choice = pickoptionsClock.getTime()
            win.flip()
        else: # did not pick
            response = 3
            RT_choice = pickoptionsClock.getTime()
            win.flip()
    if response == 0: 
        response = 3
        RT_choice = pickoptionsClock.getTime()
    choice_1 ={'play':response == 1, 'pick':response == 2, 'miss': response == 3, 'RT_choice': RT_choice}
    return choice_1

#### precommitment (pick) routine ####
def precomm_pick(win):
    pickClock = core.Clock()
    #pickClock.reset()
    response = 0
    RT_precomm = 0
    choice_2 = 0 #choice_2 refers to the precommitment routine 
    #record responses
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: #pick left
            response = 1
            RT_precomm = pickClock.getTime()
            win.flip()
        elif '2' in theseKeys: #pick right
            response = 2
            RT_precomm = pickClock.getTime()
            win.flip()
        else: #did not pick
            response = 3
            RT_precomm = pickClock.getTime()
            win.flip()
    if response == 0:
        response = 3
        RT_precomm = pickClock.getTime()
    choice_2 = {'B':response == 1, 'A':response == 2, 'miss':response == 3, 'RT_precomm': RT_precomm}
    return choice_2 

#### play routine (MID routine) ####
def play_routine(win, optionValues):
    playClock = core.Clock()
    playClock.reset()
    response = 0
    length = 0.5
    RT_play = 0
    choice_3 = 0 #choice_3 refers to the play routine 
    ### start routine "play" ###
   # theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    while playClock.getTime() < length:
        theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
        if len(theseKeys) > 0:
            if '1' in theseKeys: #pick left
                response = 1
                RT_play = playClock.getTime()
                win.flip()
            elif '2' in theseKeys: #pick right
                response = 2
                RT_play = playClock.getTime()
                win.flip()
            else: #did not pick
                response = 3
                RT_play = playClock.getTime()
                win.flip()
    if response == 0:
        response = 3
        win.flip()
    choice_3 = {'B':response == 1, 'A':response == 2, 'loose':response == 3, 'RT_play': RT_play}
    return choice_3

def press_late(win):
    lateClock = core.Clock()
    lateClock.reset()
    response = 0
    RT_late = 0
    choice_4 = 0
    #record responses
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: #pick right
            response = 1
            RT_late = lateClock.getTime()
            win.flip()
        elif '2' in theseKeys: #pick left
            response = 2
            RT_late = lateClock.getTime()
            win.flip()
        else: #did not pick
            response = 3
            RT_late = lateClock.getTime()
            win.flip()
    if response == 0:
        response = 3
        RT_late = lateClock.getTime()
    choice_4 = {'late_B':response == 1, 'late_A':response == 2, 'not_late':response == 3, 'RT_late': RT_late}
    return choice_4