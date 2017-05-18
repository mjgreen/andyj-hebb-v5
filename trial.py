from psychopy import core, visual, event
import random

def doOneTrial(stimuli_raw, clock_positions, isPractice, win,
               stimuliType, trialCount, blockCount, debug):
    trialCount=trialCount+1
    if debug: print("Trial  :                              :\t\tTrial {}".format(trialCount))

    # set up mouse
    mouse = event.Mouse()
    mouse.setVisible(False)
    mouse.setPos(newPos=(0,0))

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
    # define the order of clock positions to which images will be drawn
    correct_indices = random.sample([0,1,2,3,4],5) # e.g., [2,0,3,1,4]


    # for debug list clockposition contents
    stimuli_in_clockwise_order = []
    for i in [0,1,2,3,4]:
        stimuli_in_clockwise_order.append(stimuli[correct_indices[i]])
    if debug: print("Stimuli: in clockwise order           :\t\t{}".format(stimuli_in_clockwise_order))
    if debug: print("correct_indices                       :\t\t{}".format(correct_indices))
    # # the circle is just for adjusting clock positions in retrospect, so it can be commented out for the production version
    # showCircle=visual.Circle(win, lineColor='black', radius=.35)
    # showCircle.draw() # to buffer

    # write the stimuli to the backbuffer
    for i in range(len(stimuli)): # [0,1,2,3,4]
        showImage=visual.ImageStim(win) # initialise psychopy visual window called showImage
        showImage.setImage(stimuliType + "/" + stimuli[i]) # say which image gets shown on this iteration
        showImage.pos = clock_positions[correct_indices[i]] # use the i'th element of correct_indices as the clock position for the i'th stimulus
        showImage.draw() # to buffer without overwriting the circle

    # try and put a border round the stimulus -- that will be the target for listening for a mouseclick
    if stimuliType == 'matrices':
        y_offset=.1
    else:
        y_offset=.125
    for j in [0,1,2,3,4]:
            showBorder=visual.ShapeStim(win, "height", lineColor='black',
                                vertices=( (clock_positions[j][0]-0.1, clock_positions[j][1]-y_offset),
                                           (clock_positions[j][0]-0.1, clock_positions[j][1]+y_offset),
                                           (clock_positions[j][0]+0.1, clock_positions[j][1]+y_offset),
                                           (clock_positions[j][0]+0.1, clock_positions[j][1]-y_offset) ) )
            showBorder.draw()

    # flip the main combined recall display
    win.flip() # to screen

    # phase 3, response collection
    mouse.setPos(newPos=(0,0))
    mouse.setVisible(True)
    response_indices = []
    while len(response_indices) < len(stimuli):
        for clock_pos_index in [0,1,2,3,4]:
            if stimuliType == 'matrices':
                y_offset=.1
            else:
                y_offset=.125
            if ( mouse.isPressedIn(shape=visual.ShapeStim(win, "height", lineColor='black',
                                       vertices=(
                                       (clock_positions[clock_pos_index][0]-0.1, clock_positions[clock_pos_index][1]-y_offset),
                                       (clock_positions[clock_pos_index][0]-0.1, clock_positions[clock_pos_index][1]+y_offset),
                                       (clock_positions[clock_pos_index][0]+0.1, clock_positions[clock_pos_index][1]+y_offset),
                                       (clock_positions[clock_pos_index][0]+0.1, clock_positions[clock_pos_index][1]-y_offset)
                                       )
                                    )
                                    )
                and
                clock_pos_index not in response_indices):
                    response_indices.append(clock_pos_index)
                    # indicate already selected
                    # first redraw the images
                    # write the stimuli to the backbuffer
                    for i in range(len(stimuli)): # [0,1,2,3,4]
                        showImage=visual.ImageStim(win) # initialise psychopy visual window called showImage
                        showImage.setImage(stimuliType + "/" + stimuli[i]) # say which image gets shown on this iteration
                        showImage.pos = clock_positions[correct_indices[i]] # use the i'th element of correct_indices as the clock position for the i'th stimulus
                        showImage.draw() # to buffer
                    # then overlay borders
                    if stimuliType == 'matrices':
                        y_offset=.1
                    else:
                        y_offset=.125
                    for j in [0,1,2,3,4]:
                        if j in response_indices:
                            my_line_color='blue'
                            my_line_width=20
                        else:
                            my_line_color='black'
                            my_line_width=2
                        showBorder=visual.ShapeStim(win, "height", lineColor=my_line_color, lineWidth=my_line_width,
                                                vertices=( (clock_positions[j][0]-0.1, clock_positions[j][1]-y_offset),
                                                           (clock_positions[j][0]-0.1, clock_positions[j][1]+y_offset),
                                                           (clock_positions[j][0]+0.1, clock_positions[j][1]+y_offset),
                                                           (clock_positions[j][0]+0.1, clock_positions[j][1]-y_offset) ) )
                        showBorder.draw()
                    win.flip()
    # this flip runs after 5 responses have been made
    win.flip()
    if debug: print("response_indices                      :\t\t{}".format(response_indices))

    mouse.setVisible(False)

    # phase 4, response evaluation
    evaluation = []
    for i in [0,1,2,3,4]:
        if response_indices[i] == correct_indices[i]:
            evaluation.append(1)
        else:
            evaluation.append(0)
    if debug: print("evaluation                            :\t\t{}".format(evaluation))
    else: print("evaluation                            :\t\t{}".format(evaluation))

    trial_accuracy = False
    trial_accuracy_accumulator = 0
    for i in [0,1,2,3,4]:
        if evaluation[i] == 1:
            trial_accuracy_accumulator = trial_accuracy_accumulator + 1
    if debug: print("number of correct answers out of 5    :\t\t{}".format(trial_accuracy_accumulator))
    else: print("number of correct answers out of 5    :\t\t{}".format(trial_accuracy_accumulator))
    if trial_accuracy_accumulator == 5:
        trial_accuracy = True
    if debug: print("Whole-Trial accuracy                  :\t\t{}".format(trial_accuracy))
    else: print("Whole-Trial accuracy                  :\t\t{}".format(trial_accuracy))

    # phase 5, feedback, only if it's the practice block
    if blockCount==0:
        for i in range(len(stimuli)): # [0,1,2,3,4]
            showImage=visual.ImageStim(win) # initialise psychopy visual window called showImage
            showImage.setImage(stimuliType + "/" + stimuli[i]) # say which image gets shown on this iteration
            showImage.pos = clock_positions[correct_indices[i]] # use the i'th element of correct_indices as the clock position for the i'th stimulus
            showImage.draw() # to buffer
        # then overlay borders with color conditional on accuracy
        if stimuliType == 'matrices':
            y_offset=.1
        else:
            y_offset=.125
        for j in [0,1,2,3,4]:
            if evaluation[j]==1:
                my_line_color='green'
                my_line_width=20
            else:
                my_line_color='red'
                my_line_width=20
            showBorder=visual.ShapeStim(win, "height", lineColor=my_line_color, lineWidth=my_line_width,
                                    vertices=( (clock_positions[j][0]-0.1, clock_positions[j][1]-y_offset),
                                               (clock_positions[j][0]-0.1, clock_positions[j][1]+y_offset),
                                               (clock_positions[j][0]+0.1, clock_positions[j][1]+y_offset),
                                               (clock_positions[j][0]+0.1, clock_positions[j][1]-y_offset) ) )
            showBorder.draw()
        # then print the correct_indices[j] as a character near the stimulus
        for i in [0,1,2,3,4]:
            feedback_correct_sequence=visual.TextStim(win=win, color='black', units="height", height=.05,
                     text=str(correct_indices[i]+1), pos=(clock_positions[i][0]-.115, clock_positions[i][1]-.105) )
            feedback_correct_sequence.draw()
        # then ask for a keypress so they get time to see the feedback
        feedback_key_wait_message = visual.TextStim(
          win=win,
          color='black',
          pos=[0,-.10],
          units='height',
          alignHoriz='center',
          height=0.03,
          text=("Press any key to dismiss feedback") )
        feedback_key_wait_message.draw()
        win.flip()
        if 'escape' in event.waitKeys(): core.quit()

    # phase 6, end of block message with keypress wait
    end_of_block_message = visual.TextStim(
      win=win,
      color='black',
      pos=[0,0],
      units='height',
      alignHoriz='center',
      height=0.03,
      #text=("End of trial number {} in current block.".format(trialCount), "Block {}".format(blockCount) )
      text=("Press any key when you are ready to continue"))
    end_of_block_message.draw()
    win.flip()
    if 'escape' in event.waitKeys(): core.quit()
    win.flip()
    core.wait(2)
    print("")
    return trialCount, blockCount
