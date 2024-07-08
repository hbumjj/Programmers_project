# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:06:12 2024

@author: rapa
"""

N = 7

# start = [1, 2, 1, 5, 5, 4]
# end =   [2, 3, 5, 2, 6, 7]

'''
input:
7
6
2 3
4 5
6 7
6 5
4 3
2 1
output: 3
answer: 6

# 백준 2606 - 바이러스
'''
start = [2, 4, 6, 6, 4, 2]
end =   [3, 5, 7, 5, 3, 1]

########################

N = int(input())
C = int(input())
start = []; end = []

for i in range(C):
    a,b = map(int, input().split())
    start.append(a)
    end.append(b)

point = 1
arr = []

def DFS(point, arr):
    arr.append(point)
    # forward
    for f_idx in range(len(start)):
        if start[f_idx] == point: # 시작 포인트
            destination = end[f_idx]
            if destination not in arr:
                DFS(destination, arr)
    
    # backward
    for b_idx in range(len(end)):
        if end[b_idx] == point: # 시작 포인트
            destination = start[b_idx]
            if destination not in arr:
                DFS(destination, arr)

DFS(1, arr)
print(len(arr)-1)