from __future__ import absolute_import, division
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

def visual_bars(win, optionValues):
    # complete the path for calculating changing values
    h_optionA = (int(optionValues['optionA'])/100) * 0.8
    p_optionA = (-0.1 + h_optionA/2)
    h_endA = (int(optionValues['endA'])/100) * 0.8
    p_endA = (-0.1 + h_endA/2)
    h_optionB = (int(optionValues['optionB'])/100) * 0.8
    p_optionB = (-0.1 + h_optionB/2)
    h_endB = (int(optionValues['endB'])/100) * 0.8
    p_endB = (-0.1 + h_endB/2)
    # visual bars
    option_barA = visual.Rect(win=win, width=0.2, height=h_optionA, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_optionA])
    option_barB = visual.Rect(win=win, width=0.2, height=h_optionB, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_optionB])
    end_barA = visual.Rect(win=win, width=0.2, height=h_endA, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_endA])
    end_barB = visual.Rect(win=win, width=0.2, height=h_endB, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_endB])
    value_bars = {'option_barA': option_barA, 'option_barB': option_barB, 'end_barA': end_barA, 'end_barB': end_barB,
                  'h_endA': h_endA, 'p_endA': p_endA, 'h_endB': h_endB, 'p_endB': p_endB}
    return value_bars

###### Pick to play or not routine ######
def pickoptions(win, trialClock):
    #pickClock = core.Clock()
    #pickClock.reset()
    response = 0
    RT_choice = 0
    choice_1 = 0 # choice_1 refers to the pick or play routine
    ### start routine "pick options ###
    core.wait(1)
    win.flip()
    #while pickClock.getTime() < 4.0 and response == 0:
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
    #if pickClock.getTime() >= 4.0 and response == 0:
         #response == 0
         #response = 3
         #RT_choice = trialClock.getTime()
    choice_1 ={'play': response == 1, 'pick': response == 2, 'miss': response == 3, 'RT_choice': RT_choice}
    return choice_1

#### precommitment (pick) routine ####
def precomm_pick(win, trialClock):
    #precommClock = core.Clock()
    #precommClock.reset()
    response = 0
    RT_precomm = 0
    choice_2 = 0  # choice_2 refers to the precommitment routine
    # record responses
    #while precommClock.getTime() < 4.0 and response == 0:
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
    #if precommClock.getTime() >= 4.0 and response == 0:
        #response = 3
        #RT_precomm = trialClock.getTime()
        #win.flip()
    choice_2 = {'A': response == 1, 'B': response == 2, 'miss': response == 3, 'RT_precomm': RT_precomm}
    return choice_2 

#### play routine (MID routine) ####
def play_routine(win, optionValues, value_bars, trialClock):
    playClock = core.Clock()
    playClock.reset()
    response = 0
    length = 0.6
    RT_play = 0
    RT_trialClock_play = 0
    choice_3 = 0  # choice_3 refers to the play routine
    # show the option values as part of the play routine but need to define how to draw then a second time
    endoptionA = visual.TextStim(win=win, text=optionValues['endA'], name='endA', pos = [-0.5,-0.3],
                                 rgb= None, color=(1,1,1), colorSpace='rgb')
    endoptionB = visual.TextStim(win=win, text=optionValues['endB'], name='endB', pos = [0.5,-0.3],
                                 rgb= None, color=(1,1,1), colorSpace='rgb')
    endoptionA.draw()
    endoptionB.draw()
    value_bars['end_barA'].draw()
    value_bars['end_barB'].draw()
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

def values_change(win, optionValues):
    if optionValues['endA'] >= optionValues['optionA']:
        difference = int(optionValues['endA']) - int(optionValues['optionA'])
        step = difference / 6
        h_step1 = ((int(optionValues['optionA']) + (step * 1))/100) * 0.8
        h_step2 = ((int(optionValues['optionA']) + (step * 2))/100) * 0.8
        h_step3 = ((int(optionValues['optionA']) + (step * 3))/100) * 0.8
        h_step4 = ((int(optionValues['optionA']) + (step * 4))/100) * 0.8
        h_step5 = ((int(optionValues['optionA']) + (step * 5))/100) * 0.8
        h_step6 = ((int(optionValues['optionA']) + (step * 6))/100) * 0.8
        p_step1 = (-0.1 + h_step1/2)
        p_step2 = (-0.1 + h_step2/2)
        p_step3 = (-0.1 + h_step3/2)
        p_step4 = (-0.1 + h_step4/2)
        p_step5 = (-0.1 + h_step5/2)
        p_step6 = (-0.1 + h_step6/2)
        step1_barA = visual.Rect(win=win, width=0.2, height=h_step1, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step1])
        step2_barA = visual.Rect(win=win, width=0.2, height=h_step2, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step2])
        step3_barA = visual.Rect(win=win, width=0.2, height=h_step3, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step3])
        step4_barA = visual.Rect(win=win, width=0.2, height=h_step4, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step4])
        step5_barA = visual.Rect(win=win, width=0.2, height=h_step5, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step5])
        step6_barA = visual.Rect(win=win, width=0.2, height=h_step6, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step6])
    if optionValues['endA'] < optionValues['optionA']:
        difference = int(optionValues['optionA']) - int(optionValues['endA'])
        step = difference / 3
        h_step1 = ((int(optionValues['optionA']) - (step * 1)) / 100) * 0.8
        h_step2 = ((int(optionValues['optionA']) - (step * 2)) / 100) * 0.8
        h_step3 = ((int(optionValues['optionA']) - (step * 3)) / 100) * 0.8
        h_step4 = ((int(optionValues['optionA']) - (step * 4)) / 100) * 0.8
        h_step5 = ((int(optionValues['optionA']) - (step * 5)) / 100) * 0.8
        h_step6 = ((int(optionValues['optionA']) - (step * 6)) / 100) * 0.8
        p_step1 = (-0.1 + h_step1 / 2)
        p_step2 = (-0.1 + h_step2 / 2)
        p_step3 = (-0.1 + h_step3 / 2)
        p_step4 = (-0.1 + h_step4 / 2)
        p_step5 = (-0.1 + h_step5 / 2)
        p_step6 = (-0.1 + h_step6 / 2)
        step1_barA = visual.Rect(win=win, width=0.2, height=h_step1, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step1])
        step2_barA = visual.Rect(win=win, width=0.2, height=h_step2, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step2])
        step3_barA = visual.Rect(win=win, width=0.2, height=h_step3, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step3])
        step4_barA = visual.Rect(win=win, width=0.2, height=h_step4, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step4])
        step5_barA = visual.Rect(win=win, width=0.2, height=h_step5, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step5])
        step6_barA = visual.Rect(win=win, width=0.2, height=h_step6, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, p_step6])
    if optionValues['endB'] >= optionValues['optionB']:
        difference = int(optionValues['endB']) - int(optionValues['optionB'])
        step = difference / 6
        h_step1 = ((int(optionValues['optionB']) + (step * 1))/100) * 0.8
        h_step2 = ((int(optionValues['optionB']) + (step * 2))/100) * 0.8
        h_step3 = ((int(optionValues['optionB']) + (step * 3))/100) * 0.8
        h_step4 = ((int(optionValues['optionB']) + (step * 4))/100) * 0.8
        h_step5 = ((int(optionValues['optionB']) + (step * 5))/100) * 0.8
        h_step6 = ((int(optionValues['optionB']) + (step * 6))/100) * 0.8
        p_step1 = (-0.1 + h_step1/2)
        p_step2 = (-0.1 + h_step2/2)
        p_step3 = (-0.1 + h_step3/2)
        p_step4 = (-0.1 + h_step4/2)
        p_step5 = (-0.1 + h_step5/2)
        p_step6 = (-0.1 + h_step6/2)
        step1_barB = visual.Rect(win=win, width=0.2, height=h_step1, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step1])
        step2_barB = visual.Rect(win=win, width=0.2, height=h_step2, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step2])
        step3_barB = visual.Rect(win=win, width=0.2, height=h_step3, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step3])
        step4_barB = visual.Rect(win=win, width=0.2, height=h_step4, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step4])
        step5_barB = visual.Rect(win=win, width=0.2, height=h_step5, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step5])
        step6_barB = visual.Rect(win=win, width=0.2, height=h_step6, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step6])
    elif optionValues['endB'] < optionValues['optionB']:
        difference = int(optionValues['optionB']) - int(optionValues['endB'])
        step = difference / 3
        h_step1 = ((int(optionValues['optionB']) - (step * 1)) / 100) * 0.8
        h_step2 = ((int(optionValues['optionB']) - (step * 2)) / 100) * 0.8
        h_step3 = ((int(optionValues['optionB']) - (step * 3)) / 100) * 0.8
        h_step4 = ((int(optionValues['optionB']) - (step * 4)) / 100) * 0.8
        h_step5 = ((int(optionValues['optionB']) - (step * 5)) / 100) * 0.8
        h_step6 = ((int(optionValues['optionB']) - (step * 6)) / 100) * 0.8
        p_step1 = (-0.1 + h_step1 / 2)
        p_step2 = (-0.1 + h_step2 / 2)
        p_step3 = (-0.1 + h_step3 / 2)
        p_step4 = (-0.1 + h_step4 / 2)
        p_step5 = (-0.1 + h_step5 / 2)
        p_step6 = (-0.1 + h_step6 / 2)
        step1_barB = visual.Rect(win=win, width=0.2, height=h_step1, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step1])
        step2_barB = visual.Rect(win=win, width=0.2, height=h_step2, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step2])
        step3_barB = visual.Rect(win=win, width=0.2, height=h_step3, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step3])
        step4_barB = visual.Rect(win=win, width=0.2, height=h_step4, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step4])
        step5_barB = visual.Rect(win=win, width=0.2, height=h_step5, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step5])
        step6_barB = visual.Rect(win=win, width=0.2, height=h_step6, lineColor=[0, 1, 0],
                                 autoLog=None, fillColor=[0, 1, 0], pos=[0.5, p_step6])
    bars = {'step1_barA': step1_barA, 'step2_barA': step2_barA, 'step3_barA': step3_barA, 'step4_barA': step4_barA,
            'step5_barA': step5_barA, 'step6_barA': step6_barA, 'step1_barB': step1_barB, 'step2_barB': step2_barB,
            'step3_barB': step3_barB, 'step4_barB': step4_barB, 'step5_barB': step5_barB, 'step6_barB': step6_barB}
    return bars