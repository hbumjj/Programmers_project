# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:22:05 2024

@author: user
"""

# 피보나치 수 5

n = int(input())

if n == 0:
    
    print(0)
    
else:
    
    first = 0
    second = 1
    
    for i in range(2, n+1):
        a = second
        second = first + second
        first = a
    
    print(second)