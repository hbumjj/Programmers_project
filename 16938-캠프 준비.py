# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:03:29 2024

@author: user
"""

'''
N개의 문제 - i 번째 문제의 난이도는 Ai

캠프 사용할 문제 - 두 문제 이상
문제 난이도 합은 L 보다 크거나 같고, R 보다 작거나 같다
가장 어려운 - 쉬운 난이도 차이는 x 보다 크거나 같다.

'''
# N, L, R, X = 5, 25, 35,10

# p = [10, 10, 20, 10, 20]

# 최소 2문제


N, L, R, X = map(int, input().split())

p = list(map(int, input().split()))

from itertools import combinations
count = 0
for i in range(2, N+1): # 문제 수
    # 문제수 만큼, 조합수뽑기
    check = list(combinations(p, i))
    #print(check)
    for c in check:
         cc = sum(c); max_c = max(c); min_c = min(c)
         if cc>=L and cc<=R and (max_c-min_c) >= X:
             count+=1

print(count)