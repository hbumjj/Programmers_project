

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:03:06 2024

@author: rapa
"""

'''
n개의 로프
병렬 연결 시, 로프에 걸리는 중량 나눈다
k개 중량 w -> 각 로프에 w/k 골고루

입력
정수 2
2개 줄에 각각 버틸 수 있는 최대 중량

'''


n = 2

arr = [10, 15]

arr = [10, 15, 20, 2, 40, 100]

# =============================================================================
# 
# =============================================================================
n = int(input()); ans = 0; arr = []

for i in range(n):
    in_ = int(input())
    arr.append(in_)

r_arr = sorted(arr, reverse = True)

nn = 1
for c in r_arr:
    # c는 현재 최소값
    result = c * nn
    nn += 1
    
    ans = max(ans, result)
print(ans)