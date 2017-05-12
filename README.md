There are 30 trials:
  * 10 blocks
    * 3 trials
      * Trial 1: 5 matrices
        * exposure phase:
          * expose user to 5 matrices, one at a time, centrally, in a predetermined fixed order that stays the same across blocks.
          * returns a vector of exposure matrix IDs e.g. [matrix55, matrix4, matrix46, matrix13, matrix21]; the sequence of elements is the order of exposure to matrix IDs.
        * recall presentation phase:
          * expose user to 5 matrices, 5 at a time, arranged around a clock, in a randomised order of assignment to clockposition.
          * returns a vector of clock positions
            * returns e.g., [matrix55@clock3, matrix4@clock4, matrix46@clock2, matrix13@clock1, matrix21@clock5] (presented clockpositions) where each element is a clock position clockwise from 12 o'clock, and the sequence of clockpositions should be read like this: clockposition[1] (3 in this case) contains matrixID[1] (55 in this case)
        * recall response phase:
          * user clicks on images one at a time in the order they think matches exposure order
          * returns a vector of clock positions; the sequence of clock positions in that vector is for comparison with the sequence of exposure
            * returns e.g., [1, 3, 2, 4, 5] (response clockpositions)
            * compare with: [3, 4, 2, 1, 5] (presented clockpositions)
        * accuracy computation phase:
          * restate the vector of exposure IDs
            * returns e.g., [55, 4, 46, 13, 21]
          * turn the vector of response clock positions e.g., [3, 4, 2, 1, 5] into a vector of response matrix IDs
            * returns e.g., [21, 13, 4, 55, 46]
          * compare each element of the vector of response matrix IDs against each element of the vector of exposure matrix IDs
            * returns e.g., [0,1,0,1,0] where 1 is accurate and 2 is error
        * feedback phase (for practice only):
