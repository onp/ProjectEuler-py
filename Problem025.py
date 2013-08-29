# Project Euler Problem #25
# 1000 digit fibonacci number
''' The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

a=1
b=2
termCount=3
digCount=10

while digCount<1000:
    a,b=b,a+b
    termCount+=1
    if b>10**10:
        a,b= a//10,b//10
        digCount+=1

print(termCount)


# A= 4782
