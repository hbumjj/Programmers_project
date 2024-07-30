# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:18:03 2024

@author: rapa
"""

'''
여행
한국 도시 N
길이 있을 수도 없을 수도
여행 경로 가능한지 확인

예
5개 a-b b-c a-d b-d e-a
여행 계획
e c b c d

(e) a b (c) (b) (c) b (d)

입력
도시 개수 n
여행 계획에 속한 도시들 수 m

연결 정보

최종 계획 1,2,3
'''

'''
m은 최종 변수
'''
n = 3
direction = [[0,1,0],[1,0,1],[0,1,0]]
plan = [1,2,3]

'''
1(0)으로 시작
2(1)로 가야한다. 

0 -> 열 탐색 1인 곳을 찾는다.
append # 방문 하지 않은곳이라면,

dfs? bfs? 
'''


n = 3
direction = [[0,1,0],[1,0,1],[0,1,0]]
plan = [1,2,3]

# =============================================================================
# 
# =============================================================================

n = int(input())
m = int(input())

direction = []
for i in range(n):
    s = list(map(int, input().split()))
    direction.append(s)

plan = list(map(int, input().split()))

from collections import deque

def BFS(x, y):
    q = deque()
    q.append(x)
    visited = []; flag = False
    
    while q:
        if flag == True:
            break;
        xx = q.popleft()
        visited.append(xx) # 방문 완료        
        
        # 열 탐색
        for idx, t in enumerate(direction[xx]):
            if t == 1 and idx not in visited: # 연결되어 있다면
                q.append(idx)
            
            if idx == y: # 목적지라면
                flag = True
                break;
    return flag

for si in range(1, len(plan)):
    flag = BFS(plan[si-1]-1, plan[si]-1)
    if flag == False:
        break;

if flag == True:
    print("YES")
else:
    print("NO")


# 틀림






