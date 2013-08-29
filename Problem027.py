# Project Euler Problem #28
# Number Spiral Diagonals
''' Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?
'''

dim = 1001

diagSum=1

step=2
curr=1

while curr<dim**2:
    diagSum+=(10*step +4*curr)
    curr+=4*step
    step+=2

print(diagSum)




# A= 669171001