from __future__ import absolute_import, division
from psychopy import gui, visual, core, event, data, logging, sound
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
import sys  # to get file system encoding
import csv
import random
import time
import Precomm_Helper as helper


########### Basic experiment settings ###########


### Change task set-up for the different environments
# environment options: "A" or "B"
# if ID = even : version A
# if ID = odd : version B
version = "A"

### Store info about the experiment session ###
expName = 'PreComm_Task'  # from the Builder filename that created this script
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = time.strftime("%d%m%Y")  # data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

### Ensure that relative paths start from the same directory as this script ###
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expName, expInfo['participant'], expInfo['date'])

# use an ExperimentHandler to handle saving data
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None, originPath=None,
    savePickle=True, saveWideText=True, dataFileName=filename)

###### Setup the Window #######
win = visual.Window(
    size=(2560, 1440), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
print('measured frame rate: ')
print(expInfo['frameRate'])
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0  # couldn't get a reliable measure so guess

###############################
##### Task-specific setup #####

stimA_name = 'Bookbyte'
stimB_name = 'BookScouter'
stimA_left = visual.ImageStim(win, image='Images/' + stimA_name +'.png', units='height',
                              pos=[-0.45,-0.35], size=[0.4,0.17], name=stimA_name, interpolate=True)
stimB_right = visual.ImageStim(win, image='Images/' + stimB_name +'.png', units='height',
                              pos=[0.45,-0.35], size=[0.4,0.17], name=stimB_name, interpolate=True)


### Static Stimuli that will appear on the screen ###
# stimuli outside loop = stimuli that do not change ###
isi = visual.TextStim(win, text='+')
optionText = visual.TextStim(win=win, text='Wait for New Prices \n             or  \n      Commit Now',
                             height=0.1, pos=[0,0],
                             wrapWidth=8, alignHoriz='center', alignVert='center', ori=0.0)
pickText = visual.TextStim(win, text='Commit', height=0.1)
waitText = visual.TextStim(win, text='Wait', height=0.1)
chooseText = visual.TextStim(win, text=str(stimA_name) + ' or ' + str(stimB_name), height=0.1)
rectangle_A = visual.Rect(win, width=0.5, height=1.6, autoLog=None, fillColor=[-0.7, -0.7, -0.7], pos=[-0.5, -0.2])
rectangle_B = visual.Rect(win, width=0.5, height=1.6, autoLog=None, fillColor=[-0.7, -0.7, -0.7], pos=[0.5, -0.2])
outline_barA = visual.Rect(win, width=0.2, height=0.8, lineWidth=3, autoLog=None, pos=[-0.5, 0.3])
outline_barB = visual.Rect(win, width=0.2, height=0.8,lineWidth=3, autoLog=None, pos=[0.5, 0.3])
change_values = visual.TextStim(win, text='values change', height=0.1, pos=[0,0],
                                wrapWidth=10)
Final_value = visual.TextStim(win, text='new values', height=0.1)
attempt = visual.TextStim(win, text='ready')
highlight_A = visual.Rect(win, width=0.65, height=1.9, lineWidth=5, lineColor=[1,-1,-1], autoLog=None, pos=[-0.5, 0])
highlight_B = visual.Rect(win, width=0.65, height=1.9, lineWidth=5, lineColor=[1,-1,-1], autoLog=None, pos=[0.5, 0])
rewardtext = visual.TextStim(win, text='$0.25', height=0.1)
miss = visual.TextStim(win, text='missed', height=0.1)
tomorrow = visual.TextStim(win, text='Updated Prices', height=0.1)
choosen = visual.TextStim(win, text='One Website was \n Picked for You', height=0.1, wrapWidth=6)
got_it = visual.TextStim(win, text='hit', height=0.1)


###### set clocks #######
# create clock and timer
globalClock = core.Clock()  # this tracks all of the time of the experiment
trialClock = core.Clock()


### Task parameters ####
nTrials = 36  # number of trials in first block
n2Trials = 36  # number of trials in second block
rewardAmount = 0  # cumulative reward amount
response = 0
length = 0.3  # starting value for the MID box portion
increase = 0.05
# amount of stimuli that form the basis for d and c combinations
split_alphabet_A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',  'aa', 'bb', 'cc', 'dd',
                'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'aaa', 'bbb', 'ccc', 'ddd','eee', 'fff',
                'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll']
split_alphabet_B = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',  'aa', 'bb', 'cc', 'dd',
                'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'aaa', 'bbb', 'ccc', 'ddd','eee', 'fff',
                'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll']
##############################
###### Begin experiment ######
##############################

#Start with the welcome screen 
start = visual.TextStim(win, text= '            Welcome! \nPress ENTER to begin task', height= 0.1,
                        pos=[0, 0], wrapWidth=10, alignHoriz='center')
start.draw()
win.flip()
event.waitKeys(keyList=['return'])
globalClock.reset()

#begin trial loop 
for trialIdx in range(nTrials):
    # allow escape experiment (this will be demonstrated throughout the experiment)
    if event.getKeys(keyList='escape'):
        core.quit()
    # clear events from previous trial/ prevents a click from the previous trial to be counted on this trial
    event.clearEvents()
    trialClock.reset()
    # RT variables that need to be zeroed out each trial
    RT_choice = 0  # RT for decision to either precommit or wait
    RT_play = 0  # RT to press space in play condition on mid_clock (from square onset)
    RT_precomm = 0  # RT for decision of either left or right in commit clock
    RT_late = 0  # RT to press space if late in play condition on trial_clock (from initial trial onset)
    RT_trialClock_play = 0  # RT to press space in play condition on trial_clock (from initial trial onset)
    # amount of money you will earn on this trial
    cents = 0
    loosing_win = 0   # if you loose MID but get money
    # variables for record keeping (will be in csv file)
    blank = str(length)  # amount of time the white square is on the screen
    isi_time = 0 # isi interval changes each trial
    lost_type = 0  # if you get endA or endB if you fail in the play condition
    space = 0  # if press space during MID time
    no_space = 0  # if do not press space during MID
    # start with the cross before each trial
    isi.draw()
    win.flip()
    core.wait(1)
    if event.getKeys(keyList='escape'):
        core.quit()
    # pick the book cover image to appear on the screen
    cover_number = random.choice(range(1, 99, 1))
    book = visual.ImageStim(win, image='Books/' + str(cover_number) + '.png', units='height',
                            pos=[0, 0], size=[0.4, 0.8], interpolate=True)
    book.draw()
    win.flip()
    core.wait(2)
    if event.getKeys(keyList='escape'):
        core.quit()
    # start with the cross before each trial
    isi.draw()
    win.flip()
    core.wait(1)
    # pick options from helper for this trial
    if version == "A":
        optionValues = helper.better_wait_values(split_alphabet_A)
        # remove the value (c/d combination) that was chosen for this trial
        split_alphabet_A.remove(optionValues['letter'])
    if version == "B":
        optionValues = helper.better_commit_values(split_alphabet_B)
         # remove the value (c/d combination) that was chosen for this trial
        split_alphabet_B.remove(optionValues['letter'])
    # stimuli that need to change for each trial
    # option A is on the left side of screen
    pickoptionA = visual.TextStim(win=win, text=optionValues['optionA'], name='optionA',
                                  pos=[-0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    # option B is on the right side of screen
    pickoptionB = visual.TextStim(win=win, text=optionValues['optionB'], name='optionB',
                                  pos=[0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    endoptionA = visual.TextStim(win=win, text=optionValues['endA'], name='endA',
                                 pos=[-0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    endoptionB = visual.TextStim(win=win, text=optionValues['endB'], name='endB',
                                 pos=[0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    # prepare to start routine "pick options"
    value_bars = helper.visual_bars(win, optionValues)
    if event.getKeys(keyList='escape'):
        core.quit()
    # Draw the trial screen
    optionText.draw()
    outline_barA.setAutoDraw(True)
    outline_barB.setAutoDraw(True)
    value_bars['option_barA'].setAutoDraw(True)
    value_bars['option_barB'].setAutoDraw(True)
    pickoptionA.setAutoDraw(True)
    pickoptionB.setAutoDraw(True)
    stimA_left.setAutoDraw(True)
    stimB_right.setAutoDraw(True)
    win.flip()
    core.wait(1.5)
    # pick options routine
    pickChoice = helper.pickoptions(win, trialClock)
    RT_choice = pickChoice['RT_choice']
    # allow escape experiment
    if event.getKeys(keyList='escape'):
        core.quit()
    # if choose to play ('wait') on this trial
    if pickChoice['wait']:
        # screen to show that play was chosen
        choice = 'wait'
        waitText.draw()
        win.flip()
        core.wait(1.5)
        # start play routine with fixation cross
        isi.draw()
        win.flip()
        core.wait(1)
        # show the values changing to the new values first
        change_values.draw()
        win.flip()
        core.wait(0.5)
        value_bars['option_barA'].setAutoDraw(False)
        value_bars['option_barB'].setAutoDraw(False)
        pickoptionA.setAutoDraw(False)
        pickoptionB.setAutoDraw(False)
        # show the values change in bar
        values_change = helper.values_change(win, optionValues)
        # show progressive change of values
        bars_change = helper.progressive(win, values_change)
        if event.getKeys(keyList='escape'):
            core.quit()
        # show the final values and the one that you earn on this trial
        values_change['step6_barA'].setAutoDraw(True)
        values_change['step6_barB'].setAutoDraw(True)
        Final_value.draw()
        endoptionA.setAutoDraw(True)
        endoptionB.setAutoDraw(True)
        if event.getKeys(keyList='escape'):
            core.quit()
        win.flip()
        core.wait(1.5)
        attempt.draw()  # wait screen that will say "ready"
        win.flip()
        core.wait(2)
        if event.getKeys(keyList='escape'):
            core.quit()
        # pick the amount of time the fixation cross will be on the screen before white square
        timing_list = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
        isi_time = random.choice(timing_list)
        isi.draw()
        win.flip()
        core.wait(isi_time)
        # run the mid routine
        play_mid = helper.play_mid(win, trialClock, length)
        RT_play = play_mid['RT_play']
        RT_trialClock_play = play_mid['RT_trialClock_play']
        space = play_mid['press_hit']
        no_space = play_mid['press_miss']
        win.flip()
        core.wait(1)
        # allow escape experiment
        if event.getKeys(keyList='escape'):
            core.quit()
        # if hit the white square in the allocated time
        if play_mid['hit']:
            response = 'hit'
            if event.getKeys(keyList='escape'):
                core.quit()
            # remove time of the length if you get a hit
            length -= increase
            # tell them that it was a hit
            got_it.draw()
            win.flip()
            core.wait(1)
            # now have the ability to choose which one they want
            chooseText.draw()
            win.flip()
            core.wait(2)
            hit_pick = helper.hit_pick(win, trialClock)
            RT_hitChoice = hit_pick['RT_hitChoice']
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
            # if choose second B
            if hit_pick['B']:  # if choose the end B option after winning
                response = 'hit_pickB'
                if event.getKeys(keyList='escape'):
                    core.quit()
                cents = optionValues['endB']
                highlight_B.setAutoDraw(True)
                win.flip()
                core.wait(0.5)
                reward_amountB = str(optionValues['endB'])
                # show on the screen the amount that you earned
                winning_textB = visual.TextStim(win, text='     Get \n' + str(reward_amountB) + ' points!',
                                                wrapWidth=4, height=0.1, pos=[0, 0])
                # nonstring record for the cumulative reward amount record
                money = optionValues['endB']
                winning_textB.draw()
                win.flip()
                core.wait(2)
                # clear the screen
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                highlight_B.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
            elif hit_pick['A']:  # if choose the end A option after winning
                response = 'hit_pickA'
                if event.getKeys(keyList='escape'):
                    core.quit()
                cents = optionValues['endA']
                highlight_A.setAutoDraw(True)
                win.flip()
                core.wait(0.5)
                reward_amountA = str(optionValues['endA'])
                # show on the screen the amount that you earned
                winning_textA = visual.TextStim(win, text='     Get \n' + str(reward_amountA) + ' points!',
                                                wrapWidth=4, height=0.1, pos=[0, 0])
                # nonstring record for the cumulative reward amount record
                money = optionValues['endA']
                winning_textA.draw()
                win.flip()
                core.wait(2)
                # clear the screen
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                highlight_A.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
            elif hit_pick['miss']:  # if did not pick an option after winning
                response = 'hit_pick_miss'
                if event.getKeys(keyList='escape'):
                    core.quit()
                cents = 0
                win.flip()
                core.wait(1)
                miss.draw()
                win.flip()
                core.wait(1)
                miss_text = visual.TextStim(win, text='Receive no Points', height=0.1, pos=[0, 0])
                miss_text.draw()
                money = 0
                win.flip()
                core.wait(1)
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
        elif play_mid['miss']:  # if do not pick within the allowed time (you "lost" the game)
            response = 'miss'
            # increase the amount of time the white square will be on the screen next time
            length += increase
            # start the press_late routine to see if tried but pressed late
            press_late = helper.press_late(win, trialClock)
            RT_late = press_late['RT_late']
            win.flip()
            # if you loose the game, one of the two options will be randomly chosen
            potentials = [optionValues['endA'], optionValues['endB']]
            loosing_win = random.choice(potentials)
            # indicate on the screen that you did not hit
            miss.draw()
            win.flip()
            core.wait(1)
            # calculate the amount of money that will be earned if you lost
            cents = loosing_win
            win.flip()
            core.wait(2)
            # indicate that one is chosen for you
            choosen.draw()
            win.flip()
            core.wait(1)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
            # the next two division loops vary based on which of the two end options were randomly chosen for you
            if loosing_win == optionValues['endA']:
                lost_type = 'endA'
                cents = optionValues['endA']
                win.flip()
                core.wait(0.5)
                # highlight the option that you got
                highlight_A.setAutoDraw(True)
                win.flip()
                core.wait(2)
                reward_amountA = str(optionValues['endA'])
                # show on the screen the amount that you earned
                winning_textA = visual.TextStim(win, text='     Get \n' + str(reward_amountA) + ' points!',
                                                    wrapWidth=4, height=0.1, pos=[0,0])
                winning_textA.draw()
                # nonstring record for the cumulative reward amount record
                money = optionValues['endA']
                win.flip()
                core.wait(1)
                # clear the screen
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                highlight_A.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
            elif loosing_win == optionValues['endB']:
                lost_type = 'endB'
                cents = optionValues['endB']
                win.flip()
                core.wait(0.5)
                # highlight the option that you got
                highlight_B.setAutoDraw(True)
                win.flip()
                core.wait(2)
                reward_amountB = str(optionValues['endB'])
                # show on the screen the amount that you earned
                winning_textB = visual.TextStim(win, text='     Get \n' + str(reward_amountB) + ' points!',
                                               wrapWidth=4, height=0.1, pos=[0, 0])
                winning_textB.draw()
                # nonstring record for the cumulative reward amount record
                money = optionValues['endB']
                win.flip()
                core.wait(1)
                # clear the screen
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                highlight_B.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
    # if choose to precommit on this trial
    elif pickChoice['commit']:
        # indicate that pick was chosen for this trial
        choice = 'commit'
        if event.getKeys(keyList='escape'):
            core.quit()
        # indicate that you choose to commit
        pickText.draw()
        win.flip()
        core.wait(1.5)
        # state the two stimuli (websites) that you are picking between
        chooseText.draw()
        win.flip()
        core.wait(1.5)
        # run the pick (precommitment) routine from helper to record options chosen
        precomm = helper.precomm_pick(win, trialClock)
        RT_precomm = precomm['RT_precomm']
        # allow escape experiment
        if event.getKeys(keyList='escape'):
            core.quit()
        if precomm['B']: # if choose to precommit to the B option
            response = 'precomm_B'
            if event.getKeys(keyList='escape'):
                core.quit()
            cents = optionValues['endB']
            win.flip()
            core.wait(0.5)
            # remove the option values
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            # highlight that you choose to commit to B
            highlight_B.setAutoDraw(True)
            # show progressive change of values
            values_change = helper.values_change(win, optionValues)
            bars_change = helper.progressive(win, values_change)
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            win.flip()
            core.wait(1.8)
            reward_amountB = str(optionValues['endB'])
            # show on the screen the amount that you earned
            winning_textB = visual.TextStim(win, text='     Get \n' + str(reward_amountB) + ' points!',
                                            height=0.1, pos=[0, 0])
            winning_textB.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            # nonstring record for the cumulative reward amount record
            money = optionValues['endB']
            win.flip()
            core.wait(1)
            # clear the screen
            highlight_B.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
        elif precomm['A']: # if choose to precommit to the right option
            response = 'precomm_A'
            if event.getKeys(keyList='escape'):
                core.quit()
            cents = optionValues['endA']
            win.flip()
            core.wait(0.5)
            # remove the option values
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            # highlight that you choose to commit to A
            highlight_A.setAutoDraw(True)
            win.flip()
            # show progressive change of values
            values_change = helper.values_change(win, optionValues)
            bars_change = helper.progressive(win, values_change)
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            win.flip()
            core.wait(1.8)
            reward_amountA = str(optionValues['endA'])
            # show on the screen the amount that you earned
            winning_textA = visual.TextStim(win, text='     Get  \n' + str(reward_amountA) + ' points!',
                                            height=0.1, pos=[0, 0])
            winning_textA.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            # nonstring record for the cumulative reward amount record
            money = optionValues['endA']
            win.flip()
            core.wait(1)
            # clear the screen
            highlight_A.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
        # if you fail to pick one of the options after choosing to precommit
        elif precomm['miss']:
            if event.getKeys(keyList='escape'):
                core.quit()
            response = 'precomm_miss'
            miss.draw()
            win.flip()
            core.wait(1.5)
            cents = 0
            miss_text = visual.TextStim(win, text='Received no money', height=0.1, pos=[0, 0])
            miss_text.draw()
            money = 0
            win.flip()
            core.wait(1)
            # clear the screen
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
    # if you missed choosing to either pick or play
    elif pickChoice['miss']:
        choice = 'miss'
        miss.draw()
        if event.getKeys(keyList='escape'):
            core.quit()
        win.flip()
        core.wait(1.5)
        cents = 0
        miss_text = visual.TextStim(win, text='Received no money', height=0.1, pos=[0, 0])
        miss_text.draw()
        money = 0
        win.flip()
        core.wait(1)
        # clear the screen
        value_bars['option_barA'].setAutoDraw(False)
        value_bars['option_barB'].setAutoDraw(False)
        pickoptionA.setAutoDraw(False)
        pickoptionB.setAutoDraw(False)
        stimA_left.setAutoDraw(False)
        stimB_right.setAutoDraw(False)
        outline_barA.setAutoDraw(False)
        outline_barB.setAutoDraw(False)
        # allow escape experiment
        if event.getKeys(keyList='escape'):
            core.quit()
    # update earnings
    rewardAmount += money
    print(rewardAmount)

    # log data
    thisExp.addData('TrialNumber', trialIdx+1)
    thisExp.addData('OptionA', optionValues['optionA'])
    thisExp.addData('OptionB', optionValues['optionB'])
    thisExp.addData('EndA', optionValues['endA'])
    thisExp.addData('EndB', optionValues['endB'])
    thisExp.addData('letter', optionValues['letter'])
    thisExp.addData('difference', optionValues['difference'])
    thisExp.addData('change', optionValues['change'])
    thisExp.addData('A_alwaysBest', optionValues['A_always'])
    thisExp.addData('B_alwaysBest', optionValues['B_always'])
    thisExp.addData('Best_changes', optionValues['changes'])
    thisExp.addData('Choice_RT', RT_choice)
    thisExp.addData('Choice_Wait', choice == 'wait')
    thisExp.addData('Choice_Commit', choice == 'commit')
    thisExp.addData('Choice_Miss', choice == 'miss')
    thisExp.addData('Press_hit', space)
    thisExp.addData('Play_RT', RT_play)
    thisExp.addData('RT_trialClock_play', RT_trialClock_play)
    thisExp.addData('ITI_play', isi_time)
    thisExp.addData('Square_timing', blank)
    thisExp.addData('Press_miss', no_space)
    thisExp.addData('Play_win_A', response == 'hit_pickA')
    thisExp.addData('Play_win_B', response == 'hit_pickB')
    thisExp.addData('Late_RT', RT_late)
    thisExp.addData('Play_lost', response == 'lost_game')
    thisExp.addData('Play_lost_chosenA', lost_type == 'endA')
    thisExp.addData('Play_lost_chosenB', lost_type == 'endB')
    thisExp.addData('Precomm_RT', RT_precomm)
    thisExp.addData('Precomm_B', response == 'precomm_B')
    thisExp.addData('Precomm_A', response == 'precomm_A')
    thisExp.addData('Precomm_miss', response == 'precomm_miss')
    thisExp.addData('Earnings', money)
    thisExp.nextEntry()
# end of trial loop

# Eng of first loop break
half = visual.TextStim(win, text= '            Break \nPress ENTER to continue', height= 0.1,
                        pos=[0, 0], wrapWidth=10, alignHoriz='center')
half.draw()
win.flip()
event.waitKeys(keyList=['return'])
globalClock.reset()

#begin trial loop
for trialIdx in range(n2Trials):
    # allow escape experiment (this will be demonstrated throughout the experiment)
    if event.getKeys(keyList='escape'):
        core.quit()
    # clear events from previous trial/ prevents a click from the previous trial to be counted on this trial
    event.clearEvents()
    trialClock.reset()
    # RT variables that need to be zeroed out each trial
    RT_choice = 0  # RT for decision to either precommit or wait
    RT_play = 0  # RT to press space in play condition on mid_clock (from square onset)
    RT_precomm = 0  # RT for decision of either left or right in commit clock
    RT_late = 0  # RT to press space if late in play condition on trial_clock (from initial trial onset)
    RT_trialClock_play = 0  # RT to press space in play condition on trial_clock (from initial trial onset)
    # amount of money you will earn on this trial
    cents = 0
    loosing_win = 0   # if you loose MID but get money
    # variables for record keeping (will be in csv file)
    blank = str(length)  # amount of time the white square is on the screen
    isi_time = 0 # isi interval changes each trial
    lost_type = 0  # if you get endA or endB if you fail in the play condition
    space = 0  # if press space during MID time
    no_space = 0  # if do not press space during MID
    # start with the cross before each trial
    isi.draw()
    win.flip()
    core.wait(1)
    if event.getKeys(keyList='escape'):
        core.quit()
    # pick the book cover image to appear on the screen
    cover_number = random.choice(range(1, 99, 1))
    book = visual.ImageStim(win, image='Books/' + str(cover_number) + '.png', units='height',
                            pos=[0, 0], size=[0.4, 0.8], interpolate=True)
    book.draw()
    win.flip()
    core.wait(2)
    if event.getKeys(keyList='escape'):
        core.quit()
    # start with the cross before each trial
    isi.draw()
    win.flip()
    core.wait(1)
    # pick options from helper for this trial
    if version == "A":
        optionValues = helper.better_commit_values(split_alphabet_B)
        # remove the value (c/d combination) that was chosen for this trial
        split_alphabet_B.remove(optionValues['letter'])
    if version == "B":
        optionValues = helper.better_wait_values(split_alphabet_A)
        # remove the value (c/d combination) that was chosen for this trial
        split_alphabet_A.remove(optionValues['letter'])
    # stimuli that need to change for each trial
    # option A is on the left side of screen
    pickoptionA = visual.TextStim(win=win, text=optionValues['optionA'], name='optionA',
                                  pos=[-0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    # option B is on the right side of screen
    pickoptionB = visual.TextStim(win=win, text=optionValues['optionB'], name='optionB',
                                  pos=[0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    endoptionA = visual.TextStim(win=win, text=optionValues['endA'], name='endA',
                                 pos=[-0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    endoptionB = visual.TextStim(win=win, text=optionValues['endB'], name='endB',
                                 pos=[0.5, -0.3], rgb=None, color=(1, 1, 1), colorSpace='rgb')
    # prepare to start routine "pick options"
    value_bars = helper.visual_bars(win, optionValues)
    if event.getKeys(keyList='escape'):
        core.quit()
    # Draw the trial screen
    optionText.draw()
    outline_barA.setAutoDraw(True)
    outline_barB.setAutoDraw(True)
    value_bars['option_barA'].setAutoDraw(True)
    value_bars['option_barB'].setAutoDraw(True)
    pickoptionA.setAutoDraw(True)
    pickoptionB.setAutoDraw(True)
    stimA_left.setAutoDraw(True)
    stimB_right.setAutoDraw(True)
    win.flip()
    core.wait(1.5)
    # pick options routine
    pickChoice = helper.pickoptions(win, trialClock)
    RT_choice = pickChoice['RT_choice']
    # allow escape experiment
    if event.getKeys(keyList='escape'):
        core.quit()
    # if choose to play ('wait') on this trial
    if pickChoice['wait']:
        # screen to show that play was chosen
        choice = 'wait'
        waitText.draw()
        win.flip()
        core.wait(1.5)
        # start play routine with fixation cross
        isi.draw()
        win.flip()
        core.wait(1)
        # show the values changing to the new values first
        change_values.draw()
        win.flip()
        core.wait(0.5)
        value_bars['option_barA'].setAutoDraw(False)
        value_bars['option_barB'].setAutoDraw(False)
        pickoptionA.setAutoDraw(False)
        pickoptionB.setAutoDraw(False)
        # show the values change in bar
        values_change = helper.values_change(win, optionValues)
        # show progressive change of values
        bars_change = helper.progressive(win, values_change)
        if event.getKeys(keyList='escape'):
            core.quit()
        # show the final values and the one that you earn on this trial
        values_change['step6_barA'].setAutoDraw(True)
        values_change['step6_barB'].setAutoDraw(True)
        Final_value.draw()
        endoptionA.setAutoDraw(True)
        endoptionB.setAutoDraw(True)
        if event.getKeys(keyList='escape'):
            core.quit()
        win.flip()
        core.wait(1.5)
        attempt.draw()  # wait screen that will say "ready"
        win.flip()
        core.wait(2)
        if event.getKeys(keyList='escape'):
            core.quit()
        # pick the amount of time the fixation cross will be on the screen before white square
        timing_list = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
        isi_time = random.choice(timing_list)
        isi.draw()
        win.flip()
        core.wait(isi_time)
        # run the mid routine
        play_mid = helper.play_mid(win, trialClock, length)
        RT_play = play_mid['RT_play']
        RT_trialClock_play = play_mid['RT_trialClock_play']
        space = play_mid['press_hit']
        no_space = play_mid['press_miss']
        win.flip()
        core.wait(1)
        # allow escape experiment
        if event.getKeys(keyList='escape'):
            core.quit()
        # if hit the white square in the allocated time
        if play_mid['hit']:
            response = 'hit'
            if event.getKeys(keyList='escape'):
                core.quit()
            # remove time of the length if you get a hit
            length -= increase
            # tell them that it was a hit
            got_it.draw()
            win.flip()
            core.wait(1)
            # now have the ability to choose which one they want
            chooseText.draw()
            win.flip()
            core.wait(2)
            hit_pick = helper.hit_pick(win, trialClock)
            RT_hitChoice = hit_pick['RT_hitChoice']
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
            # if choose second B
            if hit_pick['B']:  # if choose the end B option after winning
                response = 'hit_pickB'
                if event.getKeys(keyList='escape'):
                    core.quit()
                cents = optionValues['endB']
                highlight_B.setAutoDraw(True)
                win.flip()
                core.wait(0.5)
                reward_amountB = str(optionValues['endB'])
                # show on the screen the amount that you earned
                winning_textB = visual.TextStim(win, text='     Get \n' + str(reward_amountB) + ' points!',
                                                wrapWidth=4, height=0.1, pos=[0, 0])
                # nonstring record for the cumulative reward amount record
                money = optionValues['endB']
                winning_textB.draw()
                win.flip()
                core.wait(2)
                # clear the screen
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                highlight_B.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
            elif hit_pick['A']:  # if choose the end A option after winning
                response = 'hit_pickA'
                if event.getKeys(keyList='escape'):
                    core.quit()
                cents = optionValues['endA']
                highlight_A.setAutoDraw(True)
                win.flip()
                core.wait(0.5)
                reward_amountA = str(optionValues['endA'])
                # show on the screen the amount that you earned
                winning_textA = visual.TextStim(win, text='     Get \n' + str(reward_amountA) + ' points!',
                                                wrapWidth=4, height=0.1, pos=[0, 0])
                # nonstring record for the cumulative reward amount record
                money = optionValues['endA']
                winning_textA.draw()
                win.flip()
                core.wait(2)
                # clear the screen
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                highlight_A.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
            elif hit_pick['miss']:  # if did not pick an option after winning
                response = 'hit_pick_miss'
                if event.getKeys(keyList='escape'):
                    core.quit()
                cents = 0
                win.flip()
                core.wait(1)
                miss.draw()
                win.flip()
                core.wait(1)
                miss_text = visual.TextStim(win, text='Receive no Points', height=0.1, pos=[0, 0])
                miss_text.draw()
                money = 0
                win.flip()
                core.wait(1)
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
        elif play_mid['miss']:  # if do not pick within the allowed time (you "lost" the game)
            response = 'miss'
            # increase the amount of time the white square will be on the screen next time
            length += increase
            # start the press_late routine to see if tried but pressed late
            press_late = helper.press_late(win, trialClock)
            RT_late = press_late['RT_late']
            win.flip()
            # if you loose the game, one of the two options will be randomly chosen
            potentials = [optionValues['endA'], optionValues['endB']]
            loosing_win = random.choice(potentials)
            # indicate on the screen that you did not hit
            miss.draw()
            win.flip()
            core.wait(1)
            # calculate the amount of money that will be earned if you lost
            cents = loosing_win
            win.flip()
            core.wait(2)
            # indicate that one is chosen for you
            choosen.draw()
            win.flip()
            core.wait(1)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
            # the next two division loops vary based on which of the two end options were randomly chosen for you
            if loosing_win == optionValues['endA']:
                lost_type = 'endA'
                cents = optionValues['endA']
                win.flip()
                core.wait(0.5)
                # highlight the option that you got
                highlight_A.setAutoDraw(True)
                win.flip()
                core.wait(2)
                reward_amountA = str(optionValues['endA'])
                # show on the screen the amount that you earned
                winning_textA = visual.TextStim(win, text='     Get \n' + str(reward_amountA) + ' points!',
                                                    wrapWidth=4, height=0.1, pos=[0,0])
                winning_textA.draw()
                # nonstring record for the cumulative reward amount record
                money = optionValues['endA']
                win.flip()
                core.wait(1)
                # clear the screen
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                highlight_A.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
            elif loosing_win == optionValues['endB']:
                lost_type = 'endB'
                cents = optionValues['endB']
                win.flip()
                core.wait(0.5)
                # highlight the option that you got
                highlight_B.setAutoDraw(True)
                win.flip()
                core.wait(2)
                reward_amountB = str(optionValues['endB'])
                # show on the screen the amount that you earned
                winning_textB = visual.TextStim(win, text='     Get \n' + str(reward_amountB) + ' points!',
                                               wrapWidth=4, height=0.1, pos=[0, 0])
                winning_textB.draw()
                # nonstring record for the cumulative reward amount record
                money = optionValues['endB']
                win.flip()
                core.wait(1)
                # clear the screen
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                values_change['step6_barA'].setAutoDraw(False)
                values_change['step6_barB'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                highlight_B.setAutoDraw(False)
                # allow escape experiment
                if event.getKeys(keyList='escape'):
                    core.quit()
    # if choose to precommit on this trial
    elif pickChoice['commit']:
        # indicate that pick was chosen for this trial
        choice = 'commit'
        if event.getKeys(keyList='escape'):
            core.quit()
        # indicate that you choose to commit
        pickText.draw()
        win.flip()
        core.wait(1.5)
        # state the two stimuli (websites) that you are picking between
        chooseText.draw()
        win.flip()
        core.wait(1.5)
        # run the pick (precommitment) routine from helper to record options chosen
        precomm = helper.precomm_pick(win, trialClock)
        RT_precomm = precomm['RT_precomm']
        # allow escape experiment
        if event.getKeys(keyList='escape'):
            core.quit()
        if precomm['B']: # if choose to precommit to the B option
            response = 'precomm_B'
            if event.getKeys(keyList='escape'):
                core.quit()
            cents = optionValues['endB']
            win.flip()
            core.wait(0.5)
            # remove the option values
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            # highlight that you choose to commit to B
            highlight_B.setAutoDraw(True)
            # show progressive change of values
            values_change = helper.values_change(win, optionValues)
            bars_change = helper.progressive(win, values_change)
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            win.flip()
            core.wait(1.8)
            reward_amountB = str(optionValues['endB'])
            # show on the screen the amount that you earned
            winning_textB = visual.TextStim(win, text='     Get \n' + str(reward_amountB) + ' points!',
                                            height=0.1, pos=[0, 0])
            winning_textB.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            # nonstring record for the cumulative reward amount record
            money = optionValues['endB']
            win.flip()
            core.wait(1)
            # clear the screen
            highlight_B.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
        elif precomm['A']: # if choose to precommit to the right option
            response = 'precomm_A'
            if event.getKeys(keyList='escape'):
                core.quit()
            cents = optionValues['endA']
            win.flip()
            core.wait(0.5)
            # remove the option values
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            # highlight that you choose to commit to A
            highlight_A.setAutoDraw(True)
            win.flip()
            # show progressive change of values
            values_change = helper.values_change(win, optionValues)
            bars_change = helper.progressive(win, values_change)
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            win.flip()
            core.wait(1.8)
            reward_amountA = str(optionValues['endA'])
            # show on the screen the amount that you earned
            winning_textA = visual.TextStim(win, text='     Get  \n' + str(reward_amountA) + ' points!',
                                            height=0.1, pos=[0, 0])
            winning_textA.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            # nonstring record for the cumulative reward amount record
            money = optionValues['endA']
            win.flip()
            core.wait(1)
            # clear the screen
            highlight_A.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
        # if you fail to pick one of the options after choosing to precommit
        elif precomm['miss']:
            if event.getKeys(keyList='escape'):
                core.quit()
            response = 'precomm_miss'
            miss.draw()
            win.flip()
            core.wait(1.5)
            cents = 0
            miss_text = visual.TextStim(win, text='Received no money', height=0.1, pos=[0, 0])
            miss_text.draw()
            money = 0
            win.flip()
            core.wait(1)
            # clear the screen
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
            # allow escape experiment
            if event.getKeys(keyList='escape'):
                core.quit()
    # if you missed choosing to either pick or play
    elif pickChoice['miss']:
        choice = 'miss'
        miss.draw()
        if event.getKeys(keyList='escape'):
            core.quit()
        win.flip()
        core.wait(1.5)
        cents = 0
        miss_text = visual.TextStim(win, text='Received no money', height=0.1, pos=[0, 0])
        miss_text.draw()
        money = 0
        win.flip()
        core.wait(1)
        # clear the screen
        value_bars['option_barA'].setAutoDraw(False)
        value_bars['option_barB'].setAutoDraw(False)
        pickoptionA.setAutoDraw(False)
        pickoptionB.setAutoDraw(False)
        stimA_left.setAutoDraw(False)
        stimB_right.setAutoDraw(False)
        outline_barA.setAutoDraw(False)
        outline_barB.setAutoDraw(False)
        # allow escape experiment
        if event.getKeys(keyList='escape'):
            core.quit()
    # update earnings
    rewardAmount += money
    print(rewardAmount)

    # log data
    thisExp.addData('TrialNumber', trialIdx+1)
    thisExp.addData('OptionA', optionValues['optionA'])
    thisExp.addData('OptionB', optionValues['optionB'])
    thisExp.addData('EndA', optionValues['endA'])
    thisExp.addData('EndB', optionValues['endB'])
    thisExp.addData('letter', optionValues['letter'])
    thisExp.addData('difference', optionValues['difference'])
    thisExp.addData('change', optionValues['change'])
    thisExp.addData('A_alwaysBest', optionValues['A_always'])
    thisExp.addData('B_alwaysBest', optionValues['B_always'])
    thisExp.addData('Best_changes', optionValues['changes'])
    thisExp.addData('Choice_RT', RT_choice)
    thisExp.addData('Choice_Wait', choice == 'wait')
    thisExp.addData('Choice_Commit', choice == 'commit')
    thisExp.addData('Choice_Miss', choice == 'miss')
    thisExp.addData('Press_hit', space)
    thisExp.addData('Play_RT', RT_play)
    thisExp.addData('RT_trialClock_play', RT_trialClock_play)
    thisExp.addData('ITI_play', isi_time)
    thisExp.addData('Square_timing', blank)
    thisExp.addData('Press_miss', no_space)
    thisExp.addData('Play_win_A', response == 'hit_pickA')
    thisExp.addData('Play_win_B', response == 'hit_pickB')
    thisExp.addData('Late_RT', RT_late)
    thisExp.addData('Play_lost', response == 'lost_game')
    thisExp.addData('Play_lost_chosenA', lost_type == 'endA')
    thisExp.addData('Play_lost_chosenB', lost_type == 'endB')
    thisExp.addData('Precomm_RT', RT_precomm)
    thisExp.addData('Precomm_B', response == 'precomm_B')
    thisExp.addData('Precomm_A', response == 'precomm_A')
    thisExp.addData('Precomm_miss', response == 'precomm_miss')
    thisExp.addData('Earnings', money)
    thisExp.nextEntry()
# end of trial loop


# show earnings on entire block (divided by 4 for better money earnings)
# allow escape experiment
if event.getKeys(keyList='escape'):
    core.quit()
money_value = round(str((rewardAmount/100.00)/4))
moneyontrial= visual.TextStim(win, text='            Checkout. \n   You received $' + money_value
                                        + '\n for selling your books!', height=0.1)
moneyontrial.draw()
win.flip()
# right now need to press enter to end the experiment
event.waitKeys(keyList=['return'])


###########################
##### Close-out steps #####

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()

# end the experiment
thisExp.abort()
# close the window
win.close()
# end the experiment
core.quit()