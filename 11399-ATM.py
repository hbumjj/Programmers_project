# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:58:39 2024

@author: user
"""

# 1~N까지 줄서있음
# P분걸림. 
# 시간 최소로

# 최소로 걸릴려면, 한 사람이 가장 짧게 해서 진행해야한다.

N = 5

time = [3,1,4,3,2]



N = int(input())
time = list(map(int, input().split()))

time = sorted(time)


idx = 1; answer = 0
for person in range(N):
    p_an = 0
    for i in time[:idx]:
        p_an += i
    idx += 1
    answer += p_an

print(answer)