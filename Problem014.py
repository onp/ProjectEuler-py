# Project Euler Problem #14
# Longest Collatz sequence
''' The following iterative sequence is defined for the set of positive
    integers:
    n ->  n/2 (n is even)
    n ->  3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:
    13  40  20  10  5  16  8  4  2  1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
'''

colDict={1:0,2:1}

def collatzLen(x):
    xi=x
    coLen=0
    while x not in colDict:
        if x%2==0:
            x/=2
            coLen+=1
        else:
            x= 3*x+1
            coLen+=1

    coLen+=colDict[x]
    colDict[xi]=coLen

    return coLen

maxLen=0
maxStart=0

for x in range(3,1000000):
    if collatzLen(x)>maxLen:
        maxLen=collatzLen(x)
        maxStart=x

print(str(maxStart)+' with a length of '+str(maxLen))


# A= 837799