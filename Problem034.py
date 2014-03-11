# Project Euler Problem #34
# Digital factorials
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial

digitFactorials =[]

# 8*9! < 99999999, so all digital factorials are smaller than 8*9!
for a in range(10,8*factorial(9)):
    total = 0
    for b in str(a):
        total += factorial(int(b))
    if total == a:
        digitFactorials.append(total)
     
print(digitFactorials)

print(sum(digitFactorials))
    
# A= 40730