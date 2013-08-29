# Project Euler Problem #24
# Lexicographic permutations
''' A permutation is an ordered arrangement of objects. For example, 3124 is one
    possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
    are listed numerically or alphabetically, we call it lexicographic order.
    The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math as m

#1-9 has 9! permutations
# 0,2-8 has an additional 9! permutations....

available=[0,1,2,3,4,5,6,7,8,9]


finStr = ''
rem=1000000
rem-=1

for x in range(9,0,-1):
    nxtDig=int(rem/m.factorial(x))
    print(nxtDig)
    nxtDig=available.pop(nxtDig)
    finStr+=str(nxtDig)
    rem=rem%m.factorial(x)
    print(str(x)+ '  '+finStr+'  '+str(rem)+'   '+str(available))
    print('')

finStr+=str(available[0])

print(finStr)



# A= 2783915460
