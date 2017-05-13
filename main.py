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

# block count starts at zero which indicates a practiice block
blockCount=0

# run one block for practice
isPractice = block.doOneBlock(verbose=verbose, debug=debug, isPractice=isPractice,
                              m1=m1,m2=m2,f=f, win=win, blockCount=blockCount)

# run 10 blocks as experimental blocks
for each_block in [1,2,3,4,5,6,7,8,9,10]:
    blockCount=block.doOneBlock(verbose=verbose, debug=debug, isPractice=isPractice,
                             m1=m1,m2=m2,f=f, win=win, blockCount=blockCount)
