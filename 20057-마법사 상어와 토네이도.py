
# N = 5

# matrix =[[0,0,0,0,0],[0,0,0,0,0],[0,100,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

N = int(input())
matrix = []
for i in range(N):
    a = list(map(int, input().split()))
    matrix.append(a)

center = [int(N/2),int(N/2)]
x, y = center
# =============================================================================
# 
# =============================================================================
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]
ans = 0

def distribution(x, y, direction):
    global ans
    if direction == 0:
        direction = left
    elif direction == 1:
        direction = down
    elif direction == 2:
        direction = right
    else:
        direction = up
    
    total = 0
    for dx, dy, z in direction:
        
        nx = x + dx
        ny = y + dy
        
        if z == 0:
            new_sand = matrix[x][y] - total
        else:
            new_sand = int(matrix[x][y] * z)
            total += new_sand
        
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            ans += new_sand
        else:
            matrix[nx][ny] += new_sand
        
# =============================================================================
# 
# =============================================================================
idx = 1
count = 0

dy = [-1, 0 ,1, 0] # 좌, 아래, 우, 위
dx = [0, 1, 0, -1]

flag = True
flag_2 = True
# =============================================================================
# 
# =============================================================================
while flag:
    for i in range(4): # 4방향에 대해서        
        if flag_2 == False:
            break;
            
        if i == 2:
            idx += 1
        
        for j in range(idx):
            x = x + dx[i]
            y = y + dy[i]
            distribution(x, y, i)
            
            if x == 0 and y == 0:
                flag = False
                flag_2 = False
                break;
    idx += 1

print(ans)
