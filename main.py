import os, random

verbose=True
veryverbose = False
debug=False

# choose 5 matrices for matrix subset1 1 called m1 and 5 matrices for m2
all_matrices = sorted(os.listdir("matrices"))
m = random.sample(all_matrices, 10)
m1 = m[0:5]
m2 = m[5:10]
if verbose: print("m:\t\t\t{}".format(m))
if verbose: print("m1:\t\t\t{}".format(m1))
if verbose: print("m2:\t\t\t{}".format(m2))

# choose 5 faces for the faces trials
all_faces = sorted(os.listdir("faces"))
f = random.sample(all_faces, 5)
if verbose: print("f:\t\t\t{}".format(f))

# make a list of clock positions
clock_positions = [(0.37925925925925924, 0.0), (0.11719755638516526, 0.36069698988379156), (-0.30682718601479481, 0.2229229993879602), (-0.30682718601479492, -0.22292299938796012), (0.11719755638516517, -0.36069698988379156)]
if verbose: print("clock_positions:\t{}".format(clock_positions))
