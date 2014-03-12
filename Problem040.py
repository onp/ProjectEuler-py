# Project Euler Problem #40
# Champernowne's Constant
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

number = 0
numDigits = 1
limit = 10

digit = 0
target = 1

digits = []


while target<10**7:
    number += 1
    if number == limit:
        numDigits += 1
        limit *= 10
    digit += numDigits
    if digit >=target:
        digits.append(str(number)[target-digit-1])
        target *= 10
        
product = 1
for dig in digits:
    product *= int(dig)
    
print(product)

    
# A = 210