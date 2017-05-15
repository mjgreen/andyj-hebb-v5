from psychopy import core, visual, event
import random
def doOneTrial(stimuli_raw, clock_positions, isPractice, win,
               stimuliType, trialCount, blockCount, debug):
    trialCount=trialCount+1
    if debug: print("Trial  :                              :\t\tTrial {}".format(trialCount))

    # shuffle the stimuli if it is a matrix trial but not if it is a faces trial
    if stimuliType == "matrices":
        stimuli = random.sample(stimuli_raw,5)
    else:
        stimuli = stimuli_raw
    if debug: print("Stimuli: in order of initial selection:\t\t{}".format(stimuli_raw))
    if debug: print("Stimuli: in order of exposure         :\t\t{}".format(stimuli))

    # phase 1, exposure
    for i in range(len(stimuli)):
        showImage=visual.ImageStim(win) # initialise psychopy visual window called showImage
        showImage.setImage(stimuliType + "/" + stimuli[i]) # say which image gets shown on this iteration
        showImage.pos = (0,0) # central position on screen
        showImage.draw() # to buffer
        win.flip() # to screen
        core.wait(1) # stimulus display duration in seconds
        win.flip() # clear screen
        core.wait(1) # ISI (inter-stimulus-interval) in seconds

    # phase 2, recall
    # the circle is just for adjusting clock positions in retrospect, so it can be commented out for the production version
    showCircle=visual.Circle(win, lineColor='black', radius=.35)
    showCircle.draw() # to buffer
    for i in range(len(stimuli)):
        showImage=visual.ImageStim(win) # initialise psychopy visual window called showImage
        showImage.setImage(stimuliType + "/" + stimuli[i]) # say which image gets shown on this iteration
        showImage.pos = clock_positions[i] # clockwise on screen
        showImage.draw() # to buffer without overwriting the circle
    win.flip() # to screen
    core.wait(1) # stimulus display duration in seconds
    win.flip() # clear screen
    core.wait(1) # ISI (inter-stimulus-interval) in seconds

    # phase 3, response collection

    # phase 4, response evaluation

    # phase 4, feedback, only if it's the practice block

    # phase 5, pre-return message1
    pre_return_message = visual.TextStim(
      win=win,
      color='black',
      pos=[0,0],
      units='height',
      alignHoriz='center',
      height=0.03,
      text=("End of trial number {} in current block.".format(trialCount), "Block {}".format(blockCount) ) )
    pre_return_message.draw()
    win.flip()
    if debug:
        event.waitKeys(2)
    else:
        if 'escape' in event.waitKeys(): core.quit()
    return trialCount, blockCount
