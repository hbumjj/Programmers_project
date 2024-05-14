m,n = 5, 7
matrix = [[0, 0, 0, 0, 0, 0, 0],
          [0, 2, 4, 5, 3, 0, 0],
          [0, 3, 0, 2, 5, 2, 0],
          [0, 7, 6, 2, 4, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

m,n = 7, 9
matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 9, 5, 5, 5, 5, 5, 9, 0],
          [0, 5, 9, 5, 5, 5, 9, 5, 0],
          [0, 5, 5, 9, 1, 9, 5, 5, 0],
          [0, 5, 9, 5, 5, 5, 9, 5, 0],
          [0, 9, 5, 5, 5, 5, 5, 9, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# =============================================================================
# 
# =============================================================================
# m, n = map(int, input().split())
# matrix = []

# for i in range(m):
#     a = list(map(int,input().split()))
#     matrix.append(a)

# =============================================================================
# 
# =============================================================================
'''
dfs -> 완전 탐색하고, 동시에 빼주면서, 덩어리를 평가한다.
'''
import copy
import sys
sys.setrecursionlimit(10**6)
dx_ = [0, 0, -1, 1]
dy_ = [1, -1, 0, 0]
#visited = [[0]*n for _ in range(m)]


def out_of_range(x,y):
    if x < 0 or x >= m: return -1
    if y < 0 or y >= n: return -1
    return 0
    

def DFS(matrix, visited, x, y, co_matrix):
    
    visited[x][y] = 1
    count = 0
    for dx, dy in zip(dx_, dy_):
        nx = x + dx; ny = y + dy
            
        # 1. 범위가 벗어나지 말것
        # 2. 방문하지 않은 위치일 것. 
        if out_of_range(nx, ny) == 0: # 
            if co_matrix[nx][ny] == 0:
                count += 1
            
            if visited[nx][ny] != 1 and co_matrix[nx][ny] != 0:
        
                DFS(matrix, visited, nx, ny, co_matrix)

    if matrix[x][y] - count < 0:
        matrix[x][y] = 0
    else:
        matrix[x][y] = matrix[x][y] - count
        
answer = 0

while True:
    answer += 1
    map_ = 0
    
    co_matrix = copy.deepcopy(matrix)
    visited = [[0]*n for _ in range(m)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j] == 0 and co_matrix[i][j] != 0: # 시작점 찾기
                DFS(matrix, visited, i, j, co_matrix) # i는 행, j는 열
                map_ += 1

    if map_ >= 2:
        break;


    # 합이 0이라면 멈추기
    if map_ == 0:
        break;
    
print(answer-1)
    