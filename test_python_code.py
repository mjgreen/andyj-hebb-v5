from psychopy import core, visual, gui, data, event
import os, random

# all_faces = sorted(os.listdir("faces"))
# f = random.sample(all_faces, 5)
# # clock_positions = [
# # (0.37925925925925924, 0.0),
# # (0.11719755638516526, 0.36069698988379156),
# # (-0.30682718601479481, 0.2229229993879602),
# # (-0.30682718601479492, -0.22292299938796012),
# # (0.11719755638516517, -0.36069698988379156)]
# # (-0.6667,-0.5) in the bottom left to (+0.6667,+0.5) in the top right
# clock_positions = [
# #(LR offset, UPDWN offset)
# #(x,      y)
# ( 0.0,  0.35),
# ( 0.325,  0.1),
# ( 0.225,  -.25),
# (-0.225,  -.25),
# (-.325,    .1)
# ]
# win = visual.Window(
#   size = [1920,1080],
#   color = [255,255,255],
#   units = 'height',
#   monitor = 'testMonitor',
#   screen = 1,
#   fullscr = True)
#
# # showImage=visual.Circle(win, fillColor='red', lineColor='red', radius=0.02)
# # showImage.draw()
# # win.flip()
# # core.wait(3)
#
#
# showCircle=visual.Circle(win, lineColor='black', radius=.35)
# showCircle.draw()
# for i in [0,1,2,3,4]:
#     showImage=visual.ImageStim(win)
#     showImage.setImage("faces" + "/" + f[i])
#     showImage.pos = clock_positions[i]
#     showImage.opacity=.5
#     showImage.draw()
# win.flip()
# if 'escape' in event.waitKeys(): core.quit()
#     #showImage=visual.ImageStim(win) # initialise psychopy visual window called showImage
#     # showImage.setImage("faces" + "/" + f[i-1]) # say which image gets shown on this iteration
#     # showImage.pos = clock_positions[i-1] # clockwise on screen
#     # showImage.draw() # to buffer
#     # win.flip(clearBuffer=False) # to screen
#     # core.wait(3) # stimulus display duration in seconds
#     # win.flip() # clear screen
#     # core.wait(1) # ISI (inter-stimulus-interval) in seconds

stimuli=['matrix14.jpg', 'matrix46.jpg', 'matrix50.jpg', 'matrix42.jpg', 'matrix56.jpg']
random_indices = random.sample([0,1,2,3,4],5) # e.g., [2,0,3,1,4]
print("random_indices",random_indices)
stimuli_in_clockwise_order = []
print("stimuli_in_clockwise_order", stimuli_in_clockwise_order)
stimuli_in_clockwise_order.append(stimuli[random_indices[0]])
print("stimuli_in_clockwise_order", stimuli_in_clockwise_order)
# for i in [0,1,2,3,4]:
    # stimuli_in_clockwise_order[i] = stimuli[random_indices[i]]
