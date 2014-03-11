# Project Euler Problem #37
# Truncatable primes
'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

potentialFactors = []

working = list(range(999,1,-1))

while len(working)>0:
    a = working.pop()
    if a == 0:
        continue
    potentialFactors.append(a)
        
    working = [b for b in working if b%a != 0]

def noNonPrimeTruncates(x):
    for i,a in enumerate(str(x)):
        if int(a) in [0,4,6,8]:
            return False
        if int(a) in [2,5] and (i != 0):
            return False
    return True
    
candidates = [x for x in range(10,1000000) if noNonPrimeTruncates(x)]

print(len(candidates), "candidates")
    
truncatablePrimes = []

def isPrime(x):
    if x == '':
        return True
    x = int(x)
    if x == 1:
        return False
    for factor in potentialFactors:
        if x==factor:
            return True
        if x%factor == 0:
            return False
    return True
    
for a in candidates:
    aStr = str(a)
    viable = True
    pieces = [[],[]]
    for i in range(len(aStr)):
        if isPrime(aStr[i:]):
            pieces[0].append(int(aStr[i:]))
        else:
            viable = False
            break
    for i in range(-1,-len(aStr),-1):
        if isPrime(aStr[:i]):
            pieces[1].append(int(aStr[:i]))
        else:
            viable = False
            break
            
    if viable:
        pieces = [x for x in pieces if len(str(x))>1]
        print(a, pieces)
        truncatablePrimes.append(a)
        
print(len(truncatablePrimes),"truncatable primes")
print(sum(truncatablePrimes))
    
# A = 