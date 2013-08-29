# Project Euler Problem #5
# Largest Prime Factor
''' 2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
'''

#seems to be some weirdness happening for large numbers. see
#  23982398738922*2*3*109*21
# works fine for the stated problem though.

import math as mt

def factors1(number):
    # Returns the factors of a number
    if type(number) is not int:
        return False
    factS=[]
    maxFact=2
    while int(number) > 1:
        rtLim=int(mt.sqrt(number))+1
        if maxFact>=rtLim:
            factS.append(int(number))
            break
        for x in range(maxFact,rtLim+1):
            if number%x==0:
                maxFact=x
                number=number/x
                factS.append(x)
                break
            if x==rtLim:
                factS.append(int(number))
                number=1
                break


    return factS



factors=[]

#finds the common factors of all of the numbers in the range.
for x in range(2,20+1):
    subFacts=factors1(x)
    searchStart=0
    for y in subFacts:
        if subFacts.count(y)>factors.count(y):
            factors.append(y)



pi1=1

for x in factors:
    pi1=pi1*x


print(pi1)

# A=232792560