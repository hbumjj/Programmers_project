# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:13:18 2024

@author: user
"""

n = int(input())

a = 1
b = 1

# 1,1,2,3,5,8...

for i in range(2, n):
    b,a = a + b,b

print(b)
    