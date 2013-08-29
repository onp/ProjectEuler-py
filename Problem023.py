# Project Euler Problem #23
# Non-abundant sums
''' A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors of
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper
    limit cannot be reduced any further by analysis even though it is known
    that the greatest number that cannot be expressed as the sum of two
    abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
'''

# is rather slow...

def isAbundant(number):
    # Returns the divisors of a number
    divs=1
    x=2
    minTopDiv=number-1
    if number%6==0:
        if number!=6: divs=number+1
    while (x<minTopDiv) & (divs<=number):
        if number%x==0:
            divs+=x
            if number/x !=x:
                divs+=int(number/x)
                minTopDiv=number/x
        x+=1
    return divs>number


abundants=[]
oddAbds=[]

noAbSum = 0
noAbLen = 0
noAb = []

for x in range(1,21000):
    #print(x)
    if isAbundant(x):
        abundants.append(x)
        if x%2 != 0: oddAbds.append(x)

    abFlag=0
    if x%2==0:
        for y in abundants:
            if y>(x/2+10):
                break
            if x-y in abundants:
                abFlag=1
                break
    else:
        for y in oddAbds:
            if x-y in abundants:
                abFlag=1
                break
    if abFlag==0:
        noAbSum+=x
        if x>20000: print(x)



print(noAbSum)


# A= 4179871
