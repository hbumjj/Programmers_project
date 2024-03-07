# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:09:13 2024

@author: user
"""

# example
# a = 3
# b = 7

a,b = map(int,input().split())

result = 0
def D(number):
    idx = 0
    while number > 0:
        idx +=1
        number = number - idx
    return idx

for i in range(a, b+1):
    result += D(i)

print(result)
