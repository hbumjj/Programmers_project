# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:31:42 2024

@author: user
"""
# N = 6
# arr_x = [3,15,17]
# arr_y = ['D', 'L', 'D']
# apple = [[2,3],[1,4],[4,2]]
# visit = [0, 0, 0]

# N = 10
# arr_x = [8,10,11,13]
# arr_y = ['D' ,'D', 'D', 'L']
# apple = [[0,1],[0,2],[0,3],[0, 4]]
# visit = [0, 0, 0, 0]

# N = 8
# arr_x = [2,8,10,12,18,20,22,24,25,28,32,33]
# arr_y = ['D' ,'D', 'D', 'D','L','L','L','L','L','L','D','L']
# print(len(arr_x), len(arr_y))
# apple = [[5,0],[6,2],[2,4],[4, 6],[4,5]]
# visit = [0, 0, 0, 0, 0]


N = int(input())

num = int(input())
apple = []
for i in range(num):
    x,y = map(int,input().split())
    apple.append([x-1,y-1])

visit = [0]*num

    
num = int(input())
arr_x = []
arr_y = []
for i in range(num):
    a = list(input().split())
    arr_x.append(int(a[0]))
    arr_y.append(a[1])
    

# =============================================================================
# 
# =============================================================================
def rotation(pre_way, direction):
    
    if pre_way == 1:
        if direction == 'D':
            way = 3
        if direction == 'L':
            way = 2
        
    elif pre_way == 0:
        if direction == 'D':
            way = 2
        if direction == 'L':
            way = 3
            
    elif pre_way == 2:
        if direction == 'D':
            way = 1
        if direction == 'L':
            way = 0
            
    else:
        if direction == 'D':
            way = 0
        if direction == 'L':
            way = 1
    
    return way

from collections import deque

dx = [1,-1,0,0] # down, up, left, right
dy = [0,0,-1,1]

way = 3
point = deque()
hx, hy = 0, 0
point.append([hx, hy])

time = 0

while True:
    
    #print(point)
    time+=1
    hx = hx + dx[way]
    hy = hy + dy[way]
    if hx < 0 or hx >= N or hy < 0 or hy >= N or [hx,hy] in point:
        break;
        
    point.append([hx, hy])
    
    if [hx, hy] in apple and visit[apple.index([hx,hy])] == 0:
        visit[apple.index([hx,hy])] = 1 
        
    else:
        point.popleft()
          
        
    if time in arr_x:
        way = rotation(way, arr_y[arr_x.index(time)])

print(time)
    