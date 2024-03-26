# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:09:29 2024

@author: user
"""
# =============================================================================
# 
# =============================================================================
N = 4
matrix = [[0,1,2,3],[4,0,5,6],[7,1,0,2],[3,4,5,0]]



N = 6
matrix = [[0,1,2,3,4,5],[1,0,2,3,4,5],[1,2,0,3,4,5],[1,2,3,0,4,5],[1,2,3,4,0,5],[1,2,3,4,5,0]]

# =============================================================================
# 
# =============================================================================
N = int(input())

matrix = []
for i in range(N):
    xx = list(map(int,input().split()))
    matrix.append(xx)

# =============================================================================
# 
# =============================================================================
team = [i for i in range(N)]
team_number = int(N/2)

from itertools import permutations, combinations

a = list(combinations(team, team_number))

answer = 1000000000

for i in range(int(len(a)/2)):
    f = 0; b = 0
    
    front = a[i]
    back = a[len(a)-i-1]
    
    front_case = list(permutations(front,2))
    back_case = list(permutations(back,2))
    
    #print(front_case, back_case)
    
    for alpha in front_case:
        f += matrix[alpha[0]][alpha[1]]
    
    for beta in back_case:
        b += matrix[beta[0]][beta[1]]
    
    if answer > abs(f-b):
        answer = abs(f-b)
        
print(answer)