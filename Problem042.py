# Project Euler Problem #42
# Coded Triangle Numbers
'''
The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

'''

words = None

with open('words.txt','r') as file:
    words = file.read()[1:-2].split('","')

alpha = '.abcdefghijklmnopqrstuvwxyz'
alphaValues = {}
for i,a in enumerate(alpha):
    alphaValues[a] = i
del alphaValues['.']
    
triangleValues = [1]

def isTriangle(x):
    while x>triangleValues[-1]:
        n = len(triangleValues)+1
        nextTri = int(n*(n+1)/2)
        triangleValues.append(nextTri)
        
    if x in triangleValues:
        return True
    
    return False
        
triangleWordCount = 0

for word in words:
    val = 0
    word=word.lower()
    for letter in word:
        val += alphaValues[letter]
    if isTriangle(val):
        triangleWordCount +=1

        
print(triangleWordCount)

    
# A = 162