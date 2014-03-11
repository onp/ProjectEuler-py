# Project Euler Problem #32
# Pandigital Products
''' We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from itertools import permutations

productList = []

for order in permutations([str(i) for i in range(1,10)]):
    leftA = int(order[0]) * int(''.join(order[1:5]))
    rightA = int(''.join(order[5:]))
    if (leftA == rightA) and (rightA not in productList):
        productList.append(rightA)

    leftB = int(''.join(order[0:2])) * int(''.join(order[2:5]))
    rightB = int(''.join(order[5:]))
    if (leftB == rightB) and (rightB not in productList):
        productList.append(rightB)

print(sum(productList))

# A= 45228