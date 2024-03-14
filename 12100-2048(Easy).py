# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:54:45 2024

@author: user
"""
N = 3
matrix = [[2,2,2],[4,4,4],[8,8,8]]


N = 4
matrix = [[4,2,0,0],[0,0,0,0],[0,0,0,0],[2,0,0,0]]


# N = 5
# matrix = [[2,0,0,0,0],[2,0,0,0,0,0],[4,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0]]

# N = 4
# matrix = [[2,2,4,16],[0,0,0,0,0],[0,0,0,0],[0,0,0,0]]


# =============================================================================
# Input
# =============================================================================

N = int(input())

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))


# =============================================================================
# 방향에 따른 arr 값을 출력해주는 함수들
# =============================================================================
def left(arr):
    for i in range(N):
        crit = 0
        for j in range(1, N):
            if arr[i][j] != 0:
                tmp = arr[i][j]
                arr[i][j] = 0
            
                if tmp == arr[i][crit]:
                    arr[i][crit]+=tmp
                    crit += 1
                elif arr[i][crit] == 0:
                    arr[i][crit] = tmp
                else:
                    arr[i][crit+1] = tmp
                    crit += 1
    return arr

def up(arr):
    for j in range(N):
        crit = 0
        for i in range(1, N):
            if arr[i][j] != 0:
                tmp = arr[i][j]
                arr[i][j] = 0
            
                if tmp == arr[crit][j]:
                    arr[crit][j]+=tmp
                    crit += 1
                elif arr[crit][j] == 0:
                    arr[crit][j] = tmp
                else:
                    arr[crit+1][j] = tmp
                    crit += 1
    return arr

def right(arr):
    for i in range(N):
        crit = N-1
        for j in range(N-2, -1, -1):
            if arr[i][j] != 0:
                tmp = arr[i][j]
                arr[i][j] = 0
            
                if tmp == arr[i][crit]:
                    arr[i][crit]+=tmp
                    crit -= 1
                elif arr[i][crit] == 0:
                    arr[i][crit] = tmp
                else:
                    arr[i][crit-1] = tmp
                    crit -= 1
    return arr

def down(arr):
    for j in range(N):
        crit = N-1
        for i in range(N-2, -1, -1):
            if arr[i][j] != 0:
                tmp = arr[i][j]
                arr[i][j] = 0
            
                if tmp == arr[crit][j]:
                    arr[crit][j]+=tmp
                    crit -= 1
                elif arr[crit][j] == 0:
                    arr[crit][j] = tmp
                else:
                    arr[crit-1][j] = tmp
                    crit -= 1
    return arr

# =============================================================================
# 알고리즘 - 백트래킹
# =============================================================================

import copy


result = 2
def DFS(depth, arr):
    global result
    
    if depth == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > result:
                    result = arr[i][j]
        #print(arr)
        return
    
    
    # for i in range(4):
    #     copy_arr = copy.deepcopy(arr)
    #     if i == 0:
    #         DFS(depth + 1, left(copy_arr))
    #     elif i == 1:
    #         DFS(depth + 1, right(copy_arr))
    #     elif i == 2:
    #         DFS(depth + 1, up(copy_arr))
    #     else:
    #         DFS(depth + 1, down(copy_arr))
    
    else:
        copy_arr = copy.deepcopy(arr)
        DFS(depth+1, left(copy_arr))
        
        copy_arr = copy.deepcopy(arr)
        DFS(depth+1, right(copy_arr))
        
        copy_arr = copy.deepcopy(arr)
        DFS(depth+1, up(copy_arr))
        
        copy_arr = copy.deepcopy(arr)
        DFS(depth+1, down(copy_arr))
        
            
DFS(0, matrix)
print(result)

# copy_arr = copy.deepcopy(matrix)
# copy_arr = left(copy_arr) 
# print(copy_arr)

# copy_arr = copy.deepcopy(matrix)
# copy_arr = right(copy_arr) 
# print(copy_arr)

# copy_arr = copy.deepcopy(matrix)
# copy_arr = up(copy_arr) 
# print(copy_arr)

# copy_arr = copy.deepcopy(matrix)
# copy_arr = down(copy_arr) 
# print(copy_arr)
