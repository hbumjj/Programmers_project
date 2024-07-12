# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 01:39:19 2024

@author: user
"""

# 1931 회의실 배정
n = int(input())
arr = []
for i in range(n):
    ch = list(map(int, input().split()))
    arr.append(ch)

# 끝나는 시간을 기준으로 정렬
dev_arr = sorted(arr,  key = lambda x: (x[1], x[0]))
# print(dev_arr)


# for문 하나만 
point = dev_arr[0][1] # 뒷부터 시작 시점 
c = 1
for start in dev_arr[1:]:
    p = start[0] # 앞부분을 결정 시점
    if p >= point:
        point = start[1]; c+= 1
        # print(start)

print(c)