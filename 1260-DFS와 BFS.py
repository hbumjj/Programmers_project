# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:55:44 2024

@author: user
"""

# DFS와 BFS

number, lines, start = [5,5,3] # 입력예시
'''
방문 노드
5 4
5 2
1 2
3 4
3 1
'''
visit = [0, 0, 0, 0, 0]
# =============================================================================
# 
# =============================================================================
# Input
number, lines, start = map(int,input().split())
graph = [[0]*(number+1) for i in range(number+1)]
for i in range(lines):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visit1 = [0 for i in range(number + 1)] # DFS 결과를 위한
visit2 = [0 for i in range(number + 1)] # BFS 결과를 위한

# =============================================================================
# DFS
# =============================================================================
def DFS(graph, visit, start):
    print(start, end =' ') # 출력값
    visit[start] = 1 # 방문 시 1로 변경
    for node in range(1, number+1):
        if visit[node] == 0 and graph[start][node] == 1: # 도착지가 방문하지 않았으면서, 연결된 노드인 경우
            DFS(graph, visit, node) # 재귀

DFS(graph, visit1, start)
print()

# =============================================================================
# BFS
# =============================================================================

from collections import deque 
def BFS(graph, visit, start):
    visit[start] = 1 # 방문 시 1로 변경
    new_visit = deque([start])
    while new_visit:
        ss = new_visit.popleft() # deque의 pop(0)
        print(ss, end = ' ') # 출력값
        for node in range(1, number+1):
            if visit[node] == 0 and graph[ss][node] == 1: # 도착지가 방문하지 않았으면서, 연결된 노드인 경우
                new_visit.append(node) # 이후에 방문할 요소들을 추가
                visit[node] = 1 # 도착지를 방문으로 변경
                
BFS(graph, visit2, start)
print()

    
