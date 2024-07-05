# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:07:04 2024

@author: rapa
"""

'''
세준 N개 빨대 중 3개 -> 세변의 길이 합 최대
두 변의 합이 한 변보다 크다 
'''
import sys

N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)

answer = -1
c = False
for idx in range(N-3+1):
    check = arr[idx: idx + 3]
    if check[0] < check[1] + check[2]:
        answer = sum(check)
        break;
    
print(answer)