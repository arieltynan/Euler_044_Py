# Euler Problem 045
# Started 22 February 2022

# Strategy
# Make list of pentagonal numbers
# For n from 1 to high number, check if
    # 3n + 1 in pentnum and 3n^2 + 2n + 1 in pentnum

import math


#Create array of pentagonal numbers
pentNums = [] #array of pentagonal numbers
gen = 100000 #arbitrary range of how many pentnums generated
Dmin = gen*gen

for i in range(0,gen): # number of pentnums generated
    num = int((i+1)*(3*(i+1) - 1)/2)
    pentNums.extend([num]) #dynamically growing array
    #print(pentNums[i])

for a in range(1,gen): #range of values n tested
    for b in range(1,gen):
        penta = int(a*(3*a - 1)/2)
        pentb = int(b*(3*b - 1)/2)
        if abs(pentb - penta) > Dmin:
            break

        else:
            #print(penta, pentb)
            valdif = 1/6 + math.sqrt(abs(2/3*(abs(pentb - penta)+1/36)))
            valsum = 1/6 + math.sqrt(abs(2/3*(abs(pentb + penta)+1/36)))
            #print(val)
            if valdif.is_integer() and valsum.is_integer() and abs(pentb - penta) < Dmin:
                #Dmin = abs(pentNums[a+1]-pentNums[b+1])
                print(a, penta, b, pentb)
        
        
        
print("Answer: ", Dmin)