# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:49:33 2024

@author: user
"""

import sys
from collections import deque

input = sys.stdin.readline
V = int(input())
tree = [[] for _ in range(V+1)]
# 2차원 리스트에 트리 저장(연결 그래프)
for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

# tree = [[], [(3, 2)], [(4, 4)], [(1, 2), (4, 3)], [(2, 4), (3, 3), (5, 6)], [(4, 6)]]
# V = 5

def BFS(start):
    queue = deque()
    queue.append((start, 0))
    visited = [0] * (V+1)
    visited[start] = 1
    res = [0,0]
    
    while queue:
        q = queue.popleft()
        point = q[0]; distance = q[1]
        for p, d in tree[point]:
            if visited[p] == 0:
                next_d = distance + d
                queue.append((p, next_d))
                visited[p] = 1
                if res[1] < next_d:
                    res[0] = p
                    res[1] = next_d
    return res

n,_ = BFS(1)
print(BFS(n)[1])

'''
트리의 지름
임의의 시작 정점 s로 부터 가장 멀리있는 정점인 u를 잡는다.
이 u로부터 가장 멀리 떨어진 길이를 다시 한번 찾으면 그것을 트리의 지름이라고 한다.
https://blogshine.tistory.com/111
''' 