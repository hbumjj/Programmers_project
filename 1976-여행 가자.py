n = 3
direction = [[0,1,0],[1,0,1],[0,1,0]]
plan = [1,2,3]
m = 3
# =============================================================================
# 
# =============================================================================

# n = int(input())
# m = int(input())

# direction = []
# for i in range(n):
#     s = list(map(int, input().split()))
#     direction.append(s)

# plan = list(map(int, input().split()))

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
        print(direction[xx], xx)
        for idx, t in enumerate(direction[xx]):
            
            if t == 1 and idx not in visited: # 연결되어 있다면
                q.append(idx)
            
            if idx == y: # 목적지라면
                flag = True
                break;
    return flag

for si in range(1, m):
    flag = BFS(plan[si-1]-1, plan[si]-1)
    if flag == False:
        break;

if flag == True:
    print("YES")
else:
    print("NO")
    
    
'''
틀린 이유
무작정 목적지를 찾는 것이 아니라, 목적지가 아니더라도 후에 목적지에 도달할 수 있다.
이를 고려하지 않았다.
'''