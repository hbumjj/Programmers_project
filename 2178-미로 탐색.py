# 그래프 이론

'''
1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
1,1에서 출발 m,n에 도착하는 최소 칸 수 작성
서로 인접한 칸만 이동 가능 --> 4방향

-> BFS 풀이로 진행
'''

# matrix = [[1,0,1,1,1,1],
#           [1,0,1,0,1,0],
#           [1,0,1,0,1,1],
#           [1,1,1,0,1,1]]

matrix = [[1,1,0,1,1,0],
          [1,1,0,1,1,0],
          [1,1,1,1,1,1],
          [1,1,1,1,0,1]]

destination = [4,6]

visited = [[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]

# =============================================================================
# 
# =============================================================================

destination = list(map(int, input().split()))

matrix = []
visited = []

for _ in range(destination[0]):
    l = [int(char) for char in list(input())]
    matrix.append(l)
    l2 = [0 for _ in range(destination[1])]
    visited.append(l2)
    
# =============================================================================
# 
# =============================================================================

destination_x = destination[0] -1 
destination_y = destination[1] -1 

from collections import deque

def out_of_range(x,y):
    len_y = len(matrix[0])
    len_x = len(matrix)

    if x < 0 or x >= len_x: return -1
    if y < 0 or y >= len_y: return -1
    
    return 0

def BFS(start, matrix, destination_x, destination_y, answer):
    queue = deque()
    
    queue.append((start[0],start[1], answer))
    # visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dx_ = [0, 0, 1, -1]; dy_ = [1, -1, 0, 0]
    visited[start[0]][start[1]] = 1
    while queue:
        
        q = queue.popleft()
        
        if [q[0],q[1]] == [destination_x, destination_y]:
            print(q[2])
            break;
        
        # 이동 수행
        for dx, dy in zip(dx_, dy_):
            q_x = q[0] + dx
            q_y = q[1] + dy
            if out_of_range(q_x, q_y) == 0:
                if visited[q_x][q_y] != 1 and matrix[q_x][q_y] == 1:
                    queue.append((q_x, q_y, q[2]+1))
                    visited[q_x][q_y] = 1
    
BFS([0,0], matrix, destination_x, destination_y, 1)