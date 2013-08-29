# Project Euler Problem #30
# Digit fifth powers
''' In England the currency is made up of pound, £, and pence, p, and there are
    eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    It is possible to make £2 in the following way:

    1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

    How many different ways can £2 be made using any number of coins?
'''

britishCoins = [200,100,50,20,10,5,2,1]

def fillDown(valueLeft,coinValues,coinIndex=0):
    if coinIndex >= len(coinValues):
        return 0
    coin = coinValues[coinIndex]
    if valueLeft/coin < 1:
        return fillDown(valueLeft,coinValues,coinIndex+1)
    else:
        uniqueFills = 0
        for coinCount in range(valueLeft//coin+1):
            uniqueFills += fillDown(valueLeft-coin*coinCount,coinValues,coinIndex+1)
        if valueLeft%coin == 0:
            uniqueFills += 1
        return uniqueFills

        
possibleWays = fillDown(200,britishCoins)

print(possibleWays)

# A=73682