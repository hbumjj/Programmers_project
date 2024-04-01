# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:25:19 2024

@author: user
"""
N,M = 6, 6

matrix = [[0,0,0,0,0,0],[0,2,0,0,0,0],[0,0,0,0,6,0],[0,6,0,0,2,0],[0,0,0,0,0,0],[0,0,0,0,0,5]]

point = [[1,1],[3,4],[5,5]]
# =============================================================================
# 
# =============================================================================

N,M = map(int, input().split())

point = []
matrix = []

for i in range(N):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:
            point.append([i,j])
    matrix.append(a)


# =============================================================================
# 
# =============================================================================

from collections import deque
import copy

one = [[0],[1],[2],[3]]
two = [[0, 2],[1, 3]]
three = [[0, 1],[1,2],[2,3],[3,0]]
four = [[0, 1, 2],[1,2,3],[2,3,0], [3,0,1]]
five = [[0, 1, 2, 3]]

dic = {1:one, 2:two, 3:three, 4:four, 5:five}

def counter(matrix, i,j,direction):
    cc = [1,2,3,4,5]
    for way in direction:
        if way == 0: # 위
            for x in range(i-1,-1,-1):
                if matrix[x][j] == 6:
                    break;
                elif matrix[x][j] in cc:
                    pass
                else:
                    matrix[x][j] = "#"
                    
        elif way == 2: # 아래
            for x in range(i+1,N):
                if matrix[x][j] == 6:
                    break;
                elif matrix[x][j] in cc:
                    pass
                else:
                    matrix[x][j] = "#"
                    
        elif way == 3: # 왼
            for y in range(j-1,-1,-1):
                if matrix[i][y] == 6:
                    break;
                elif matrix[i][y] in cc:
                    pass
                else:
                    matrix[i][y] = "#"
        
        elif way == 1: # 우
            for y in range(j+1, M):
                if matrix[i][y] == 6:
                    break;
                elif matrix[i][y] in cc:
                    pass
                else:
                    matrix[i][y] = "#"
    return matrix


result = N*M

def count_zero(array):
    answer = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                answer += 1
    return answer
    
def DFS(level, matrix):
    global result
    matrix_copy = copy.deepcopy(matrix)
    if level == len(point):
        a = count_zero(matrix_copy)
        if result > a:
            result = a
        return
    
    p = point[level]
    camera = matrix[p[0]][p[1]]
    for i in dic[camera]:
        matrix_copy = counter(matrix_copy,p[0],p[1],i)
        DFS(level+1, matrix_copy)
        matrix_copy = copy.deepcopy(matrix)

level = 0
DFS(level, matrix)

print(result)


