# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:57:37 2024

@author: rapa
"""

'''

백준 2667: 단지번호붙이기


빈 배열 만들고, 방문시 True

단지수 계산

0,0시작  - 1 -> 0이 된다면 + 1 

if True -> False가 된다면 result += 1

dfs로 수행

3
7
8
9
'''

N = 7
arr = [0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1] \
    ,[0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,0,0,0]

# =============================================================================
# 
# =============================================================================
from collections import deque

N = int(input())

arr = []
for i in range(N):
    #ls_ = list(map(int, input().split()))
    ls_ = list(map(int, list(input())))
    arr.append(ls_)

    
copy_arr = [[0 for i in range(N)] for i in range(N)]

dx_ = [0, 0, -1, 1]
dy_ = [1, -1, 0, 0]

def out_of_range(x, y): # 0 ~ 6
    if x <= N-1 and x >= 0 and y <= N-1 and y >= 0:
        return True
    else: return False

def BFS(x_, y_, copy_arr):
    q = deque()
    q.append([x_,y_]); c = 1
    copy_arr[x_][y_] = 1
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dx_, dy_):
            nx = x + dx; ny = y + dy
            if out_of_range(nx, ny) == True: # 벗어나지 않은곳
                if copy_arr[nx][ny] == 0 and arr[nx][ny] == 1: # 방문하지 않으면서, 거주지인곳    
                    c += 1
                    copy_arr[nx][ny] = 1
                    q.append([nx, ny])
    return c

result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and copy_arr[i][j] == 0:
            c = BFS(i,j, copy_arr)
            result.append(c) 

print(len(result))

sorted_result = sorted(result)

for x in sorted_result:
    print(x)