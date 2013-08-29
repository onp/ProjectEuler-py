# Project Euler Problem #4
# Largest Palindrome Product
''' A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
'''

#solution assumes a is within 200 of b.

def palinTest(number):
    x=list(str(number))
    while len(x)>1:
        a=x.pop(len(x)-1)
        b=x.pop(0)
        if a != b:
            return False
    return True


stopTest=0

for a in range(999,100,-1):
    if stopTest==1:
        break
    for b in range(999,a-200,-1):
        if palinTest(a*b):
            print(a*b)
            stopTest=1
            break


# A= 96609