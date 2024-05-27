# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:44:44 2024

@author: rapa
구간합구하기 5 11660
"""
from collections import deque

n =  4


matrix = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]

# =============================================================================
# 
# =============================================================================


# =============================================================================
# 시간초과
# =============================================================================

def cal(start, end, matrix):
    x = start[0]; y = start[1]
    ex = end[0]; ey = end[1]
    
    q = deque()
    q.append((x,y))
    visited[x-1][y-1] = 1
    sum_ = matrix[x-1][y-1]
    
    dx_ = [1, 0]; dy_ = [0 ,1]
    
    while q:
        popq = q.popleft()
        x = popq[0]; y= popq[1]
        for dx, dy in zip(dx_, dy_):
            nx = x + dx; ny = y + dy
            if nx <= ex and ny <= ey and visited[nx-1][ny-1] == 0:
                q.append((nx,ny))
                visited[nx-1][ny-1] = 1
                sum_ += matrix[nx-1][ny-1]
            if nx == ex and ny == ey:
                break;    
    return sum_

# =============================================================================
# 입력
# =============================================================================
n, m = map(int,input().split())
matrix = []

for i in range(n):
    a = list(map(int,input().split()))
    matrix.append(a)

for j in range(m):
    visited = [[0] * n for _ in range(n)]
    
    point = list(map(int,input().split()))
    start = [point[0], point[1]]
    end = [point[2], point[3]]
    
    s = cal(start, end , matrix)
    print(s)