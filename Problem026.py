# Project Euler Problem #26
# Reciprocal cycles
''' A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
    seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d  1000 for which 1/d contains the longest recurring cycle
    in its decimal fraction part.
'''

from decimal import *

numDigs=2000

getcontext().prec = numDigs
getcontext().rounding = ROUND_DOWN

one=Decimal(1)
maxCyLen=1
maxD=1

def cycleLen(denom):
    frac=str(one/denom)
    cycflag=0
    cyLen=0        #use this for just finding the cycle length, not the problem
    #cyLen=maxCyLen
    if len(frac)<(numDigs+2):
        return 0

    while frac[-(cyLen+1):] in frac[:-(cyLen+1)]:
        cyLen+=1
        if frac[-(cyLen):] == frac[-2*(cyLen):-(cyLen)]:
            cycflag=1
            break
    if cycflag==0:
        print('did not find cycle '+ str(denom))

    return cyLen

for x in range(1,1000):
    if cycleLen(x)>maxCyLen:
        maxD=x
        maxCyLen=cycleLen(x)

print(maxD)

# A= 983