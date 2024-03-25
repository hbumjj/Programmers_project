# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:09:15 2024

@author: user
"""

N,M = 11, 10

x, y, direction = 7, 4, 0
# 0: 북쪽    1: 동쪽    2: 남쪽     3: 서쪽

matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 1, 1, 1, 1, 0, 1],[1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 1, 1, 1 ,1, 1, 1, 1, 1, 1]]

# =============================================================================
# 
# =============================================================================

N, M = map(int,input().split())
matrix = []
x, y, direction = map(int,input().split())

for i in range(N):
    a = list(map(int, input().split()))
    matrix.append(a)

# =============================================================================
# 
# =============================================================================
from collections import deque

dx = [1,-1,0,0] # 남, 북, 서, 동
dy = [0,0,-1,1]


answer = 0

def not_cleaning(x, y, way, matrix):
    if way == 0: #북
        idx = 0; way = 2#남
        
    elif way == 1: #동
        idx = 2; way = 3#서

    elif way == 2: #남
        idx = 1; way = 0# 북
        
    else: # 서
        idx = 3; way = 1# 동
    
    nx = x + dx[idx]
    ny = y + dy[idx]
    
    if matrix[nx][ny] == 2 or matrix[nx][ny] == 0:
        return [nx, ny, way]
    else:
        return False

def cleaning(x, y, way, matrix):
    # 방향전환
    FLAG = True
    while FLAG:
        if way == 0:
            idx = 2; way = 3
        elif way == 1:
            idx = 1; way = 0
        elif way == 2:
            idx = 3; way = 1
        else:
            idx = 0; way = 2
        
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if matrix[nx][ny] == 0:
            FLAG = False
            return nx, ny, way
    
def BFS(x, y, direction):
    global answer
    queue = deque()
    queue.append([x,y])
    flag = False
    while queue:
        x,y = queue.popleft()
#        print(x,y, "  ", direction)
        answer += 1
        matrix[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if matrix[nx][ny] == 0:
                flag = True
                break;
        # 4방향 탐색. # flag = true면 청소할 곳이 있음, flag = False면 청소할 곳 없음
        #print(flag)
        if flag == True:
            nx_, ny_, direction = cleaning(x,y,direction, matrix)
            queue.append([nx_,ny_])
            
        elif flag == False: 
            re = not_cleaning(x,y,direction, matrix)
            if re == False:
                break;
            else:
                queue.append([re[0], re[1]])
                answer -= 1
    
        flag = False
    print(answer)
    #print(matrix)
BFS(x, y, direction)