# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:10:35 2024

@author: user
"""

# matric = [['C','C','P'],['C','C','P'],['P','P','C']]
# matric = [['Y','C','P','Z','Y'],['C','Y','Z','Z','P'],['C','C','P','P','P'],['Y','C','Y','Z','C'],['C','P','P','Z','Z']]
# criteria = matric

def row_counter(c):
    result = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if c[i][j] == c[i][j-1]:
                count+=1
            else:
                count = 1
            result = max(result, count)
    return result

def col_counter(c):
    result = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if c[j][i] == c[j-1][i]:
                count+=1
            else:
                count = 1
            result = max(result, count)
    return result

matric = []
N = int(input())
for i in range(N):
    a = list(map(str, input()))
    matric.append(a)

ant = 0

for x in range(N):
    for y in range(N):
        if y+1 < N:
            matric[x][y], matric[x][y+1] = matric[x][y+1], matric[x][y]
            
            a = row_counter(matric)
            b = col_counter(matric)
            ant = max(ant, a, b)
            matric[x][y], matric[x][y+1] = matric[x][y+1] , matric[x][y]
            
            
        if x+1 < N:
            matric[x][y], matric[x+1][y] = matric[x+1][y], matric[x][y]
            
            a = row_counter(matric)
            b = col_counter(matric)
            ant = max(ant, a, b)
            matric[x][y], matric[x+1][y] = matric[x+1][y], matric[x][y] 
               
print(ant)


