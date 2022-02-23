# Euler Problem 045
# Started 22 February 2022

# Strategy
# Make list of pentagonal numbers
# For n from 1 to high number, check if
    # 3n + 1 in pentnum and 3n^2 + 2n + 1 in pentnum

import math


#Create array of pentagonal numbers
pentNums = [] #array of pentagonal numbers
gen = 1000000 #arbitrary range of how many pentnums generated
Dmin = 10000

for i in range(0,gen): # number of pentnums generated
    num = int((i+1)*(3*(i+1) - 1)/2)
    pentNums.extend([num]) #dynamically growing array
    #print(pentNums[i])

for a in range(1,gen): #range of values n tested
    for b in range(1,gen):
        valdif = 1/6 + math.sqrt(abs(2/3*(abs(6*a*b + 3*b*b - b)/2)+1/36))
        valsum = 1/6 + math.sqrt(abs(2/3*(abs(6*a*b + 3*b*b - b + 6*a*a - 2*a)/2)+1/36))
        #print(val)
        if abs(2/3*(6*a*b + 3*b*b - b)/2) > Dmin:
            break
        else:
            if valdif.is_integer() and valsum.is_integer() and abs(6*a*b + 3*b*b - b)/2 < Dmin:
                #Dmin = abs(pentNums[a+1]-pentNums[b+1])
                print(a, (3*a*a - a)/2, b, (3*b*b - b)/2)
        
        
        
print("Answer: ", Dmin)