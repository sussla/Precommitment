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
    optionValues = {'optionA':optionA, 'optionB':optionB, 'endA':endA, 'endB':endB}
    return optionValues

###### Pick to play or not routine ######
def pickoptions(win, length):
    pickoptionsClock = core.Clock()
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
def precomm_pick(win, length):
    pickClock = core.Clock()
    response = 0
    RT_precomm = 0
    choice_2 = 0 #choice_2 refers to the precommitment routine 
    #record responses
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: #pick right
            response = 1
            RT_precomm = pickClock.getTime()
            win.flip()
        elif '2' in theseKeys: #pick left
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
    choice_2 = {'right':response == 1, 'left':response == 2, 'miss':response == 3, 'RT_precomm': RT_precomm}
    return choice_2 

#### play routine (MID routine) ####
def play_routine(win, length):
    playClock = core.Clock()
    playClock.reset()
    response = 0
    played = 0
    late_reaction = 0
    #length = 0.5
    RT_play = 0
    choice_3 = 0 #choice_3 refers to the play routine 
    ### start routine "play" ###
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: #pick right
            if playClock.getTime() < 0.5:
                response = 1
                print('a')
                played = 1
                RT_play = playClock.getTime()
                win.flip()
            elif playClock.getTime() >= 0.5:
                response = 3
                print('one')
                late_reaction = 4
                RT_play = playClock.getTime()
                win.flip()
        elif '2' in theseKeys:
            if playClock.getTime() < 0.5: # pick left
                response = 2
                print('b')
                played = 1
                RT_play = playClock.getTime()
                win.flip()
            elif playClock.getTime() >= 0.5:
                response = 3
                print('two')
                late_reaction = 5
                RT_play = playClock.getTime()
                win.flip()
        else: #did not pick
            response = 3
            print('three')
            late_reaction = 6
            win.flip()
    if response == 0:
        response = 3
        win.flip()
        print('whoops')
    choice_3 = {'win_right':response == 1, 'win_left':response == 2, 'loose':response == 3,
                'late_right': late_reaction == 4, 'late_left': late_reaction == 5,
                'never_press': late_reaction == 6,
                'RT_play': RT_play}
    return choice_3

def press_late(win, length ):
    lateClock = core.Clock()
    response = 0
    RT_late = 0
    choice_4 = 0 #choice_2 refers to the precommitment routine
    #record responses
    theseKeys = event.getKeys(keyList=['1', '2', 'escape'])
    if len(theseKeys) > 0:
        if '1' in theseKeys: #pick right
            response = 1
            print('hello')
            RT_late = lateClock.getTime()
            win.flip()
        elif '2' in theseKeys: #pick left
            print('world')
            response = 2
            RT_late = lateClock.getTime()
            win.flip()
        else: #did not pick
            print('yup')
            response = 3
            RT_late = lateClock.getTime()
            win.flip()
    if response == 0:
        response = 3
        RT_late = lateClock.getTime()
    choice_2 = {'late_right':response == 1, 'late_left':response == 2, 'not_late':response == 3, 'RT_late': RT_late}
    return choice_2