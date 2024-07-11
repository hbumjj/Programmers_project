# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:30:56 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:04:56 2024

@author: rapa
"""

# 1012 유기농 배추

'''
입력
테스트 케이스: 2
가로길이 10
세로길이 8
배추 개수 17
나머지는 배추 좌표
'''
t = 2

m, n, bachu = 10, 8, 17

position = [[0,0],[1,0],[1,1],[4,2],[4,3],[4,5],[2,4],[3,4],[7,4],
       [8,4],[9,4],[7,5],[8,5],[9,5],[7,6],[8,6],[9,6]]

arr = [[0 for i in range(m)] for i in range(n)]
copy = [[0 for i in range(m)] for i in range(n)]

for p in position:   
    arr[p[1]][p[0]] = 1

# =============================================================================
# 
# =============================================================================


# global
from collections import deque

dx_ = [1, -1, 0, 0]
dy_ = [0, 0, 1, -1]

def BFS(x_, y_, copy):
    q = deque(); c = 1
    q.append([x_,y_])
    while q:
        x, y  = q.popleft()
        for dx, dy in zip(dx_, dy_):
            nx = x + dx; ny = y + dy
            if out_of_range(nx, ny) == True: # 범위안에 있을 것
                if copy[nx][ny] != 1 and arr[nx][ny] == 1: # 방문하지 않았을 것 + 배추가 있을 것
                    copy[nx][ny] = 1; c += 1
                    q.append([nx,ny])
    return c

def out_of_range(x,y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    else: return False

# =============================================================================
# 
# =============================================================================
t = int(input()) # 2
for problem in range(t):
    
    m, n, bachu = map(int, input().split())
    arr = [[0 for i in range(m)] for i in range(n)]
    copy = [[0 for i in range(m)] for i in range(n)]
    
    for num in range(bachu):
        p_y, p_x = map(int, input().split())
        arr[p_x][p_y] = 1
        
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and copy[i][j] != 1: # 방문하지 않았으면서 배추있으면 시작
                copy[i][j] = 1
                s = BFS(i, j, copy)
                result += 1
    
    print(result)
