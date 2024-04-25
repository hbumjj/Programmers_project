# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:04:08 2024

@author: user
"""

n = int(input())
visited = [0] * (n+1)


# =============================================================================
# 기존 풀이
# =============================================================================
for i in range(2,n+1):
    
    if i%2 == 0 and i%3 == 0:
        mim_v = min(visited[i//2], visited[i//3], visited[i-1])
        
        if visited[i//2] == mim_v:
            visited[i] = visited[i//2] + 1
        elif visited[i-1] == mim_v:
            visited[i] = visited[i-1] + 1
        elif visited[i//3] == mim_v:
            visited[i] = visited[i//3] + 1
            
    elif i%2 == 0:
        if visited[i//2] > visited[i-1]:
            visited[i] = visited[i-1] + 1
        else:
            visited[i] = visited[i//2] + 1
    
    elif i%3 == 0:    
        if visited[i//3] > visited[i-1]:
            visited[i] = visited[i-1] + 1
        else:
            visited[i] = visited[i//3] + 1
    
    else:
        visited[i] = visited[i-1] + 1
    
print(visited[-1])


# =============================================================================
# 정답 풀이
# =============================================================================

for i in range(2, n+1):
    visited[i] = visited[i-1] + 1
    if i % 3 == 0: # 나누어 떨어지는 경우
        visited[i] = min(visited[i], visited[i//3]+1)
    if i % 2 == 0:
        visited[i] = min(visited[i], visited[i//2]+1)