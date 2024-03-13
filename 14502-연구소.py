# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:56:29 2024

@author: user
"""

# N,M = 7,7

# matrix = [[2,0,0,0,1,1,0], [0,0,1,0,1,2,0], [0,1,1,0,1,0,0], [0,1,0,0,0,0,0],
#        [0,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0]]

# point = [[0, 1], [0, 2], [0, 3], [0, 6], [1, 0], [1, 1], [1, 3], [1, 6], [2, 0], [2, 3], [2, 5], [2, 6], [3, 0], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 0], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [6, 0], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]


N,M = map(int,input().split())
matrix = []
point = []
for i in range(N):
    ar = list(map(int,input().split()))
    matrix.append(ar)
    for j in range(M):
        if ar[j] == 0:
            point.append([i,j]) # 벽을 세울수 있는 좌표를 미리 저장

from itertools import combinations
from collections import deque
import copy


def BFS(i,j,arr):
    virus = 0
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]
    
    queue = deque()
    queue.append([i,j])
    
    while queue:
        fac = queue.popleft()
        for dx, dy in zip(x,y):
            nx = fac[0] + dx 
            ny = fac[1] + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: # 인덱스 벗어날시 계속
                continue
            if arr[nx][ny] == 1: # 1도 무시
                continue
            if arr[nx][ny] == 0: # 0일때 감염
                arr[nx][ny] = 2
                queue.append([nx, ny])
                virus += 1
    return virus

if_num = list(combinations(point, 3)) # 3가지 좌표를 뽑았을때 가능한 경우에 수 전부 찾기
result = N*M

for if_ in if_num:
    pre = copy.deepcopy(matrix) # 깊은 복사
    
    for wall in if_:
        pre[wall[0]][wall[1]] = 1 # 벽 세우기
    
    virusCount = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2: # 2일때 BFS 실행 (감염 시작)
                virusCount+=BFS(i,j, pre) # 감염된 지점 더해주기
    if virusCount < result: # 결과 계산
        result = virusCount 

print(len(point) - result- 3)


# =============================================================================
# 백트래킹을 이용해서 더욱 효과적으로 해결도 가
# =============================================================================
