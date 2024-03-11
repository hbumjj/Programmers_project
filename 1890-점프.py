# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:14:42 2024

@author: user
"""
# DP - 동적 프로그래밍
# n = 4
# matric = [[2,3,3,1],[1,2,1,3],[1,2,3,1],[3,1,1,0]]
# copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

matric = []
n = int(input())

for i in range(n):
    arr = list(map(int,input().split()))
    matric.append(arr)

copy = [[0 for _ in range(n)] for _ in range(n)]
copy[0][0] = 1 # 처음 시작점을 정의

for x in range(0, n):
    for y in range(0, n): # 좌표 X, Y 결
        
        if x == n-1 and y == n-1:
            break; # 마지막에 정지. 추가 진행 X
        
        move = matric[x][y] # 매트릭스의 이동 간격
        
        if x + move < n: # INDEX 오류 방지
            copy[x+move][y] += copy[x][y] # 기존에 갔던거에 추가
    
        if y + move < n:
            copy[x][y+move] += copy[x][y]
        
print(copy[n-1][n-1])