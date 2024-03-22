# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:31:39 2024

@author: user
"""

N, M = 5, 5

matrix = [[1,2,3,4,5],[5,4,3,2,1],[2,3,4,5,6],[6,5,4,3,2],[1,2,1,2,1]]
totalmax = 6

# N, M = 4, 10
# matrix = [[1,2,1,2,1,2,1,2,1,2],[2,1,2,1,2,1,2,1,2,1],[1,2,1,2,1,2,1,2,1,2],[2,1,2,1,2,1,2,1,2,1]]

# N, M =4,5
# matrix = [[5,5,5,5,5],[5,100,1,1,100],[5,5,5,5,5],[5,5,5,5,5]]
# totalmax = 100

# N, M = 3,3
# matrix=[[1,1,1],[0,1,0],[0,0,0]]
# totalmax = 1
# =============================================================================
# 
# =============================================================================
matrix = []

N,M = map(int,input().split())
totalmax = 0

for i in range(N):
    a = list(map(int,input().split()))
    matrix.append(a)    
    totalmax = max(totalmax, max(a))

# =============================================================================
# 
# =============================================================================
from collections import deque


nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
def BFS(i,j):
    arr = deque()
    
    arr.append([[(i, j)], matrix[i][j]])
    
    ans = 0
    
    while arr:
        path, val = arr.popleft()
        for dx, dy in path:
            for i in range(4):
                x = dx + nx[i]
                y = dy + ny[i]
                
                if x >= 0 and y >= 0 and x < N and y < M:
                    if (x, y) not in path:
                        new_path = path + [(x, y)]
                        new_val = val + matrix[x][y]
                        
                        if len(new_path) == 4:
                            ans = max(ans, new_val)
                        else:
                            arr.append([new_path,new_val])
    return ans

maxval = totalmax + 3

for i in range(N):
    for j in range(M):
        if matrix[i][j]*4 > maxval:
            a = BFS(i,j)
            maxval = max(maxval,a)
            
print(maxval)


























'''
def BFS(i,j):
    arr = deque()
    visit = []
    arr.append([1,matrix[i][j],i,j])
    ans = 0
    
    flag = True
    while arr:
        print(arr)
        depth, value, dx, dy = arr.popleft()
        
        visit.append([dx,dy])
        for i in range(4):
            x = dx + nx[i]
            y = dy + ny[i]
            if [x, y] not in visit:
                if x >= 0 and y >= 0 and x < N and y < M:
                    
                    
                    if depth == 2 and flag == True:
                        exc_x = dx + ny[i]
                        exc_y = dy + nx[i]
                        if exc_x >= 0 and exc_y >= 0 and exc_x < N and exc_y < M:
                            if [exc_x, exc_y] not in visit:
                                #arr.append([4, value + matrix[x][y] + matrix[exc_x][exc_y], x, y])
                                arr.append([3, value + matrix[exc_x][exc_y], x, y])
                        else:
                            pass
                        print(exc_x, exc_y)
                        print()
                        exc_x = dx - ny[i]
                        exc_y = dy - nx[i]
                        if exc_x >= 0 and exc_y >= 0 and exc_x < N and exc_y < M:
                            if [exc_x, exc_y] not in visit:
                                #arr.append([4, value + matrix[x][y] + matrix[exc_x][exc_y], x, y])
                                arr.append([3, value  + matrix[exc_x][exc_y], x, y])
                                
                        else:
                            pass
                        print(exc_x, exc_y)
                        print()
                        flag = True
                        
                    
                    if depth == 4:
                        ans = max(ans, value)
                        break;
                    else:
                        arr.append([depth+1, value + matrix[x][y], x, y])

    return ans
'''


        