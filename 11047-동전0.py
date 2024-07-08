# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:51:59 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:13:36 2024

@author: rapa
"""

'''
백준 11047 - 동전 0

총 N 종류 - 매무 많이 각각
가치의 합을 k
최소개수?
'''
# 시간 초과
# N, K = 10, 4200
# 100,000,000
# arr = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

arr = []
N, K = map(int, input().split())
for i in range(N):
    arr.append(int(input()))

r_arr = arr[::-1]

idx = 0; result = 0
while idx < len(arr):
    if K == 0:
        break;
    if r_arr[idx] > K:
        idx += 1
    else: # 만약에 구간에 속한다면
        c = (K//r_arr[idx])
        K -= (r_arr[idx] * c)
        result += c

print(result)
# result = 6