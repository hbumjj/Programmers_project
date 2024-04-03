# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:41:40 2024

@author: user
"""
N = 5; M = 3
homes = [[0,2],[1,4],[2,1],[3,2]]
chick = [[1,2],[2,2],[4,4]]

N = 5; M = 1

homes = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
chick = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]


homes = [[0, 0], [0, 4], [1, 0], [1, 4], [2, 0], [2, 4], [3, 0], [3, 4], [4, 0], [4, 4]]
chick = [[0, 1], [0, 3], [1, 1], [1, 3], [2, 1], [2, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
# =============================================================================
# 
# =============================================================================

N,M = map(int, input().split())
homes = []
chick = []

for i in range(N):
    a = list(map(int,input().split()))
    
    for j in range(len(a)):
        if a[j] == 1:
            homes.append([i,j])
        elif a[j] == 2:
            chick.append([i,j])

# print(homes)
# print(chick)


# =============================================================================
# 
# =============================================================================
from itertools import combinations


def min_cal(homes, chick_set):
    answer = 0
    for home in homes:
        a = N**2
        for chick in chick_set:
            distance = abs(chick[0]- home[0]) + abs(chick[1]-home[1])
            
             
            if distance < a:
                a = distance
        answer += a

    return answer

chick_com = list(combinations(chick, M))

result = 100000000

for chick_set in chick_com:
    answer = min_cal(homes, chick_set)
    if result > answer:
        result = answer
print(result)
    
