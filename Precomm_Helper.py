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

#### values associated with d and c values in practice task ###
def pvalues(alphabet):
    letter = random.choice(alphabet)
    A_start = 0
    A_end = 0
    B_start = 0
    B_end = 0
    d = 0  # d indicates the difference between the starting values
    c = 0  # c indicates the change that both of the values will take
    if letter == 'a':
        d = 20
        c = 3
    if letter == 'b':
        d = 20
        c = -3
    if letter == 'e':
        d = 20
        c = 9
    if letter == 'g':
        d = 20
        c = 13
    if letter == 'o':
        d = 28
        c = 3
    if letter == 'x':
        d = 28
        c = -13
    if letter == 's':
        d = 4
        c = 3
    if letter == 'r':
        d = 4
        c = 9
    if letter == 'q':
        d = 4
        c = -13

    if letter == 'u':
        d = 12
        c = 9
    if letter == 'f':
        d = 12
        c = -9
    if letter == 'k':
        d = 12
        c = 13
    First_start = random.choice(range(13, 58, 1))
    Second_start = First_start + d
    First_end = First_start + c
    Second_end = Second_start - c
    r = random.choice(range(0, 1, 1))
    if r == 1:
        A_start = First_start
        A_end = First_end
        B_start = Second_start
        B_end = Second_end
    if r == 0:
        A_start = Second_start
        A_end = Second_end
        B_start = First_start
        B_end = First_end
    # Determine which value is larger or smaller
    max_start = max(A_start, B_start)
    min_start = min(A_start, B_start)
    max_end = max(A_end, B_end)
    min_end = min(A_end, B_end)
    # if best option changes or stays the same
    change = 0
    if (A_start == max_start) and (A_end == max_end):
        change = 1
    if (B_start == max_start) and (B_end == max_end):
        change = 2
    if (A_start == max_start and A_end == min_end) or (B_start == max_start and B_end == min_end):
        change = 3
    optionValues = {'letter': letter, 'optionA': A_start, 'optionB': B_start, 'endA': A_end, 'endB': B_end,
                    'difference': d, 'change': c,
                    'A_always': change == 1, 'B_always': change == 2, 'changes': change == 3}
    return optionValues


def better_wait_values(split_alphabet_A):
    letter = random.choice(split_alphabet_A)
    A_start = 0
    A_end = 0
    B_start = 0
    B_end = 0
    d = 0  # d indicates the difference between the starting values
    c = 0  # c indicates the change that both of the values will take
    if letter == 'a':
        d = 4
        c = 3
    if letter == 'b':
        d = 4
        c = -3
    if letter == 'c':
        d = 4
        c = 9
    if letter == 'd':
        d = 4
        c = -9
    if letter == 'e':
        d = 4
        c = 13
    if letter == 'f':
        d = 4
        c = -13
    if letter == 'g':
        d = 12
        c = 3
    if letter == 'h':
        d = 12
        c = -3
    if letter == 'i':
        d = 12
        c = 9
    if letter == 'j':
        d = 12
        c = -9
    if letter == 'k':
        d = 12
        c = 13
    if letter == 'l':
        d = 12
        c = -13
    if letter == 'aa':
        d = 4
        c = 3
    if letter == 'bb':
        d = 4
        c = -3
    if letter == 'cc':
        d = 4
        c = 9
    if letter == 'dd':
        d = 4
        c = -9
    if letter == 'ee':
        d = 4
        c = 13
    if letter == 'ff':
        d = 4
        c = -13
    if letter == 'gg':
        d = 12
        c = 3
    if letter == 'hh':
        d = 12
        c = -3
    if letter == 'ii':
        d = 12
        c = 9
    if letter == 'jj':
        d = 12
        c = -9
    if letter == 'kk':
        d = 12
        c = 13
    if letter == 'll':
        d = 12
        c = -13
    if letter == 'aaa':
        d = 4
        c = 3
    if letter == 'bbb':
        d = 4
        c = -3
    if letter == 'ccc':
        d = 4
        c = 9
    if letter == 'ddd':
        d = 4
        c = -9
    if letter == 'eee':
        d = 4
        c = 13
    if letter == 'fff':
        d = 4
        c = -13
    if letter == 'ggg':
        d = 12
        c = 3
    if letter == 'hhh':
        d = 12
        c = -3
    if letter == 'iii':
        d = 12
        c = 9
    if letter == 'jjj':
        d = 12
        c = -9
    if letter == 'kkk':
        d = 12
        c = 13
    if letter == 'lll':
        d = 12
        c = -13
    First_start = random.choice(range(13, 58, 1))
    Second_start = First_start + d
    First_end = First_start + c
    Second_end = Second_start - c
    r = random.choice(range(0, 1, 1))
    if r == 1:
        A_start = First_start
        A_end = First_end
        B_start = Second_start
        B_end = Second_end
    if r == 0:
        A_start = Second_start
        A_end = Second_end
        B_start = First_start
        B_end = First_end
    # Determine which value is larger or smaller
    max_start = max(A_start, B_start)
    min_start = min(A_start, B_start)
    max_end = max(A_end, B_end)
    min_end = min(A_end, B_end)
    # if best option changes or stays the same
    change = 0
    if (A_start == max_start) and (A_end == max_end):
        change = 1
    if (B_start == max_start) and (B_end == max_end):
        change = 2
    if (A_start == max_start and A_end == min_end) or (B_start == max_start and B_end == min_end):
        change = 3
    optionValues = {'letter': letter, 'optionA': A_start, 'optionB': B_start, 'endA': A_end, 'endB': B_end,
                    'difference': d, 'change': c,
                    'A_always': change == 1, 'B_always': change == 2, 'changes': change == 3}
    return optionValues

def better_commit_values(split_alphabet_B):
    letter = random.choice(split_alphabet_B)
    A_start = 0
    A_end = 0
    B_start = 0
    B_end = 0
    d = 0  # d indicates the difference between the starting values
    c = 0  # c indicates the change that both of the values will take
    if letter == 'a':
        d = 20
        c = 3
    if letter == 'b':
        d = 20
        c = -3
    if letter == 'c':
        d = 20
        c = 9
    if letter == 'd':
        d = 20
        c = -9
    if letter == 'e':
        d = 20
        c = 13
    if letter == 'f':
        d = 20
        c = -13
    if letter == 'g':
        d = 28
        c = 3
    if letter == 'h':
        d = 28
        c = -3
    if letter == 'i':
        d = 28
        c = 9
    if letter == 'j':
        d = 28
        c = -9
    if letter == 'k':
        d = 28
        c = 13
    if letter == 'l':
        d = 28
        c = -13
    if letter == 'aa':
        d = 20
        c = 3
    if letter == 'bb':
        d = 20
        c = -3
    if letter == 'cc':
        d = 20
        c = 9
    if letter == 'dd':
        d = 20
        c = -9
    if letter == 'ee':
        d = 20
        c = 13
    if letter == 'ff':
        d = 20
        c = -13
    if letter == 'gg':
        d = 28
        c = 3
    if letter == 'hh':
        d = 28
        c = -3
    if letter == 'ii':
        d = 28
        c = 9
    if letter == 'jj':
        d = 28
        c = -9
    if letter == 'kk':
        d = 28
        c = 13
    if letter == 'll':
        d = 28
        c = -13
    if letter == 'aaa':
        d = 20
        c = 3
    if letter == 'bbb':
        d = 20
        c = -3
    if letter == 'ccc':
        d = 20
        c = 9
    if letter == 'ddd':
        d = 20
        c = -9
    if letter == 'eee':
        d = 20
        c = 13
    if letter == 'fff':
        d = 20
        c = -13
    if letter == 'ggg':
        d = 28
        c = 3
    if letter == 'hhh':
        d = 28
        c = -3
    if letter == 'iii':
        d = 28
        c = 9
    if letter == 'jjj':
        d = 28
        c = -9
    if letter == 'kkk':
        d = 28
        c = 13
    if letter == 'lll':
        d = 28
        c = -13
    First_start = random.choice(range(13, 58, 1))
    Second_start = First_start + d
    First_end = First_start + c
    Second_end = Second_start - c
    r = random.choice(range(0, 1, 1))
    if r == 1:
        A_start = First_start
        A_end = First_end
        B_start = Second_start
        B_end = Second_end
    if r == 0:
        A_start = Second_start
        A_end = Second_end
        B_start = First_start
        B_end = First_end
    # Determine which value is larger or smaller
    max_start = max(A_start, B_start)
    min_start = min(A_start, B_start)
    max_end = max(A_end, B_end)
    min_end = min(A_end, B_end)
    # if best option changes or stays the same
    change = 0
    if (A_start == max_start) and (A_end == max_end):
        change = 1
    if (B_start == max_start) and (B_end == max_end):
        change = 2
    if (A_start == max_start and A_end == min_end) or (B_start == max_start and B_end == min_end):
        change = 3
    optionValues = {'letter': letter, 'optionA': A_start, 'optionB': B_start, 'endA': A_end, 'endB': B_end,
                    'difference': d, 'change': c,
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
    response = 0
    RT_choice = 0
    ### start routine "pick options ###
    core.wait(1)
    win.flip()
    # record responses
    theseKeys = event.getKeys(keyList=['up', 'down', 'escape'])
    if len(theseKeys) > 0:
        if 'up' in theseKeys: # pick wait
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
    choice_1 ={'wait': response == 1, 'commit': response == 2, 'miss': response == 3, 'RT_choice': RT_choice}
    return choice_1

#### precommitment (pick) routine ####
def precomm_pick(win, trialClock):
    response = 0
    RT_precomm = 0
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


#### MID play routine ####
def play_mid(win, trialClock, length):
    midClock = core.Clock()
    midClock.reset()
    response = 0
    hit = 0
    RT_play = 0
    RT_trialClock_play = 0
    #MID_square
    square = visual.Rect(win=win, width=0.5, height=0.5, autoLog=None, fillColor='white', pos=[0,0])
    square.draw()
    win.flip()
    core.wait(0.2)
    while midClock.getTime() < length:
        theseKeys = event.getKeys(keyList=['space', 'escape'])
        if len(theseKeys) > 0:
            if 'space' in theseKeys:  # hit
                hit = 1
                RT_play = midClock.getTime()
                RT_trialClock_play = trialClock.getTime()
                response = 1
                win.flip()
            else:  # did not pick
                hit = 2
                response = 2
                RT_play = midClock.getTime()
                RT_trialClock_play = trialClock.getTime()
                win.flip()
    if response == 0:
        response = 2
        hit = 2
        win.flip()
    choice_3 = {'hit': response == 1, 'miss': response == 2, 'press_hit': hit == 1, 'press_miss': hit == 2,
                'RT_play': RT_play, 'RT_trialClock_play': RT_trialClock_play}
    return choice_3

#### routine that allows you to pick an option after you win MID game ###
def hit_pick(win, trialClock):
    response = 0
    RT_hitChoice = 0
    # record responses
    theseKeys = event.getKeys(keyList=['left', 'right', 'escape'])
    if len(theseKeys) > 0:
        if 'left' in theseKeys:  # pick left
            response = 1
            RT_hitChoice = trialClock.getTime()
            win.flip()
        elif 'right' in theseKeys:  # pick right
            response = 2
            RT_hitChoice = trialClock.getTime()
            win.flip()
        else:  # did not pick
            response = 3
            RT_hitChoice = trialClock.getTime()
            win.flip()
    if response == 0:
        response = 3
        RT_hitChoice = trialClock.getTime()
    choice_3 = {'A': response == 1, 'B': response == 2, 'miss': response == 3, 'RT_hitChoice': RT_hitChoice}
    return choice_3

### Routine to record if you press the space bar late and do not win the MID play option ###
def press_late(win, trialClock):
    response = 0
    RT_late = 0
    choice_4 = 0
    # record responses
    theseKeys = event.getKeys(keyList=['space', 'escape'])
    if len(theseKeys) > 0:
        if 'space' in theseKeys:  # pick right
            response = 1
            RT_late = trialClock.getTime()
            win.flip()
        else:  # did not pick
            response = 2
            RT_late = trialClock.getTime()
            win.flip()
    if response == 0:
        response = 2
        RT_late = trialClock.getTime()
    choice_4 = {'late_press': response == 1, 'not_late': response == 2, 'RT_late': RT_late}
    return choice_4

### Get the different step values to indicate the movement of the bars ###
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
        step = difference / 6
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
        step = difference / 6
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

### Progressive movement of the bars arranged in values_change ###
def progressive(win, values_change):
    values_change['step1_barA'].draw()
    values_change['step1_barB'].draw()
    win.flip()
    core.wait(0.2)
    values_change['step2_barA'].draw()
    values_change['step2_barB'].draw()
    win.flip()
    core.wait(0.2)
    values_change['step3_barA'].draw()
    values_change['step3_barB'].draw()
    win.flip()
    core.wait(0.2)
    values_change['step4_barA'].draw()
    values_change['step4_barB'].draw()
    win.flip()
    core.wait(0.2)
    values_change['step5_barA'].draw()
    values_change['step5_barB'].draw()
    win.flip()
    core.wait(0.2)
    values_change['step6_barA'].draw()
    values_change['step6_barB'].draw()
    win.flip()
    core.wait(0.2)
