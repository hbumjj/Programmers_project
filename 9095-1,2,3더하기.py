# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:03:08 2024

@author: user
"""

def cal(n):
    arr = [0] * n
    arr[0] = 1; arr[1] = 2; arr[2] = 4
    
    for i in range(3, n): # 4~n
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    
    return arr

n = 10
arr = cal(n)

N = int(input())

for s in range(N):
    a = int(input())
    print(arr[a-1])
