# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:10:09 2024

@author: user
"""

N, L = 6, 2

matrix = [[3,3,3,3,3,3],[2,3,3,3,3,3],[2,2,2,3,2,3],[1,1,1,2,2,2],[1,1,1,3,3,1],[1,1,2,3,3,2]]
matrix = [[3,2,1,1,2,3],[3,2,2,1,2,3],[3,2,2,2,3,3],[3,3,3,3,3,3],[3,3,3,3,2,2],[3,3,3,3,2,2]]

total = int(N*2)
arr = [3,2,2,1,1,1]
# =============================================================================
# 
# =============================================================================

N,L = map(int, input().split())
matrix = []
for i in range(N):
    a = list(map(int,input().split()))
    matrix.append(a)

def search(arr):
    visited = [False] * len(arr)
    for i in range(0, len(arr)-1):

        if arr[i] == arr[i+1]:
            continue
        elif abs(arr[i+1] - arr[i]) > 1:
            return False
        
        elif arr[i+1] - arr[i] == 1: # 왼쪽에 경사로 설치
            for index in range(i-L+1, i+1):
                if index < 0:
                    return False
                elif arr[i+1] - arr[index] == 1 and visited[index] == False:
                    visited[index] = True
                else:
                    return False
                
        elif arr[i+1] - arr[i] == -1: # 오른쪽에 경사로 설치
            for index in range(i+1, i+L+1):
                if index >= len(arr):
                    return False
                elif arr[i] - arr[index] == 1 and visited[index] == False:
                    visited[index] = True
                else:
                    return False
        
    return True
        
# a = search(arr)
# print(a)

total = 0
for x in range(N):
    cols = []
    
    for y in range(N):
        cols.append(matrix[y][x])
    arr = (matrix[x]) # 행검사
    r = search(arr)
    if r == True:
        total+=1
    #print(arr, r)
    r = search(cols)
    if r == True:
        total +=1
    #print(cols, r)
    
print(total)