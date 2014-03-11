# Project Euler Problem #33
# Digit canceling fractions
'''
 The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

fractions = []

for a in range(10,100):
    for b in range(a+1,100):
        if (a%10 == 0) and (b%10 == 0):
            continue
        sa = str(a)
        sb = str(b)
        if sa[0] in sb:
            sb = sb.replace(sa[0],"",1)
            if sb == '0':
                continue
            if int(sa[1])/int(sb) == a/b:
                fractions.append([a,b])
        elif sa[1] in sb:
            sb = sb.replace(sa[1],"",1)
            if sb == '0':
                continue
            if int(sa[0])/int(sb) == a/b:
                fractions.append([a,b])
            
print(fractions)

numerator = 1
denominator = 1

for a,b in fractions:
    numerator*= a
    denominator*= b
    
print(numerator,denominator)

factor = 2

while factor <= numerator:
    if (numerator%factor==0) and (denominator%factor==0):
        numerator/= factor
        denominator/= factor
    else:
        factor += 1
    
print(numerator,denominator)
    
# A= 100