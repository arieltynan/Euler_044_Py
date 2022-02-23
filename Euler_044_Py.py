# Euler Problem 045
# Started 22 February 2022

# Strategy
# Make list of pentagonal numbers
# For n from 1 to high number, check if
    # 3n + 1 in pentnum and 3n^2 + 2n + 1 in pentnum

#Create array of pentagonal numbers
pentNums = [] #array of pentagonal numbers
gen = 10000 #arbitrary range of how many pentnums generated
Dmin = 100000

for i in range(0,gen): # number of pentnums generated
    num = int((i+1)*(3*(i+1) - 1)/2)
    pentNums.extend([num]) #dynamically growing array
    #print(pentnums[i])

for a in range(1,len(pentNums)): #range of values n tested
    for b in range(a + 1,len(pentNums)):
        if (pentNums[a] + pentNums[b])/2 in pentNums and (pentNums[a] - pentNums[b])/2 in pentNums and pentNums[a] < Dmin: # a is dif, b is sum of two pent nums
            Dmin = pentNums[a]
            print(pentNums[a], pentNums[b])
        
print("Answer: ", Dmin)






# Design
# Create array of pentagonal numbers
# For each new pent num, check sum and difference of each and every other pent nums in list to confirm if pent
