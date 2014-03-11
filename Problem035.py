# Project Euler Problem #35
# Circular primes
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

potentialFactors = []

working = list(range(999,1,-1))

while len(working)>0:
    a = working.pop()
    if a == 0:
        continue
    potentialFactors.append(a)
        
    working = [b for b in working if b%a != 0]

def noEvenRotations(x):
    for a in str(x):
        if int(a) in [0,2,4,6,8]:
            return False
    return True
    
newWorking = [x for x in range(2,1000000) if noEvenRotations(x)]

print(len(newWorking), "candidates")
    
circularPrimes = [2]

def isPrime(x):
    x = int(x)
    for factor in potentialFactors:
        if x==factor:
            return True
        if x%factor == 0:
            return False
    return True
    

while len(newWorking)>0:
    a = str(newWorking[-1])
    rotations = []
    mightBeCircular = True
    for x in range(len(a)):
        b = int(a[-x:] + a[:-x])
        if b not in newWorking:
            continue
        elif mightBeCircular:
            newWorking.remove(b)
            if isPrime(b):
                rotations.append(b)
            else:
                rotations = []
                mightBeCircular = False
        else:
            newWorking.remove(b)
    circularPrimes.extend(rotations)
    
        
print(len(circularPrimes), "circular primes below 1000000")
    
# A = 55