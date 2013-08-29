# Project Euler Problem #17
# Number letter counts
''' If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
    letters. The use of "and" when writing out numbers is in compliance with
    British usage.
'''

dictNumLengths={'1':len("one"),'2':len("two"),'3':len("three"),'4':len("four"),
                '5':len("five"),'6':len("six"),'7':len("seven"),
                '8':len("eight"),'9':len("nine"),'10':len('ten'),
                '11':len('eleven'),'12':len('twelve'),'13':len('thirteen'),
                '14':len('fourteen'),'15':len('fifteen'),'16':len('sixteen'),
                '17':len('seventeen'),'18':len('eighteen'),'19':len('nineteen'),
                '20':len('twenty'),'30':len('thirty'),'40':len('forty'),
                '50':len('fifty'),'60':len('sixty'),'70':len('seventy'),
                '80':len('eighty'),'90':len('ninety'),'100':len('hundred'),
                '1000':len('thousand'),'0':0,'00':0,'and':len('and')}

def numLetters(x):
    letterTotal=0
    x=str(x)
    if len(x)==4:
        letterTotal+=(dictNumLengths['1000']+dictNumLengths[x[0]])
    if len(x)>=3:
        if x[-3] != '0':
            letterTotal+=(dictNumLengths['100']+dictNumLengths[x[-3]])
            if (x[-2] !='0')|(x[-1] != '0'): letterTotal+=dictNumLengths['and']
    if len(x)>=2:
        if x[-2]=='1': letterTotal+=dictNumLengths[x[-2:]]
        else: letterTotal+=(dictNumLengths[x[-2]+'0']+dictNumLengths[x[-1]])
    elif len(x)==1:
        letterTotal+=dictNumLengths[x[-1]]

    return(letterTotal)


grandTotal=0

for y in range(1,1001):
    grandTotal+=numLetters(y)

print(grandTotal)

# A= 21124