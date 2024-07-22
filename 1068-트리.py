# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:39:29 2024

@author: user
"""
'''
5
-1 0 0 1 1
2
'''
from collections import deque

n = int(input())

dir = {}
for i in range(-1, n):
    dir[i] = []

arr = list(map(int, input().split()))

for j in range(0, n):
    dir[arr[j]].append(j)

cut = int(input())

def BFS(x):
    ans = 0;
    q = deque()
    q.append(x)
    while q:
        s = q.popleft()
        for ss in s:
            if cut != ss:
                q.append(dir[ss])
                if dir[ss] == []:
                    ans += 1
            elif cut == ss and len(s) == 1:
                ans += 1
    return ans

a = BFS(dir[-1])
if dir[-1] == [cut]:
    print(0)
else:
    print(a)
