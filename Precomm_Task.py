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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
                              pos=[-0.4,-0.35], size=[0.45,0.2], name=stimA_name, interpolate=True)
stimB_right = visual.ImageStim(win, image='Images/' + stimB_name +'.png', units='height',
                              pos=[0.4,-0.35], size=[0.45,0.2], name=stimB_name, interpolate=True)


## Word Stimuli ##
# stimuli outside loop = stimuli that do not change ###
isi = visual.TextStim(win, text='+')
optionText = visual.TextStim(win=win, text='  Play \n    or  \n Commit', height=0.1,
                             pos=[0, 0], alignHoriz='center')
pickText = visual.TextStim(win, text='Commit', height=0.1)
playText = visual.TextStim(win, text='Play', height=0.1)
chooseText = visual.TextStim(win, text=str(stimA_name) + ' or ' + str(stimB_name), height=0.1)
rectangle_A = visual.Rect(win, width=0.5, height=1.3, autoLog=None, fillColor=[-0.7, -0.7, -0.7], pos=[-0.5, -0.2])
rectangle_B = visual.Rect(win, width=0.5, height=1.3, autoLog=None, fillColor=[-0.7, -0.7, -0.7], pos=[0.5, -0.2])
outline_barA = visual.Rect(win, width=0.2, height=0.8, lineWidth=3, autoLog=None, pos=[-0.5, 0.3])
outline_barB = visual.Rect(win, width=0.2, height=0.8,lineWidth=3, autoLog=None, pos=[0.5, 0.3])
looseText = visual.TextStim(win, text='loose', height=0.1)
values_change = visual.TextStim(win, text='Values Change', height=0.1)
Final_value = visual.TextStim(win, text='Final Values', height=0.1)
highlight_A = visual.Rect(win, width=0.6, height=1.9, lineWidth=5, lineColor=[1,-1,-1], autoLog=None, pos=[-0.5, 0])
highlight_B = visual.Rect(win, width=0.6, height=1.9, lineWidth=5, lineColor=[1,-1,-1], autoLog=None, pos=[0.5, 0])
rewardtext = visual.TextStim(win, text='$0.25', height=0.1)
miss = visual.TextStim(win, text='miss', height=0.1)
choosen = visual.TextStim(win, text='One website was \n picked for you', height = 0.1)
got_it = visual.TextStim(win, text='hit', height=0.1)
lost = visual.TextStim(win, text='missed', height = 0.1,
                       pos=[0, 0], alignHoriz='center')


###### set clocks #######
# create clock and timer
globalClock = core.Clock()  # this tracks all of the time of the experiment
trialClock = core.Clock()


### Task parameters ####
nTrials = 5  # number of trials per block
rewardAmount = 0  # cumulative reward amount
response = 0
length = 0

##############################
###### Begin experiment ######
##############################

#Start with the welcome screen 
start = visual.TextStim(win, text= '            Welcome! \nPress ENTER to begin task', height= 0.1,
                        pos=[0, 0], alignHoriz='center')
start.draw()
win.flip()
event.waitKeys(keyList=['return'])
globalClock.reset()

#begin trial loop 
for trialIdx in range(nTrials):
    #allow escape experiment
    if event.getKeys(keyList='escape'):
        core.quit()
    # clear events from previous trial/ prevents a click from the previous trial to be counted on this trial
    event.clearEvents()
    trialClock.reset()
    RT_choice = 0
    RT_play = 0
    RT_precomm = 0
    RT_late = 0
    RT_trialClock_play = 0
    win_or_loose = 0
    lost_type = 0
    # start with the cross before each trial
    isi.draw()
    win.flip()
    core.wait(1)
    # track the reward value for each particular trial
    cents = 0
    loosing_win = 0   # amount of money you earn when you play but loose (randomly chosen amount)
    # pick options from helper for this trial
    optionValues = helper.pickvalues()
    # stimuli that need to change for each trial
    # option A is on the left side of screen
    pickoptionA = visual.TextStim(win=win, text=optionValues['optionA'], name='optionA',
                                  pos = [-0.5,-0.3], rgb= None, color=(1,1,1), colorSpace='rgb')
    # option B is on the right side of screen
    pickoptionB = visual.TextStim(win=win, text=optionValues['optionB'], name='optionB',
                                  pos = [0.5,-0.3], rgb= None, color=(1,1,1), colorSpace='rgb')
    endoptionA = visual.TextStim(win=win, text=optionValues['endA'], name='endA',
                                 pos = [-0.5,-0.3], rgb= None, color=(1,1,1), colorSpace='rgb')
    endoptionB = visual.TextStim(win=win, text=optionValues['endB'], name='endB',
                                 pos = [0.5,-0.3], rgb= None, color=(1,1,1), colorSpace='rgb')
    # prepare to start routine "pick options"
    value_bars = helper.visual_bars(win, optionValues)
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
    if pickChoice['play']:  # if choose to play on this trial
        # screen to show that play was chosen
        choice = 'play'
        pickoptionA.draw()
        pickoptionB.draw()
        playText.draw()
        win.flip()
        core.wait(1.5)
        # start play routine with fixation cross
        isi.draw()
        win.flip()
        core.wait(1)
        outline_barB.setAutoDraw(False)
        outline_barA.setAutoDraw(False)
        value_bars['option_barA'].setAutoDraw(False)
        value_bars['option_barB'].setAutoDraw(False)
        pickoptionA.setAutoDraw(False)
        pickoptionB.setAutoDraw(False)
        stimA_left.setAutoDraw(False)
        stimB_right.setAutoDraw(False)
        outline_barA.setAutoDraw(False)
        outline_barB.setAutoDraw(False)
        # run the routine for responding to the stimulus
        play_mid = helper.play_mid(win, trialClock)
        RT_play = play_mid['RT_play']
        RT_trialClock_play = play_mid['RT_trialClock_play']
        win.flip()
        core.wait(1)
        # start the play routine to record response
        if play_mid['hit']:  # if choose the left option on play
            response = 'hit'
            got_it.draw()
            win.flip()
            core.wait(1)
            # show the values change in bar
            values_change = helper.values_change(win, optionValues)
            outline_barB.setAutoDraw(True)
            outline_barA.setAutoDraw(True)
            stimA_left.setAutoDraw(True)
            stimB_right.setAutoDraw(True)
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
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.setAutoDraw(True)
            value_bars['end_barA'].setAutoDraw(True)
            endoptionB.setAutoDraw(True)
            value_bars['end_barB'].setAutoDraw(True)
            win.flip()
            core.wait(1.8)
            hit_pick = helper.hit_choice(win, trialClock)
            chooseText.draw()
            win.flip()
            core.wait(2)
            if hit_pick['B']:  # if choose to precommit to the left option
                response = 'hit_pick_B'
                cents = optionValues['endB']
                win.flip()
                core.wait(0.5)
                highlight_B.setAutoDraw(True)
                win.flip()
                core.wait(1)
                if cents == optionValues['endB']:  # you earned the B value
                    reward_amountB = str(optionValues['endB'])
                    # show on the screen the amount that you earned
                    winning_textB = visual.TextStim(win, text='You get \n' + str(reward_amountB) + '\n cents',
                                                    height=0.1, pos=[0,0])
                    winning_textB.draw()
                    # nonstring record for the cumulative reward amount record
                    money = optionValues['endB']
                    win.flip()
                    core.wait(1)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                value_bars['end_barA'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                value_bars['end_barB'].setAutoDraw(False)
                highlight_B.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
            if hit_pick['A']:  # if choose to precommit to the left option
                response = 'hit_pick_A'
                cents = optionValues['endA']
                win.flip()
                core.wait(0.5)
                highlight_A.draw()
                win.flip()
                core.wait(1)
                if cents == optionValues['endA']:  # you earned the B value
                    reward_amountA = str(optionValues['endA'])
                    # show on the screen the amount that you earned
                    winning_textA = visual.TextStim(win, text='You get \n' + str(reward_amountA) + '\n cents',
                                                    height=0.1, pos=[0,0])
                    winning_textA.draw()
                    # nonstring record for the cumulative reward amount record
                    money = optionValues['endB']
                    win.flip()
                    core.wait(1)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                value_bars['end_barA'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                value_bars['end_barB'].setAutoDraw(False)
                highlight_A.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
            if hit_pick['miss']:  # if choose to precommit to the left option
                response = 'hit_pick_miss'
                cents = 0
                win.flip()
                core.wait(0.5)
                miss.draw()
                win.flip()
                core.wait(1)
                miss_text = visual.TextStim(win, text='Received no money', height=0.1, pos=[0, 0])
                miss_text.draw()
                money = 0
                win.flip()
                core.wait(1)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                value_bars['end_barA'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                value_bars['end_barB'].setAutoDraw(False)
                highlight_A.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
        elif play_mid['miss']:  # if do not pick within the allowed time (you "lost" the game)
            response = 'miss'
            press_late = helper.press_late(win, trialClock)
            RT_late = press_late['RT_late']
            win.flip()
            potentials = [optionValues['endA'], optionValues['endB']]
            # if you loose the game, one of the two options will be chosen for you
            loosing_win = random.choice(potentials)
            # indicate that you lost
            if press_late['late_A']:
                win_or_loose = 1
                win.flip()
            if press_late['late_B']:
                win_or_loose = 2
                win.flip()
            miss.draw()
            win.flip()
            core.wait(1)
            # calculate the amount of money that will be earned if you lost
            cents = loosing_win
            win.flip()
            values_change = helper.values_change(win, optionValues)
            stimA_left.setAutoDraw(True)
            stimB_right.setAutoDraw(True)
            outline_barB.setAutoDraw(True)
            outline_barA.setAutoDraw(True)
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
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.setAutoDraw(True)
            value_bars['end_barA'].setAutoDraw(True)
            endoptionB.setAutoDraw(True)
            value_bars['end_barB'].setAutoDraw(True)
            win.flip()
            core.wait(1.8)
            choosen.draw()
            win.flip()
            core.wait(1)
            # highlight the random value that was chosen for you if you lost
            if loosing_win == optionValues['endA']:
                lost_type = 'chosen_endA'
                cents = optionValues['endA']
                win.flip()
                core.wait(0.5)
                highlight_A.setAutoDraw(True)
                win.flip()
                if cents == optionValues['endA']:  # you earned the B value
                    reward_amountA = str(optionValues['endA'])
                    # show on the screen the amount that you earned
                    winning_textA = visual.TextStim(win, text='You get \n' + str(reward_amountA) + '\n cents',
                                                    height=0.1, pos=[0,0])
                    winning_textA.draw()
                    # nonstring record for the cumulative reward amount record
                    money = optionValues['endB']
                    win.flip()
                    core.wait(1)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                value_bars['end_barA'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                value_bars['end_barB'].setAutoDraw(False)
                highlight_A.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
            elif loosing_win == optionValues['endB']:
                lost_type = 'chosen_endB'
                cents = optionValues['endB']
                win.flip()
                core.wait(0.5)
                highlight_B.setAutoDraw(True)
                win.flip()
                core.wait(2)
                if cents == optionValues['endB']:  # you earned the B value
                    reward_amountB = str(optionValues['endB'])
                    # show on the screen the amount that you earned
                    winning_textB = visual.TextStim(win, text='You get \n' + str(reward_amountB) + '\n cents',
                                                    height=0.1, pos=[0,0])
                    winning_textB.draw()
                    # nonstring record for the cumulative reward amount record
                    money = optionValues['endB']
                    win.flip()
                    core.wait(1)
                outline_barB.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                endoptionA.setAutoDraw(False)
                value_bars['end_barA'].setAutoDraw(False)
                endoptionB.setAutoDraw(False)
                value_bars['end_barB'].setAutoDraw(False)
                highlight_B.setAutoDraw(False)
                stimA_left.setAutoDraw(False)
                stimB_right.setAutoDraw(False)
                outline_barA.setAutoDraw(False)
                outline_barB.setAutoDraw(False)
    elif pickChoice['pick']: # if choose to precommit on this trial
        # indicate that pick was chosen for this trial
        choice = 'pick'
        pickoptionA.draw()
        pickoptionB.draw()
        pickText.draw()
        win.flip()
        core.wait(1.5)
        # instructions on how to pick
        chooseText.draw()
        pickoptionA.draw()
        pickoptionB.draw()
        win.flip()
        core.wait(1.5)
        # run the pick (precommitment) routine from helper to record options chosen
        precomm = helper.precomm_pick(win, trialClock)
        RT_precomm = precomm['RT_precomm']
        if precomm['B']: # if choose to precommit to the left option
            response = 'precomm_B'
            pickoptionB.draw()
            cents = optionValues['endB']
            win.flip()
            core.wait(0.5)
            # indicate that the values change
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            highlight_B.setAutoDraw(True)
            # show the values change in bar
            values_change = helper.values_change(win, optionValues)
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
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            win.flip()
            core.wait(1.8)
            highlight_B.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
        elif precomm['A']: # if choose to precommit to the right option
            response = 'precomm_A'
            pickoptionA.draw()
            cents = optionValues['endA']
            win.flip()
            core.wait(0.5)
            # indicate that the values change
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            highlight_A.setAutoDraw(True)
            win.flip()
            # show the values change in bar
            values_change = helper.values_change(win, optionValues)
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
            # show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.draw()
            value_bars['end_barA'].draw()
            endoptionB.draw()
            value_bars['end_barB'].draw()
            win.flip()
            core.wait(1.8)
            highlight_A.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
        elif precomm['miss']:
            response = 'precomm_miss'
            miss.draw()
            win.flip()
            core.wait(1.5)
            cents = 0
            value_bars['option_barA'].setAutoDraw(False)
            value_bars['option_barB'].setAutoDraw(False)
            pickoptionA.setAutoDraw(False)
            pickoptionB.setAutoDraw(False)
            stimA_left.setAutoDraw(False)
            stimB_right.setAutoDraw(False)
            outline_barA.setAutoDraw(False)
            outline_barB.setAutoDraw(False)
    elif pickChoice['miss']:  # if missed in choosing to pick or play
        choice = 'miss'
        miss.draw()
        win.flip()
        core.wait(1.5)
        cents = 0
        value_bars['option_barA'].setAutoDraw(False)
        value_bars['option_barB'].setAutoDraw(False)
        pickoptionA.setAutoDraw(False)
        pickoptionB.setAutoDraw(False)
        stimA_left.setAutoDraw(False)
        stimB_right.setAutoDraw(False)
        outline_barA.setAutoDraw(False)
        outline_barB.setAutoDraw(False)
    # show the amount of money earned on this trial
    if cents == optionValues['endA']: # you earned the A value
        reward_amountA = str(optionValues['endA'])
        # show on the screen the amount that you earned
        winning_textA = visual.TextStim(win, text = 'You earned ' +str(reward_amountA)+ ' cents', height = 0.1)
        winning_textA.draw()
        # nonstring record for the cumulative reward amount record
        money = optionValues['endA']
        win.flip()
        core.wait(1)
    if cents == optionValues['endB']: # you earned the B value
        reward_amountB = str(optionValues['endB'])
        # show on the screen the amount that you earned
        winning_textB= visual.TextStim(win, text = 'You earned ' +str(reward_amountB)+ ' cents', height = 0.1)
        winning_textB.draw()
        # nonstring record for the cumulative reward amount record
        money = optionValues['endB']
        win.flip()
        core.wait(1)
    if cents == loosing_win:  # the amount of money you earn if you lost (one or the other)
        reward_amount = str(loosing_win)
        # show on the screen the amount that you earned
        loosing_winning_text = visual.TextStim(win, text = 'You earned ' +str(loosing_win)+ ' cents', height = 0.1)
        loosing_winning_text.draw()
        money = loosing_win
        win.flip()
        core.wait(1)
    # if you receive no money on the trial (forgot to click)
    elif cents == 0:
        money = 0
    # update earnings
    rewardAmount += money

    # log data
    thisExp.addData('TrialNumber', trialIdx+1)
    thisExp.addData('OptionA', optionValues['optionA'])
    thisExp.addData('OptionB', optionValues['optionB'])
    thisExp.addData('EndA', optionValues['endA'])
    thisExp.addData('EndB', optionValues['endB'])
    thisExp.addData('A_difference', optionValues['A_difference'])
    thisExp.addData('B_difference', optionValues['B_difference'])
    thisExp.addData('largest_option',optionValues['max_option'])
    thisExp.addData('largest_end', optionValues['max_end'])
    thisExp.addData('A_alwaysBest', optionValues['A_always'])
    thisExp.addData('B_alwaysBest', optionValues['B_always'])
    thisExp.addData('Best_changes', optionValues['changes'])
    thisExp.addData('Choice_RT', RT_choice)
    thisExp.addData('Choice_Play', choice == 'play')
    thisExp.addData('Choice_Pick', choice == 'pick')
    thisExp.addData('Choice_Miss', choice == 'miss')
    thisExp.addData('Play_RT', RT_play)
    thisExp.addData('RT_trialClock_play', RT_trialClock_play)
    thisExp.addData('Play_win_A', response == 'win_A')
    thisExp.addData('Play_win_B', response == 'win_B')
    thisExp.addData('Late_RT', RT_late)
    thisExp.addData('Play_lost', response == 'lost_game')
    thisExp.addData('Play_lost_chosenA', lost_type == 'chosen_endA')
    thisExp.addData('Play_lost_chosenB', lost_type == 'chosen_endB')
    thisExp.addData('Play_toolate_B', win_or_loose == 1)
    thisExp.addData('Play_toolate_A', win_or_loose == 2)
    thisExp.addData('Precomm_RT', RT_precomm)
    thisExp.addData('Precomm_B', response == 'precomm_B')
    thisExp.addData('Precomm_A', response == 'precomm_A')
    thisExp.addData('Precomm_miss', response == 'precomm_miss')
    thisExp.addData('Earnings', money)
    thisExp.nextEntry()
# end of trial loop


# show earnings on entire block
# allow escape experiment
if event.getKeys(keyList='escape'):
    core.quit()
moneyontrial= visual.TextStim(win, text='Congrats! You earned $' +str(rewardAmount/100.00) +'!', height = 0.1)
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