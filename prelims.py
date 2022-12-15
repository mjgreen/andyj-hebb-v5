from psychopy import core, visual, gui, data, event
import copy, sys, glob, numpy, string, random, math, itertools
import os

def getSessionInfo(verbose, debug):
    # present a dialogue box to collect session information
    dialogueDict = {
                'Name': u'learning experiment' ,
                'Version': '5',
                'Date': data.getDateStr(),
                'Session type: don\'t use Test for real data collection': ['Test', 'Experimental'],
                'Participant identifier': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)),
                'Participant number (optional)': '0'
                }
    dlg = gui.DlgFromDict(title='hebb', dictionary=dialogueDict, order=['Name','Version','Date','Participant identifier', 'Participant number (optional)'], fixed=['Name','Version','Date','Participant identifier'])
    if dlg.OK:
        session_info = dialogueDict
        if verbose: print('The user pressed OK at the dialogue box.')
    else:
        if verbose: print('The user pressed cancel at the dialogue box.')
        core.quit()

    # participant_data_filename = dlg.GetTitle() + '_' + 'Version' + '_' + session_info['Version'] + '_' + session_info['Participant identifier'] + '_' + session_info['Participant number (optional)'].zfill(3) + '_' + session_info['Date']
    participant_data_filename = session_info['Participant number (optional)'].zfill(3) + '_' + session_info['Participant identifier'] + '_'  + session_info['Date']

    return participant_data_filename, session_info

def showInstructions(verbose, debug):
    # display experiment level instructions and wait for a dismiss keypress
    # open a window
    win = visual.Window(
      size = [1920,1080],
      color = [255,255,255],
    #   allowGUI = True,
      units = 'height',
      monitor = 'testMonitor', # obligatory argument to avoid a warning
      screen = 1,
      fullscr = True)
    # show the instructions
    message1 = visual.TextStim(
      win=win,
      color='black',
      pos=[0,0],
      units='height',
      anchorHoriz='center',
      height=0.03,
      text='Hebb Experiment.\n\nYou will be presented with a series of images, one at a time in the center of the screen.\n\nThen you will be presented with the same images arranged in a circle.\n\nYour task is to click on the images in the order that they were originally presented to you.\n\nPress any key to begin.')
    message1.draw()
    win.flip() # flip the text
    if 'escape' in event.waitKeys(): core.quit()
    win.flip() # blank screen after keypress
    core.wait(2)
    return win

def chooseStimuli(verbose, debug):
    all_matrices = sorted(os.listdir("matrices"))
    m = random.sample(all_matrices, 10)
    m1 = m[0:5]
    m2 = m[5:10]
    all_faces = sorted(os.listdir("faces"))
    f = random.sample(all_faces, 5)
    return m1, m2, f
