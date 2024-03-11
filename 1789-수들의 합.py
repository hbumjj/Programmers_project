# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:03:41 2024

@author: user
"""

n = int(input())

idx = 1
result = 1


while True:

    
    if result > n:
        break
    
    idx+=1
    result+=idx    

print(idx-1)