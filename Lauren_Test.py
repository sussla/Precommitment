from __future__ import absolute_import, division
from psychopy import gui, visual, core, event
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
import sys  # to get file system encoding
import csv
import random
import time
import Pre_Helper as helper


########### Basic experiment settings ###########

### Ensure that relative paths start from the same directory as this script ###
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

### Store info about the experiment session ###
expName = 'PreComm_Task'  # from the Builder filename that created this script
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = time.strftime("%d%m%Y")#data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

### log file name ###
## log order: 'timing','Expected Reward','Decision (0=quit;1=complete; 2=failed)','RT','Trial Time','Total Time','Trial result','Task presentec','Parameters used'
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date']) # old
filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
filename2 = u'data/attention_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

### Check if data folder exists ###
if os.path.isdir(_thisDir + os.sep + 'data') == False:
    print ('NOTE: Created data directory because none existed')
    os.makedirs('data')

###### Setup the Window #######
win = visual.Window(
    size=(2560, 1440), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)

##### timing parameters #######
taskTime = 4
isiTime = 1
blockLength = 5
length = 5

## Create Stimuli ##
# stimuli outside loop - stimuli that do not change ###
isi = visual.TextStim(win, text='+')
optionText = visual.TextStim(win=win, text='PLAY (1) or PICK (2)', height=0.1)
pickText = visual.TextStim(win, text='PICK', height=0.1)
playText = visual.TextStim(win, text='PLAY', height=0.1)
chooseText = visual.TextStim(win, text='Left (1) or Right (2)', height=0.1)
rectangle_1 = visual.Rect(win, width=0.6, height=0.6, autoLog= None, fillColor=[-0.2,-0.2,-0.2], pos = [0.5,0])
rectangle_2 = visual.Rect(win, width=0.6, height=0.6, autoLog= None, fillColor=[-0.2,-0.2,-0.2], pos = [-0.5,0])
looseText = visual.TextStim(win, text='loose', height=0.1)
values_change = visual.TextStim(win, text='Values Change', height=0.1)
Final_value = visual.TextStim(win, text='Final Values', height = 0.1)
highlight_1 = visual.Rect(win, width=0.6, height=0.6, autoLog= None, pos = [0.5,0])
highlight_2 = visual.Rect(win, width=0.6, height=0.6, autoLog= None, pos = [-0.5,0])
rewardtext = visual.TextStim(win, text = '$0.25', height = 0.1)
miss = visual.TextStim(win, text = 'miss', height = 0.1)

###### set clocks #######
globalClock = core.Clock()
trialClock = core.Clock()
playClock = core.Clock()

### Task parameters ####
rewardAmount = 0 #cummulative reward amount 
nTrials = 3

##############################
###### Begin experiment ######
##############################

#Start with the welcome screen 
start = visual.TextStim(win, text= 'Welcome! \n' + 'Press ENTER to begin', height= 0.1)
start.draw()
win.flip()
event.waitKeys(keyList=['return'])
globalClock.reset()

#begin trial loop 
for trialIdx in range(nTrials):
    #Start with the cross before each trial 
    isi.draw()
    win.flip()
    core.wait(1)
    trialClock.reset()
    #track the reward value for each particular trial 
    cents = 0 
    # pick options from helper for this trial
    optionValues = helper.pickvalues()
    #stimuli that need to change for each trial
    pickoptionA = visual.TextStim(win=win, text= optionValues['optionA'], name='optionA', pos = [0.5,0], rgb= None, color=(0,1,0), colorSpace='rgb')
    pickoptionB = visual.TextStim(win=win, text= optionValues['optionB'], name='optionB', pos = [-0.5,0], rgb= None, color=(1,0,0), colorSpace='rgb')
    endoptionA = visual.TextStim(win=win, text= optionValues['endA'], name='endA', pos = [0.5,0], rgb= None, color=(0,1,0), colorSpace='rgb')
    endoptionB = visual.TextStim(win=win, text= optionValues['endB'], name='endB', pos = [-0.5,0], rgb= None, color=(1,0,0), colorSpace='rgb')
    #prepare to start routine "pick options"
    pickoptionA.draw()
    pickoptionB.draw()
    optionText.draw()
    win.flip()
    #pick options routine
    pickChoice = helper.pickoptions(win)
    if pickChoice['play']: #if choose to play on this trial 
        #screen to show that play was choosen 
        pickoptionA.draw()
        pickoptionB.draw()
        playText.draw()
        win.flip()
        core.wait(1)
        #start play routine with fixation cross
        isi.draw()
        win.flip()
        core.wait(1)
        #show the two options for the playing 
        endoptionA.draw()
        endoptionB.draw()
        win.flip()
        core.wait(0.2)
        win.flip()
        core.wait(0.2)
        #mask the two options
        rectangle_1.draw()
        rectangle_2.draw()
        win.flip()
        core.wait(1)
        #start the play routine to record response
        playgame = helper.play_routine(win)
        if playgame['win_right']:#if choose the right option on play
            cents = optionValues['endB']
            win.flip()
            #another iti for fun 
            isi.draw()
            win.flip()
            core.wait(1)
            ##indicate what you got
            Final_value.draw()
            endoptionA.draw()
            endoptionB.draw()
            highlight_2.draw()
            win.flip()
            core.wait(1)
        if playgame['win_left']:#if choose the left option on play
            cents = optionValues['endA']
            win.flip()
            #another iti for fun 
            isi.draw()
            win.flip()
            core.wait(1)
            ##indicate what you got
            Final_value.draw()
            endoptionA.draw()
            endoptionB.draw()
            highlight_1.draw()
            win.flip()
            core.wait(1)
        elif playgame['loose']: #if do not pick within the allowed time (you "lost" the game)
            looseText.draw()
            potentials = [optionValues['endA'], optionValues['endB']]
            loosing_win = random.choice(potentials)
            print(loosing_win)
            cents == loosing_win
            win.flip()
            Final_value.draw()
            endoptionA.draw()
            endoptionB.draw()
            if loosing_win == str(optionValues['endA']):
               highlight_1.draw()
            elif loosing_win == str(optionValues['endB']):
                highlight_2.draw()
            win.flip()
            core.wait(1)
    elif pickChoice['pick']: #if choose pick on this trial 
        #indicate that pick was chosen for this trial
        pickoptionA.draw()
        pickoptionB.draw()
        pickText.draw()
        win.flip()
        core.wait(1)
        #instructions on how to pick 
        chooseText.draw()
        pickoptionA.draw()
        pickoptionB.draw()
        win.flip()
        core.wait(1)
        #run the pick (precommitment) routine from helper to record options chosen 
        precomm = helper.precomm_pick(win)
        if precomm['left']: #if choose to precommit to the left option 
            pickoptionA.draw()
            cents = optionValues['endA']
            win.flip()
            core.wait(1)
            #indicate that the values change 
            values_change.draw()
            win.flip()
            core.wait(1)
            #show the final values and the one that you earn on this trial
            Final_value.draw()
            endoptionA.draw()
            endoptionB.draw()
            highlight_1.draw()
            win.flip()
            core.wait(1)
        elif precomm['right']: #if choose to precommit to the right option
            pickoptionB.draw()
            cents = optionValues['endB']
            win.flip()
            core.wait(1)
            #indicate that the values change
            values_change.draw()
            win.flip()
            core.wait(1)
            #show the final values and the one that you earn on this trial 
            Final_value.draw()
            endoptionA.draw()
            endoptionB.draw()
            highlight_2.draw()
            win.flip()
            core.wait(1)
        elif precomm['miss']:
            miss.draw()
            win.flip()
            core.wait(1)
            cents = 0
    elif pickChoice['miss']:
        miss.draw()
        win.flip()
        core.wait(1)
        cents = 0
    #show the amount of money earned on this trial
    if cents == optionValues['endA']: #you earned the A value
        reward_amountA = str(optionValues['endA'])
        #show on the screen the amount that you earned 
        winning_textA = visual.TextStim(win, text = 'You earned ' +str(reward_amountA)+ ' cents', height = 0.1)
        winning_textA.draw()
        #nonstring record for the cummulative reward amount record
        money = optionValues['endA']
        win.flip()
        core.wait(1)
    if cents == optionValues['endB']: #you earned the B value
        reward_amountB = str(optionValues['endB'])
        #show on the screen the amount that you earned 
        winning_textB= visual.TextStim(win, text = 'You earned ' +str(reward_amountB)+ ' cents', height = 0.1)
        winning_textB.draw()
        #nonstring record for the cummulative reward amount record
        money = optionValues['endB']
        win.flip()
        core.wait(1)
    if cents == loosing_win:
        reward_amount == loosing_win
        loosing_winning_text = visual.TextStim(win, text = 'You earned ' +loosing_win+ ' cents', height = 0.1)
        loosing_winning_text.draw()
        money = loosing_win
        win.flip()
        core.wait(1)
    elif cents == 0:
        money = 0
    #to add the money that you earned on this trial to the cummulative amount 
    rewardAmount += money

#show earnings on entire block 
moneyontrial= visual.TextStim(win, text='You earned a total of : ' +str(rewardAmount) + ' cents !', height = 0.1)
moneyontrial.draw()
win.flip()
core.wait(1)

#end the experiment 
win.close()
core.quit()