'''
N, M, K
N은 미로 크기
M은 참가자의 좌표 (개수)
K는 게임 시간

마지막은 출구 좌표

출력: K초가 지났거나, 모든 참가자가 미로를 탈출 했을 때의 이동거리 합과 출구 좌표
'''

N = 5; K = 8
matrix = [[0,0,0,0,1],[9,2,2,0,0],[0,1,0,1,0],[0,0,0,1,0],[0,0,0,0,0]]
people = [[1,3],[3,1],[3,5]]
out = [3,3]
#print(matrix)
#####################################################################################
N, M, K = map(int, input().split())
matrix = []
for i in range(N):
    a = list(map(int, input().split()))
    matrix.append(a)

people = []
for j in range(M):
    b = list(map(int, input().split()))
    people.append(b)

c,d = map(int, input().split())
out = [c,d]
####################################################################################
# with open('D:/프로젝트/input (1).txt', 'r') as file:
#     lines = file.readlines()
# #
# N, M, K = map(int, lines[0].split())
# matrix = []
# for line in lines[1:N+1]:
#     a = list(map(int, line.split()))
#     matrix.append(a)
#
# people = []
# for line in lines[N+1:N+1+M]:
#     b = list(map(int, line.split()))
#     people.append(b)
#
# c,d = map(int, lines[-1].split())
# out = [c,d]

######################################################################
score = [0] * len(people)

import copy
def rotation(rx,ry,zx,zy): # 좌표에 대해서 시계 90도 방향도는거 필요
    global out

    L = abs(rx[1]-ry[1])+1 # 한변의 길이
    r = abs(rx[1]-ry[1])

    start = rx
    copy_matrix = copy.deepcopy(matrix); copy_people = copy.deepcopy(people); copy_out = copy.deepcopy(out)
    for i in range(0,L):
        for j in range(0,L): #10 --> 1~10
            x = i; y = j
            nx,ny = y,(r)-x # 시계방향으로 90도 회전

            x = x + start[0]; y = y + start[1] # 평행이동
            nx = nx + start[0]; ny = ny + start[1]

            for ID in range(len(copy_people)):
                if copy_people[ID] == [x,y]: # 옮기기전에 좌표가 있었다면 옮겨줘야함
                    people[ID][0],people[ID][1] = nx, ny

            if [x,y] == copy_out:
                out = [nx,ny]

            matrix[nx - 1][ny - 1] = copy_matrix[x-1][y-1]
            if matrix[nx-1][ny-1] > 0:
                matrix[nx-1][ny-1] -= 1

    return matrix, people, out

def detection(matrix):
    rx,ry,zx,zy = [1,1],[1,N],[N,1],[N,N] # 초기화 값을 설정해준다.
    count = False

    for ls in range(1, N): # 길이가 1부터 - N까지의 사각형을 탐색한다.

        for i in range(1,len(matrix)-ls+1): # 이부분 주의
            for j in range(1,len(matrix[0])-ls+1):

                four = [i+ls, j+ls]; one = [i, j]
                two = [i+ls, j]; three = [i, j+ls]

                if one[0] <= out[0] <= four[0] and one[1] <= out[1] <= four[1]:# 들어와있다. 출구는
                    for person in people: # 출구가 들어온 상태에서 사람별로 본다. 들어온 사람이 있는지
                        if one[0] <= person[0] <= four[0] and one[1] <= person[1] <= four[1]:
                            rx = one; ry = three; zx = two; zy = four # 사람이 들어왔을 경우 좌표를 저장한다. r과 c가 작은것이 우선이므로 처음나오면 스탑
                            count = True
                            break;
                if count == True:
                    break;
            if count == True:
                break;
        if count == True:
            break;

    if rx == [0,0] and zy == [10,10]:
        print(people)
    return rx,ry,zx,zy

############################################################
'''
1. 움직임 
2. 벽이 있으면 못감
3. 가까워지는 방향에 벽이 있으면 못감 - 안감
'''

dx_ = [-1,1,0,0] # 위, 아래, 우, 좌 순으로 평가
dy_ = [0,0,1,-1]

for time in range(K):
    for i,person in enumerate(people): # 사람별로 탐색

       distance = N**2; w_nx = 0; w_ny = 0
       if person[0] == 0 and person[1] == 0: # 탈출한 사람은 스킵한다.
           pass
       else:
           arr = []; poun = []
           for dx,dy in zip(dx_,dy_): # 네방향 탐색
              nx = person[0] + dx; ny = person[1] + dy # 임시로 갔을 경우
              cal_distance = abs(nx - out[0]) + abs(ny - out[1]) # 거리 계산
              arr.append(cal_distance) # 거리 저장
              poun.append([nx,ny]) # 그에 따른 좌표 저장
           min_distance = min(arr) # 최단 거리 찾기

           for sv in range(len(arr)): # 저장된 거리를 기반으로 최단 거리시 좌표 찾기
               if arr[sv] == min_distance:
                   nx, ny = poun[sv] # 좌표에 대한 후보 설정  # 평가 순서는 위, 아래, 좌, 우 순.

                   if nx < 1 or ny < 1 or nx > N or ny > N or matrix[nx - 1][ny - 1] != 0: # 후보가 예외조건을 만족하는지 평가
                       w_nx, w_ny = person[0], person[1] # 만족안했을 때는 이동안함
                   else: # 만족을 했다면
                       w_nx, w_ny = nx, ny # 정답이므로 저장한다. (움직인다.)
                       person[0] = w_nx; person[1] = w_ny  # 좌표 바꾸기
                       score[i] += 1
                       break;

       if person == out: # 탈출한 경우 # 만약에 이동했는데, 그곳이 탈출구일 수 있다.
           person[0] = 0; person[1] = 0 # 0,0으로 아예 뺴버린다

    # 사람들 이동 완료
    re = 0 # 만약에 전부 나갔다면 바로 끝내기
    for check in people:
        re += sum(check)
    if re==0: break;

    rx,ry,zx,zy = detection(matrix)
    matrix,people,out = rotation(rx,ry,zx,zy) # 회전 후에 매트릭스 완성

print(sum(score))
print(out[0], out[1])

'''
<핵심>
네방향 탐색 --> 리스트로 모아서, 최소 거리에 대해서 출력
정사각형 생성해서 모든 리스트 탐색하기
시계방향으로 90도는 X,Y = Y,X 후 좌우 반전 시행
new_x = old_y
new_y = (len(row) - 1) - old_x
'''


