# Project Euler Problem #3
# Largest Prime Factor
''' The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
'''
# solution assumes that answer is less than 4000, but is easily extensible.

numT= 600851475143

primes=[2]
ntFactors=[]

for x in range(3,4000,2):
    factors=0
    for y in primes:
        if x%y==0:
            factors=1
            break
    if factors==0:
        primes.append(x)
        if numT%x==0:
            numT=numT/x
            ntFactors.append(x)
    if x>numT/2:
        ntFactors.append(int(numT))
        numT=1
        break


print(ntFactors)
if numT != 1:
    print(str(numT)+' left, max prime may not have been found. Enlarge interval')

# A= 6857