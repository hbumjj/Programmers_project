# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:41:37 2024

@author: user
"""

N, K = map(int, input().split())

n = []

# example
# 1,2,3,6

# N = 6
# K = 3
 
# =============================================================================
# 
# =============================================================================
for check in range(1, N+1):
    if N%check == 0:
        n.append(check)
try:
    print(n[K-1])
except:
    print(0)