# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:23:54 2024

@author: user
"""

# 첫번째 줄에 k, 두번째 줄부터 k개 줄을 걸쳐 갈수 없는 좌표 주어짐

avoid = []
N = int(input())
for i in N:
    cc = list(map(int,input().split()))
    avoid.append(cc)


dx_ = [-1,1,0,0]
dy_ = [0,0,-1,1]

def out_of_range(x,y):
    if x > 0 and y > 0 and x < 6 and y < 6:
        return True
    return False

def sum_visited(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return False
    return True

def BackTracking(a,b, visited):
    global count
        
    visited[a[0]-1][a[1]-1] = 1
    visited[b[0]-1][b[1]-1] = 1    
    
    
    if a == b:
        if sum_visited(visited) == True: 
            count += 1
            return
        else:
            return
        
    
    
    for adx, ady in zip(dx_,dy_):
        for bdx, bdy in zip(dx_,dy_):
            
            na = [a[0]+adx, a[1]+ady]
            nb = [b[0]+bdx, b[1]+bdy] # a,b가 이동한 좌표
            
            if out_of_range(na[0],na[1]) == True and out_of_range(nb[0],nb[1]) == True: # 범위를 벗어나지 않음
                if visited[na[0]-1][na[1]-1] == 0 and visited[nb[0]-1][nb[1]-1] == 0: # 방문하지 않아야함
                    
                    BackTracking(na, nb, visited)
                    
                    visited[na[0]-1][na[1]-1] = 0
                    visited[nb[0]-1][nb[1]-1] = 0
                        
a = [1,1]
b = [5,5]
count = 0
visited = [[0 for _ in range(5)] for _ in range(5)]

for c in avoid:
    visited[c[0]-1][c[1]-1] = 1

BackTracking(a,b, visited)
print(count)