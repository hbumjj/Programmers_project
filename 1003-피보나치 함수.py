# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:49:53 2024

@author: user
"""
n = 40

zeros = [0] * 41
ones = [0] * 41

zeros[0] = 1
ones[1] = 1

for i in range(2, n+1):
    
    zeros[i] = zeros[i-1] + zeros[i-2]
    ones[i] = ones[i-1] + ones[i-2]


N = int(input())
for _ in range(N):
    a = int(input())
    print(zeros[a], ones[a])