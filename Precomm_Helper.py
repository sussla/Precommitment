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
def play_routine(win, optionValues, value_bars, trialClock):
    playClock = core.Clock()
    playClock.reset()
    response = 0
    length = 0.6
    RT_play = 0
    RT_trialClock_play = 0
    choice_3 = 0  # choice_3 refers to the play routine
    # show the option values as part of the play routine but need to define how to draw then a second time
    endoptionA = visual.TextStim(win=win, text=optionValues['endA'], name='endA', pos = [-0.5,-0.3], rgb= None, color=(1,1,1), colorSpace='rgb')
    endoptionB = visual.TextStim(win=win, text=optionValues['endB'], name='endB', pos = [0.5,-0.3], rgb= None, color=(1,1,1), colorSpace='rgb')
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

def value_bar(win, optionValues):
    option_barA = 0
    option_barB = 0
    end_barA = 0
    end_barB = 0
    # 5 - 15 (First)
    if (optionValues['optionA'] <= 15):
        option_barA = visual.Rect(win, width=0.2, height=0.02,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.095])
    if (optionValues['optionB'] <= 15):
        option_barB = visual.Rect(win, width=0.2, height=0.02,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.095])
    if (optionValues['endA'] <= 15):
        end_barA = visual.Rect(win, width=0.2, height=0.02,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.095])
    if (optionValues['endB'] <= 15):
        end_barB = visual.Rect(win, width=0.2, height=0.02,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.095])
    # 16 - 25 (Second)
    if (optionValues['optionA'] > 15) and (optionValues['optionA'] <= 25):
        option_barA = visual.Rect(win, width=0.2, height=0.12, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.037])
    if (optionValues['optionB'] > 15) and (optionValues['optionB'] <= 25):
        option_barB = visual.Rect(win, width=0.2, height=0.12,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.037])
    if (optionValues['endA'] > 15) and (optionValues['endA'] <= 25):
        end_barA = visual.Rect(win, width=0.2, height=0.12,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.037])
    if (optionValues['endB'] > 15) and (optionValues['endB'] <= 25):
        end_barB = visual.Rect(win, width=0.2, height=0.12,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.037])
    # 26 - 35 (Third)
    if (optionValues['optionA'] > 25) and (optionValues['optionA'] <= 35):
        option_barA = visual.Rect(win, width=0.2, height=0.22,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.015])
    if (optionValues['optionB'] > 25) and (optionValues['optionB'] <= 35):
        option_barB = visual.Rect(win, width=0.2, height=0.22,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.015])
    if (optionValues['endA'] > 25) and (optionValues['endA'] <= 35):
        end_barA = visual.Rect(win, width=0.2, height=0.22,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.015])
    if (optionValues['endB'] > 25) and (optionValues['endB'] <= 35):
        end_barB = visual.Rect(win, width=0.2, height=0.22,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.015])
    # 36 - 45 (Fourth)
    if (optionValues['optionA'] > 35) and (optionValues['optionA'] <= 45):
        option_barA = visual.Rect(win, width=0.2, height=0.32, lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.065])
    if (optionValues['optionB'] > 35) and (optionValues['optionB'] <= 45):
        option_barB = visual.Rect(win, width=0.2, height=0.32,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.065])
    if (optionValues['endA'] > 35) and (optionValues['endA'] <= 45):
        end_barA = visual.Rect(win, width=0.2, height=0.32,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.065])
    if (optionValues['endB'] > 35) and (optionValues['endB'] <= 45):
        end_barB = visual.Rect(win, width=0.2, height=0.32,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.065])
    # 46 - 55 (Fifth)
    if (optionValues['optionA'] > 45) and (optionValues['optionA'] <= 55):
        option_barA = visual.Rect(win, width=0.2, height=0.42,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.113])
    if (optionValues['optionB'] > 45) and (optionValues['optionB'] <= 55):
        option_barB = visual.Rect(win, width=0.2, height=0.42,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.113])
    if (optionValues['endA'] > 45) and (optionValues['endA'] <= 55):
        end_barA = visual.Rect(win, width=0.2, height=0.42,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.113])
    if (optionValues['endB'] > 45) and (optionValues['endB'] <= 55):
        end_barB = visual.Rect(win, width=0.2, height=0.42,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.113])
    # 56 - 65 (Sixth)
    if (optionValues['optionA'] > 55) and (optionValues['optionA'] <= 65):
        option_barA = visual.Rect(win, width=0.2, height=0.52,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.164])
    if (optionValues['optionB'] > 55) and (optionValues['optionB'] <= 65):
        option_barB = visual.Rect(win, width=0.2, height=0.52,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.164])
    if (optionValues['endA'] > 55) and (optionValues['endA'] <= 65):
        end_barA = visual.Rect(win, width=0.2, height=0.52,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.164])
    if (optionValues['endB'] > 55) and (optionValues['endB'] <= 65):
        end_barB = visual.Rect(win, width=0.2, height=0.52,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.164])
    # 66 - 75 (Seventh)
    if (optionValues['optionA'] > 65) and (optionValues['optionA'] <= 75):
        option_barA = visual.Rect(win, width=0.2, height=0.62,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.215])
    if (optionValues['optionB'] > 65) and (optionValues['optionB'] <= 75):
        option_barB = visual.Rect(win, width=0.2, height=0.62,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.215])
    if (optionValues['endA'] > 65) and (optionValues['endA'] <= 75):
        end_barA = visual.Rect(win, width=0.2, height=0.62,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.215])
    if (optionValues['endB'] > 65) and (optionValues['endB'] <= 75):
        end_barB = visual.Rect(win, width=0.2, height=0.62,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.215])
    # 76 - 85 (Eighth)
    if (optionValues['optionA'] > 75) and (optionValues['optionA'] <= 85):
        option_barA = visual.Rect(win, width=0.2, height=0.72,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.262])
    if (optionValues['optionB'] > 75) and (optionValues['optionB'] <= 85):
        option_barB = visual.Rect(win, width=0.2, height=0.72,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.262])
    if (optionValues['endA'] > 75) and (optionValues['endA'] <= 85):
        end_barA = visual.Rect(win, width=0.2, height=0.72,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, 0.262])
    if (optionValues['endB'] > 75) and (optionValues['endB'] <= 85):
        end_barB = visual.Rect(win, width=0.2, height=0.72, lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [0.5, 0.262])
    # 86 - 95 (Ninth)
    if (optionValues['optionA'] > 85) and (optionValues['optionA'] <= 95):
        option_barA = visual.Rect(win, width=0.2, height=0.8,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, -0.3])
    if (optionValues['optionB'] > 85) and (optionValues['optionB'] <= 95):
        option_barB = visual.Rect(win, width=0.2, height=0.8,  lineColor=[0, 1, 0],
                                  autoLog=None, fillColor=[0, 1, 0], pos = [0.5, -0.3])
    if (optionValues['endA'] > 85) and (optionValues['endA'] <= 95):
        end_barA = visual.Rect(win, width=0.2, height=0.8,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [-0.5, -0.3])
    if (optionValues['endB'] > 85) and (optionValues['endB'] <= 95):
        end_barB = visual.Rect(win, width=0.2, height=0.8,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos = [0.5, -0.3])
    bars = {'option_barA': option_barA,'option_barB': option_barB, 'end_barA': end_barA, 'end_barB': end_barB}
    return bars


def random_bars(win):
    # Value A bars
    First_barA = visual.Rect(win, width=0.2, height=0.02, lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.095])
    Second_barA = visual.Rect(win, width=0.2, height=0.12, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, -0.037])
    Third_barA = visual.Rect(win, width=0.2, height=0.22,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.015])
    Fourth_barA = visual.Rect(win, width=0.2, height=0.32,  lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.065])
    Fifth_barA = visual.Rect(win, width=0.2, height=0.42,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.113])
    Sixth_barA = visual.Rect(win, width=0.2, height=0.52,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.164])
    Seventh_barA = visual.Rect(win, width=0.2, height=0.62, lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.215])
    Eighth_barA = visual.Rect(win, width=0.2, height=0.72, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.262])
    Ninth_barA = visual.Rect(win, width=0.2, height=0.8,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[-0.5, 0.3])
    # Value B bars
    First_barB = visual.Rect(win, width=0.2, height=0.02,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.095])
    Second_barB = visual.Rect(win, width=0.2, height=0.12, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[0.5, -0.037])
    Third_barB = visual.Rect(win, width=0.2, height=0.22,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.015])
    Fourth_barB = visual.Rect(win, width=0.2, height=0.32, lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.065])
    Fifth_barB = visual.Rect(win, width=0.2, height=0.42, lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.113])
    Sixth_barB = visual.Rect(win, width=0.2, height=0.52,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.164])
    Seventh_barB = visual.Rect(win, width=0.2, height=0.62,  lineColor=[0, 1, 0],
                               autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.215])
    Eighth_barB = visual.Rect(win, width=0.2, height=0.72,  lineColor=[0, 1, 0],
                              autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.262])
    Ninth_barB = visual.Rect(win, width=0.2, height=0.8,  lineColor=[0, 1, 0],
                             autoLog=None, fillColor=[0, 1, 0], pos=[0.5, 0.3])
    # List for the random choice
    List_A = [First_barA, Second_barA, Third_barA, Fourth_barA, Fifth_barA, Sixth_barA,
                                        Seventh_barA, Eighth_barA, Ninth_barA]
    List_B = [First_barB, Second_barB, Third_barB, Fourth_barB, Fifth_barB, Sixth_barB,
                                        Seventh_barB, Eighth_barB, Ninth_barB]
    # Random Bar choices A
    Random_BarA1 = random.choice(List_A)
    Random_BarA2 = random.choice(List_A)
    Random_BarA3 = random.choice(List_A)
    Random_BarA4 = random.choice(List_A)
    # Random Bar choices B
    Random_BarB1 = random.choice(List_B)
    Random_BarB2 = random.choice(List_B)
    Random_BarB3 = random.choice(List_B)
    Random_BarB4 = random.choice(List_B)
    #Export List
    random_bars ={'Random_BarA1': Random_BarA1, 'Random_BarA2': Random_BarA2, 'Random_BarA3': Random_BarA3,
                  'Random_BarB1' : Random_BarB1, 'Random_BarB2': Random_BarB2, 'Random_BarB3': Random_BarB3,
                  'Random_BarA4' : Random_BarA4, 'Random_BarB4' : Random_BarB4}
    return random_bars