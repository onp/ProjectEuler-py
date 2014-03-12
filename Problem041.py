# Project Euler Problem #41
# Pandigital Prime
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''

from itertools import permutations

#find all primes below 31427 (sqrt of the largest pandigital 987654321)
primes = [2]

working = list(range(32999,1,-2))

while len(working)>0:
    a = working.pop()
    if a == 0:
        continue
    primes.append(a)
        
    working = [b for b in working if b%a != 0]
    
print(len(primes),"primes found")

def isPrime(x):
    for p in primes:
        if x%p == 0:
            if x == p:
                return True
            else:
                return False
    return True
    
solution = None

for numDigits in range(9,0,-1):
    if solution:
        break
    print(numDigits, "digits")
    digits = [str(a) for a in range(numDigits,0,-1)]
    for pan in permutations(digits):
        candidate = int("".join(pan))
        if isPrime(candidate):
            solution = candidate
            break

print(solution)
            
# A = 7652413