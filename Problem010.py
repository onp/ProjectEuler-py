# Project Euler Problem #10
# Summation of Primes
''' The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
'''

lL=2000000

primes=list(range(lL))

primes[1]=0

for x in range(lL):
    if primes[x] != 0:
        for y in range(2*x,lL,x):
            primes[y]=0



print(sum(primes))


# A= 142913828922