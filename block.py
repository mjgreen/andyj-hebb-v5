import trial, os, random
def doOneBlock(verbose, debug, isPractice, m1, m2, f, win, blockCount):

    # make a list of clock positions
    # clock_positions = [(0.37925925925925924, 0.0), (0.11719755638516526, 0.36069698988379156), (-0.30682718601479481, 0.2229229993879602), (-0.30682718601479492, -0.22292299938796012), (0.11719755638516517, -0.36069698988379156)]
    clock_positions = [
    #(LR offset, UPDWN offset)
    #(x,      y)
    ( 0.0  ,   0.35),
    ( 0.325,   0.10),
    ( 0.225,  -0.25),
    (-0.225,  -0.25),
    (-0.325,   0.10)
    ]
    # say that it is trial 0
    trialCount=0

    if isPractice:
        # if it is practice, choose a set of stimuli that are distinct
        # from the experimental stimuli that were set in prelims.chooseStimuli()
        all_matrices = sorted(os.listdir("matrices"))
        m = random.sample(all_matrices, 10)
        m1 = m[0:5]
        m2 = m[5:10]
        all_faces = sorted(os.listdir("faces"))
        f = random.sample(all_faces, 5)
        # this gets run when it is still practice
        print("Block  :                              :\t\tBlock {} (practice is block 0)".format(blockCount))
        trialCount, blockCount = trial.doOneTrial(stimuli_raw=m1, clock_positions=clock_positions, isPractice=isPractice, win=win,
            stimuliType="matrices", trialCount=trialCount, blockCount=blockCount, debug=debug)
        trialCount, blockCount = trial.doOneTrial(stimuli_raw=m2, clock_positions=clock_positions, isPractice=isPractice, win=win,
            stimuliType="matrices", trialCount=trialCount, blockCount=blockCount, debug=debug)
        trialCount, blockCount = trial.doOneTrial(stimuli_raw=f, clock_positions=clock_positions, isPractice=isPractice, win=win,
            stimuliType="faces", trialCount=trialCount, blockCount=blockCount, debug=debug)
        # turn off isPractice now
        isPractice=False
    else:
        # this gets run when is not practice any more
        blockCount=blockCount+1
        print("Block  :                              :\t\tBlock {}".format(blockCount))
        trialCount, blockCount = trial.doOneTrial(stimuli_raw=m1, clock_positions=clock_positions, isPractice=isPractice, win=win,
            stimuliType="matrices", trialCount=trialCount, blockCount=blockCount, debug=debug)
        trialCount, blockCount = trial.doOneTrial(stimuli_raw=m2, clock_positions=clock_positions, isPractice=isPractice, win=win,
            stimuliType="matrices", trialCount=trialCount, blockCount=blockCount, debug=debug)
        trialCount, blockCount = trial.doOneTrial(stimuli_raw=f, clock_positions=clock_positions, isPractice=isPractice, win=win,
            stimuliType="faces", trialCount=trialCount, blockCount=blockCount, debug=debug)
    #
    return blockCount
