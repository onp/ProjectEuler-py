# Project Euler Problem #36
# Double-base palindromes
'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

palindromes = []

#values under 10:
for a in range(10):
    aBin = bin(a)[2:]
    
    isBinPal = True
    for i in range(len(aBin)//2):
        if aBin[i] != aBin[-(i+1)]:
            isBinPal = False
    if isBinPal:
        palindromes.append(a) 

#11 to 999999:
for a in range(1,1000):
    #even number of digits
    aPal = int(str(a)+str(a)[::-1])
    aBin = bin(aPal)[2:]
    
    isBinPal = True
    for i in range(len(aBin)//2):
        if aBin[i] != aBin[-(i+1)]:
            isBinPal = False
    if isBinPal:
        palindromes.append(aPal)
    
    #odd number of digits
    if a>99:
        continue
    for mid in range(10):
        aPal = int(str(a)+str(mid)+str(a)[::-1])
        aBin = bin(aPal)[2:]
        
        isBinPal = True
        for i in range(len(aBin)//2):
            if aBin[i] != aBin[-(i+1)]:
                isBinPal = False
        if isBinPal:
            palindromes.append(aPal)
            
print(sum(palindromes))
    
# A = 872187