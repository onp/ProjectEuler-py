# Project Euler Problem #44
# 
'''
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?

'''

pentagonals = [1]

def isPent(x):
    if x<0:
        return False
    while x>pentagonals[-1]:
        n = len(pentagonals)+1
        nextPent = int(n*(3*n-1)/2)
        pentagonals.append(nextPent)
        
    if x in pentagonals:
        return True
    else:
        return False
        
n=2
diff = 9999999999999999

while n<2500:
    p1 = int(n*(3*n-1)/2)
    n += 1
    for p2 in pentagonals:
        if p2>p1:
            break
        if not isPent(p1-p2):
            continue
        if not isPent(p2+p1):
            continue
        if (p1-p2)<diff:
            diff = p1-p2
            print(p1,p2,diff)

print(diff)
        
# A = 5482660