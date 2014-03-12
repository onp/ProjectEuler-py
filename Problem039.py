# Project Euler Problem #39
# Integer Right Triangles
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

'''

maxSolutions = 0
maxAt = None
solutions = []

for p in range(10,1001):
    hMin = int((p*1.4)//3.4)
    hMax = p//2+1
    sols = []
    for h in range(hMin,hMax):
        h2 = h**2
        for a in range(1,(p-h)//2+1):
            b = p-h-a
            if h2 == a**2 + b**2:
                sol = sorted([h,a,b])
                if sol not in sols:
                    sols.append(sol)
    if len(sols) > maxSolutions:
        maxSolutions = len(sols)
        maxAt = p
        solutions = sols
        print(maxAt,maxSolutions)
                
    

    
    
# A = 840