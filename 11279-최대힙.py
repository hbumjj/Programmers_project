# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 01:10:08 2024

@author: user
"""



import sys
import heapq


N = int(input())
arr = []


for i in range(N):
    a = int((sys.stdin.readline()))
    
    
    if a != 0:
        heapq.heappush(arr, -1*a)

    elif a == 0:
        if arr:
            x = heapq.heappop(arr)
            print(-1*x)
        else:
            print(0)
    