# v5
from psychopy import visual, event, core
import os, random
import prelims
import block


# globals
verbose=True
veryverbose=False
debug=True
blockCount=0
isPractice=True

# get session info using a dialogue box
participant_data_filename, \
session_info = \
prelims.getSessionInfo(verbose=verbose, debug=debug)

# run intro with instructions
win = prelims.showInstructions(verbose=verbose, debug=debug)

# choose stimuli
m1,m2,f = prelims.chooseStimuli(verbose=verbose, debug=debug)

# run one block for practice
isPractice = block.doOneBlock(verbose=verbose, debug=debug, isPractice=isPractice,
                              m1=m1,m2=m2,f=f, win=win, blockCount=blockCount, participant_data_filename=participant_data_filename, session_info=session_info)

# end of practice message
end_of_practice_message = visual.TextStim(
      win=win,
      color='black',
      pos=[0,0],
      units='height',
      alignHoriz='center',
      height=0.03,
      text='This is the end of the practice phase. There now follows 30 experimental trials for which you will not receive feedback. Press space bar to begin.')
end_of_practice_message.draw()
win.flip() # flip the text
if 'escape' in event.waitKeys(): core.quit()
win.flip() # blank screen after keypress
core.wait(2) # wait 2 seconds befor moving on

# run 10 blocks as experimental blocks
for each_block in [1,2,3,4,5,6,7,8,9,10]:
    blockCount=block.doOneBlock(verbose=verbose, debug=debug, isPractice=isPractice,
                             m1=m1,m2=m2,f=f, win=win, blockCount=blockCount, participant_data_filename=participant_data_filename, session_info=session_info)
