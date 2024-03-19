# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:28:17 2024

@author: user
"""

# N = 5

# arr = [1000000, 1000000, 1000000, 1000000, 1000000]

# B, C = 5, 7



# N = 8

# arr = [5, 10,30,235,1,23, 24, 101]

# B, C = 10 ,3

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())


total = 0

for class_ in arr:
    people = class_ - B        
    
    if people <= 0:
        total+=1
    else:
        total += 1    
        if people%C == 0:
            total+=people//C
        else:
            total+=(people//C) + 1
            
print(total)


