n = 3
direction = [[0,1,0],[1,0,1],[0,1,0]]
plan = [1,2,3]
m = 3


n = 3
direction = [[0,0,0],[0,0,0],[0,0,0]]
plan = [1,2,3]
m =3

n = 3
direction = [[0,1,0],[1,0,1],[0,1,0]]
plan = [1,1]
m = 2
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
        
        xx = q.popleft()
        visited.append(xx) # 방문 완료        
        
        if flag == True or xx == y:
            flag = True
            break;
            
        # 열 탐색
        print(direction[xx], xx)
        for idx, t in enumerate(direction[xx]): # idx, t
            # print(xx, idx, t, visited)   
            if t == 1 and idx not in visited: # 연결되어 있다면
                q.append(idx)
                  
                if idx == y: # 목적지라면
                    flag = True
                    break;
    return flag


for si in range(1, m):
    # print(plan[si-1], plan[si])
    
    check = BFS(plan[si-1]-1, plan[si]-1)
    if check == False:
        break;

if check == True:
    print("YES")
else:
    print("NO")
    

'''
<해결>
고려 안해준 사항: 같은 여행지일 경우에는 방문할 수 있음을 간과
'''