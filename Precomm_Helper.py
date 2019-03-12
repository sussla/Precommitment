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
    w = 60  # width of each range
    # derived params
    b1 = a1 + w 
    b2 = a2 + w 
    # pick options
    optionA = random.choice(range(a1, b1, 1))
    optionB = random.choice(range(a2, b2, 1))
    # end values
    endA = random.choice(range(a1, b1, 1))
    endB = random.choice(range(a2, b2, 1))
    # difference between values
    A_difference = optionA - endA
    B_difference = optionB - endB
    # largest of options
    max_option = max(optionA, optionB)
    # largest of end values
    max_end = max(endA, endB)
    # if the best option changes or stays the same
    change = 0
    if (optionA >= optionB) and (endA >= endB):
        change = 1
    if (optionA <= optionB) and (endA <= endB):
        change = 2
    if (optionA >= optionB and endA <= endB) or (optionA <= optionB and endA >= endB):
        change = 3
    optionValues = {'optionA': optionA, 'optionB': optionB, 'endA': endA, 'endB': endB,
                    'A_difference': A_difference, 'B_difference': B_difference,
                   'max_option': max_option, 'max_end': max_end,
                    'A_always': change == 1, 'B_always': change == 2, 'changes': change == 3}
    return optionValues

###### Pick to play or not routine ######
def pickoptions(win, trialClock):
    response = 0
    RT_choice = 0
    choice_1 = 0 # choice_1 refers to the pick or play routine
    ### start routine "pick options ###
    core.wait(1)
    win.flip()
    # record responses
    theseKeys = event.getKeys(keyList=['up', 'down', 'escape'])
    if len(theseKeys) > 0:
        if 'up' in theseKeys: # pick play
            response = 1
            RT_choice = trialClock.getTime()
            win.flip()
        elif 'down' in theseKeys: # pick pick
            response = 2
            RT_choice = trialClock.getTime()
            win.flip()
        else: # did not pick
            response = 3
            RT_choice = trialClock.getTime()
            win.flip()
    if response == 0: 
        response = 3
        RT_choice = trialClock.getTime()
    choice_1 ={'play': response == 1, 'pick': response == 2, 'miss': response == 3, 'RT_choice': RT_choice}
    return choice_1

#### precommitment (pick) routine ####
def precomm_pick(win, trialClock):
    response = 0
    RT_precomm = 0
    choice_2 = 0  # choice_2 refers to the precommitment routine
    # record responses
    theseKeys = event.getKeys(keyList=['left', 'right', 'escape'])
    if len(theseKeys) > 0:
        if 'left' in theseKeys:  # pick left
            response = 1
            RT_precomm = trialClock.getTime()
            win.flip()
        elif 'right' in theseKeys:  # pick right
            response = 2
            RT_precomm = trialClock.getTime()
            win.flip()
        else:  # did not pick
            response = 3
            RT_precomm = trialClock.getTime()
            win.flip()
    if response == 0:
        response = 3
        RT_precomm = trialClock.getTime()
    choice_2 = {'A': response == 1, 'B': response == 2, 'miss': response == 3, 'RT_precomm': RT_precomm}
    return choice_2 

#### play routine (MID routine) ####
def play_routine(win, optionValues, trialClock):
    playClock = core.Clock()
    playClock.reset()
    response = 0
    length = 0.6
    RT_play = 0
    RT_trialClock_play = 0
    choice_3 = 0  # choice_3 refers to the play routine
    # show the option values as part of the play routine but need to define how to draw then a second time
    endoptionA = visual.TextStim(win=win, text= optionValues['endA'], name='endA', pos = [0.5,0], rgb= None, color=(0,1,0), colorSpace='rgb')
    endoptionB = visual.TextStim(win=win, text= optionValues['endB'], name='endB', pos = [-0.5,0], rgb= None, color=(1,0,0), colorSpace='rgb')
    endoptionA.draw()
    endoptionB.draw()
    win.flip()
    core.wait(0.5)  # how long the end values are on the screen for the quick MID section
    ### start routine "play" ###
    while playClock.getTime() < length:
        theseKeys = event.getKeys(keyList=['left', 'right', 'escape'])
        if len(theseKeys) > 0:
            if 'left' in theseKeys:  # pick left
                response = 1
                RT_play = playClock.getTime()
                RT_trialClock_play = trialClock.getTime()
                win.flip()
            elif 'right' in theseKeys:  # pick right
                response = 2
                RT_play = playClock.getTime()
                RT_trialClock_play = trialClock.getTime()
                win.flip()
            else:  # did not pick
                response = 3
                RT_play = playClock.getTime()
                RT_trialClock_play = trialClock.getTime()
                win.flip()
    if response == 0:
        response = 3
        win.flip()
    choice_3 = {'A': response == 1, 'B': response == 2, 'loose': response == 3,
                'RT_play': RT_play, 'RT_trialClock_play': RT_trialClock_play}
    return choice_3

def press_late(win, trialClock):
    response = 0
    RT_late = 0
    choice_4 = 0
    # record responses
    theseKeys = event.getKeys(keyList=['left', 'right', 'escape'])
    if len(theseKeys) > 0:
        if 'left' in theseKeys:  # pick right
            response = 1
            RT_late = trialClock.getTime()
            win.flip()
        elif 'right' in theseKeys:  # pick left
            response = 2
            RT_late = trialClock.getTime()
            win.flip()
        else:  # did not pick
            response = 3
            RT_late = trialClock.getTime()
            win.flip()
    if response == 0:
        response = 3
        RT_late = trialClock.getTime()
    choice_4 = {'late_A': response == 1, 'late_B': response == 2, 'not_late': response == 3, 'RT_late': RT_late}
    return choice_4

def value_bar(win, optionValues):
    # 5 - 15
    bar_1A = visual.Rect(win, width=0.2, height=0.02, autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.095])
    bar_1B = visual.Rect(win, width=0.2, height=0.02, autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.095])
    # 16 - 25
    bar_2A = visual.Rect(win, width=0.2, height=0.12, autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.037])
    bar_2B = visual.Rect(win, width=0.2, height=0.12, autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.037])
    # 26 - 35
    bar_3A = visual.Rect(win, width=0.2, height=0.22, autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, ])
    bar_3B = visual.Rect(win, width=0.2, height=0.22, autoLog=None, fillColor=[0, 1, 0], pos = [0.5, ])
    # 36 - 45
    bar_4A = visual.Rect(win, width=0.2, height=0.32, autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, ])
    bar_4B = visual.Rect(win, width=0.2, height=0.32, autoLog=None, fillColor=[0, 1, 0], pos = [0.5, ])
    # 46 - 55
    bar_5A = visual.Rect(win, width=0.2, height=0.42, autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, ])
    bar_5B = visual.Rect(win, width=0.2, height=0.42, autoLog=None, fillColor=[0, 1, 0], pos = [0.5, ])
    # 56 - 65
    bar_6A = visual.Rect(win, width=0.2, height=0.52, autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, ])
    bar_6B = visual.Rect(win, width=0.2, height=0.52, autoLog=None, fillColor=[0, 1, 0], pos = [0.5, ])
    # 66 - 75
    bar_7A = visual.Rect(win, width=0.2, height=0.62, autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, ])
    bar_7B = visual.Rect(win, width=0.2, height=0.62, autoLog=None, fillColor=[0, 1, 0], pos = [0.5, ])
    # 76 - 85
    bar_8A = visual.Rect(win, width=0.2, height=0.72, autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, ])
    bar_8B = visual.Rect(win, width=0.2, height=0.72, autoLog=None, fillColor=[0, 1, 0], pos = [0.5, ])
    # 86 - 95
    bar_9A = visual.Rect(win, width=0.2, height=0.8, autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, -0.3])
    bar_9B = visual.Rect(win, width=0.2, height=0.8, autoLog=None, fillColor=[0, 1, 0], pos = [0.5, -0.3])

    bars = {'bar_1A': bar_1A,'bar_1B': bar_1B, 'bar_2A': bar_2A, 'bar_2B': bar_2B, 'bar_3A': bar_3A,
            'bar_3B': bar_3B, 'bar_4A': bar_4A, 'bar_4B': bar_4B, 'bar_5A': bar_5A, 'bar_5B': bar_5B,
            'bar_6A': bar_6A, 'bar_6B': bar_6B, 'bar_7A': bar_7A, 'bar_7B': bar_7B, 'bar_8A': bar_8A,
            'bar_8B': bar_8B, 'bar_9A': bar_9A, 'bar_9B': bar_9B}
    return bars