# Euler Problem 045
# Started 22 February 2022

# P_n = n(3n - 1)/2
## Based on paper calculations
# P_n+1 - P_n = 3n + 1
# P_n+1 + P_n = 3n^2 + 2n + 1

# Strategy
# Make list of pentagonal numbers
# For n from 1 to high number, check if
    # 3n + 1 in pentnum and 3n^2 + 2n + 1 in pentnum

#Create array of pentagonal numbers
pentNums = [] #array of pentagonal numbers
gen = 1000000 #arbitrary range of how many pentnums generated
numsTested = 150000 #arbitary range of numbers tested

Dmin = 1000000
for i in range(0,gen): # number of pentnums generated
    num = int((i+1)*(3*(i+1) - 1)/2)
    pentNums.extend([num]) #dynamically growing array
    #print(pentnums[i])

for n in range(120000,numsTested): #range of values n tested
    for x in (range(1,gen-n)): # k is distance between two numbers in list of pentnums (x)
        #dif = (5*j*k + 2*k + j)//2
        if (6*n*x + 3*x*x - x)//2 > Dmin:
            break
        else:
            if (6*n*x + 3*x*x - x)//2 in pentNums and (6*n*n + 6*n*x + 3*x*x - 2*n - x)//2 in pentNums and (6*n*x + 3*x*x - x)//2 < Dmin:
                Dmin = (6*n*x + 3*x*x - x)//2
                print(Dmin, n, pentNums[n - 1], n + x, pentNums[n + x - 1])
        

## for j in reversed(pentnums): #iterating through growing list of pentnums
#    if abs(pentnums[i] - j) > Dmin:
#        #print(abs(pentnums[i] - j))
#        #print(i,j)
#        break
#    else:
#        if pentnums[i] != j:
#            if (pentnums[i] - j) in pentnums and (pentnums[i] + j) in pentnums:
#                    Dmin = abs(pentnums[i] - j)
#                    print(Dmin, "\n")
#            break

print("Answer: ", Dmin)






# Design
# Create array of pentagonal numbers
# For each new pent num, check sum and difference of each and every other pent nums in list to confirm if pent
