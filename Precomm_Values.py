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
import Precomm_Task as task

def new_values():
    from task import letter
    if task[letter] == 'a':
        d = 4
        c = +3
        print('optionA')
    if task[letter] == 'b':
        d = 4
        c = -3
        print('optionB')
    if task[letter] == 'c':
        d = 4
        c = +9
        print('optionC')
    if task[letter] == 'd':
        d = 4
        c = -9
        print('optionD')
    if task[letter] == 'e':
        d = 4
        c = +13
        print('optionE')
    if task[letter] == 'f':
        d = 4
        c = -13
        print('optionF')
    if task[letter] == 'g':
        d = 12
        c = +3
        print('optionG')
    if task[letter] == 'h':
        d = 12
        c = -3
        print('optionH')
    if task[letter] == 'i':
        d = 12
        c = +9
        print('optionI')
    if task[letter] == 'j':
        d = 12
        c = -9
        print('optionJ')
    if task[letter] == 'k':
        d = 12
        c = +13
        print('optionK')
    if task[letter] == 'l':
        d = 12
        c = -13
        print('optionL')
    if task[letter] == 'm':
        d = 20
        c = +3
        print('optionM')
    if task[letter] == 'n':
        d = 20
        c = -3
        print('optionN')
    if task[letter] == 'o':
        d = 20
        c = +9
        print('optionO')
    if task[letter] == 'p':
        d = 20
        c = -9
        print('optionP')
    if task[letter] == 'q':
        d = 20
        c = +13
        print('optionQ')
    if task[letter] == 'r':
        d = 20
        c = -13
        print('optionR')
    if task[letter] == 's':
        d = 28
        c = +3
        print('optionS')
    if task[letter] == 't':
        d = 28
        c = -3
        print('optionT')
    if task[letter] == 'u':
        d = 28
        c = +9
        print('optionU')
    if task[letter] == 'v':
        d = 28
        c = -9
        print('optionV')
    if task[letter] == 'w':
        d = 28
        c = +13
        print('optionW')
    if task[letter] == 'x':
        d = 28
        c = -13
        print('optionX')

    First_start = random.choice(range(13, 58, 1))
    Second_start = First_start + d
    First_end = First_start + c
    Second_end = Second_start + c
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
    print(A_start)
    print(A_end)
    print(B_start)
    print(B_end)
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
    optionValues = {'optionA': A_start, 'optionB': B_start, 'endA': A_end, 'endB': B_end,
                    'difference': d, 'change': c,
                    'A_always': change == 1, 'B_always': change == 2, 'changes': change == 3}
    return optionValues
