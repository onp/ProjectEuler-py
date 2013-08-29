# Project Euler Problem #5
# Largest Prime Factor
''' The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
'''

primes=[2]

x=3
numP=1
while numP<10001:
    factors=0
    for y in primes:
        if x%y==0:
            factors=1
            break
    if factors==0:
        primes.append(x)
        numP+=1
        #print(x)
    x+=2

print(primes[-1])
# A= 104743