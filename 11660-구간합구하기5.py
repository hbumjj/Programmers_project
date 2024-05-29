# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:53:16 2024

@author: user
"""

import sys 
input = sys.stdin.readline

# 정답 풀이 
N, M = map(int, input().split())

matrix = []
for i in range(N):
    a = list(map(int, input().split()))
    matrix.append(a)

dp = [[0] * (N+1) for _ in range (N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + matrix[i-1][j-1] - dp[i-1][j-1]




for ss in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    
    
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        
    print(ans)        
    
    
# x1,y1,x2,y2 = 2, 2 ,3, 4

# print(dp[x1][y1], dp[x2][y2])

# ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        
# print(ans)        
        
