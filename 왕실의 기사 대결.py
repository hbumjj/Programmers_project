'''
입력
첫째줄 L N Q # L은 체스판 크기, N은 기사의 수, Q는 명령의 수
# 맵이 나온다.
# 기사 정보가 준다. r,c 위치, h,w 직사각형, k 체력 # 기사들이 겹쳐짐
# Q개의 왕의 명령 (i,d) i번 기사에게 d 방향으로 한칸
# d: 0,1,2,3 => 위, 오른쪽, 아래쪽, 왼쪽

1 2
2 1
3 3

'''
############################## 입력 ################################
# L = 4
# matrix = [[0,0,1,0],[0,0,1,0],[1,1,0,1],[0,0,2,0]] # 0: 빈칸, 1: 함정, 2: 벽
#
# nights = [[1,2,2,1,5],[2,1,2,1,1],[3,2,1,2,3]]
#
# nights_HP = [0]
# nights_LC = [[0]]
# for night in nights:
#     nights_HP.append(night[-1])
#     ni = []
#     for i in range(night[2]):
#         for j in range(night[3]):
#             ni.append([night[0]+i,night[1]+j])
#     nights_LC.append(ni)
#
# #print(nights_LC, nights_HP)
#
# # [[0], [[1, 2], [2, 2]], [[2, 1], [3, 1]], [[3, 2], [3, 3]]] # nights_LC
# Q = 3
# orders = [[1,2],[2,1],[3,3]]


############################## 입력 ################################

L, N, Q = map(int,input().split())
matrix = []
for i in range(L):
    matrix.append(list(map(int,input().split())))


nights = []
for j in range(N):
    nights.append(list(map(int,input().split())))

nights_HP = [0]
nights_LC = [[0]]
for night in nights:
    nights_HP.append(night[-1])
    ni = []
    for i in range(night[2]):
        for j in range(night[3]):
            ni.append([night[0]+i,night[1]+j])
    nights_LC.append(ni)

orders = []
for k in range(Q):
    orders.append(list(map(int,input().split())))

############################## 입력 ################################
# with open('D:/프로젝트/input.txt', 'r') as file:
#     lines = file.readlines()
#
# # L, N, Q 값 추출
# L, N, Q = map(int, lines[0].split())
#
# # matrix 데이터 파싱
# matrix = []
# for line in lines[1:L+1]:
#     matrix.append(list(map(int, line.split())))
#
# # nights 데이터 파싱
# nights = []
# for line in lines[L+1:L+N+1]:
#     nights.append(list(map(int, line.split())))
#
# nights_HP = [0]
# nights_LC = [[0]]
# for night in nights:
#     nights_HP.append(night[-1])
#     ni = []
#     for i in range(night[2]):
#         for j in range(night[3]):
#             ni.append([night[0]+i,night[1]+j])
#     nights_LC.append(ni)
#
# # orders 데이터 파싱
# orders = []
# for line in lines[L+N+1:]:
#     orders.append(list(map(int, line.split())))
############################## 입력 ################################
from collections import deque
import copy
first = copy.deepcopy(nights_HP)

def move_nights(idx, way):
    dx = [-1, 0, 1, 0]  # 0:위, 1:오른쪽, 2:아래, 3:왼
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append(nights_LC[idx])
    visited = [idx]
    while queue:
        #print(queue)
        move = queue.popleft()
        point = visited[-1]
        for [x,y] in move:
            nx = x + dx[way]
            ny = y + dy[way]
            #print(nx, ny, matrix[nx-1][ny-1])
            if nx <= 0 or ny <= 0 or nx > L or ny > L or matrix[nx-1][ny-1] == 2: # 벽이거나 벗어난경우
                 queue = deque()
                 visited = []
                 break; # 움직이지 않기

            elif matrix[nx-1][ny-1] !=2: # 벽이 아닌데, 기사가 있는 경우
                 for i, night in enumerate(nights_LC):
                     if [nx,ny] in night and i != point and i not in visited:
                         queue.append(nights_LC[i])
                         visited.append(i)
            else:
                pass


    for p in visited: # 2, 1, 3
        for factor in nights_LC[p]:
            factor[0] += dx[way]
            factor[1] += dy[way]
            #print(factor[0], factor[1])
            if p != idx and matrix[factor[0]-1][factor[1]-1] == 1: # HP 감소
                #print(factor[0], factor[1])
                nights_HP[p] -= 1

        # 체스판에서 사라지게 하는법
        if nights_HP[p] <= 0:
            nights_HP[p] = -1
            nights_LC[p] = []

    #print(visited, nights_LC, nights_HP)
    return nights_HP, nights_LC


#print(first)
for order in orders:
    #print(order)
    nights_HP, nights_LC = move_nights(order[0], order[1])

result = 0
for i,j in zip(first, nights_HP):
    if j > 0:
        result += (i-j)
print(result)