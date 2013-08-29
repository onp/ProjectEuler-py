# Project Euler Problem #15
# Lattice Paths
''' Starting in the top left corner of a 22 grid, there are 6 routes (without
    backtracking) to the bottom right corner.

    How many routes are there through a 20x20 grid?
'''

import math as mt

#based on the fact that there must be 20 horizontal and 20 vertical moves, in
# any order:

Answer= int(mt.factorial(40)/(mt.factorial(20)**2))

print(Answer)


# A= 137846528820