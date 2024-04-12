from collections import deque

def out_range(x,y, N, M):
    if x <0 or y <0 or x > N-1 or y > M-1 :
        return False
    return True

def change_position(dx,dy,x,y, N,M): # 방향과 현재 위치, 범위
    nx = x - ((N-1) * dx)
    ny = y - ((M-1) * dy)
    return nx, ny

def out_range_for_bomb(x,y, N, M):
    if (x <0 or x > N-1) and (y <0 or y > M-1) :
        return "xy" # 둘다 벗어남
    elif x <0 or x > N-1:
        return "x" # x가 벗어남
    elif y <0 or y> M-1:
        return "y" # y가 벗어남
    return True

def change_position_for_bomb(dx,dy,x,y, N,M, main): # 방향과 현재 위치, 범위
    if main == "x":
        nx = x - ((N-1) * dx)
        ny = y + dy
    elif main == "y":
        ny = y - ((M-1) * dy)
        nx = x + dx
    elif main == "xy":
        nx = x - ((N-1) * dx)
        ny = y - ((M-1) * dy)
    return nx, ny

def BFS(matrix, x,y, end_x, end_y, N, M): # 경로찾기
    dx_ = [0,1,0,-1]# 우 하 좌 상
    dy_ = [1,0,-1,0]

    queue = deque()
    queue.append([(x,y)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    route = []

    while queue:
        q_s = queue.popleft()
        q = q_s[-1]
        visited[q[0]][q[1]] = True
        if q[0] == end_x and q[1] == end_y:
            route = (q_s[1:])
            break;

        for dx, dy in zip(dx_, dy_):
            nx = q[0] + dx
            ny = q[1] + dy
            # 범위가 넘을 경우 변환 한번 해주기
            if out_range(nx, ny, N, M) == False:
                nx, ny = change_position(dx,dy,q[0],q[1],N,M)

            if matrix[nx][ny] != 0 and visited[nx][ny] == False: #[nx,ny] not in visited:
                queue.append(q_s + [(nx,ny)])
    return route

def razer(matrix, route, attack, ed_attack, effect): #
    for r in route:
        if r != (ed_attack[0],ed_attack[1]):
            matrix[r[0]][r[1]] -= matrix[attack[0]][attack[1]]//2
            effect.append([r[0],r[1]])
            if matrix[r[0]][r[1]] <= 0:
                matrix[r[0]][r[1]] = 0
        else:
            matrix[r[0]][r[1]] -= matrix[attack[0]][attack[1]]
            if matrix[r[0]][r[1]] <= 0:
                matrix[r[0]][r[1]] = 0

    return matrix, effect

def bomb(matrix, attack, ed_attack, N, M, effect):
    dx_ = [1,-1,0,0,-1,1,1,-1,0] # 9방향에 대해서 감소
    dy_ = [0,0,-1,1,1,-1,1,-1,0]
    x = ed_attack[0]; y = ed_attack[1]
    for dx,dy in zip(dx_, dy_):
        nx = x + dx; ny = y + dy

        if out_range_for_bomb(nx, ny, N, M) != True: # 초과시에는 범위 한번 바꿔주기
            main = out_range_for_bomb(nx, ny, N, M)
            nx, ny = change_position_for_bomb(dx, dy, x, y, N, M,main)

        if nx == x and ny == y: # 온전한 피해
            matrix[nx][ny] -= matrix[attack[0]][attack[1]]
            if matrix[nx][ny] <= 0:
                matrix[nx][ny] = 0

        elif nx == attack[0] and ny == attack[1]:
            pass
        else:
            matrix[nx][ny] -= (matrix[attack[0]][attack[1]])//2
            effect.append([nx,ny])
            if matrix[nx][ny] <= 0:
                matrix[nx][ny] = 0

    return matrix, effect

def algrorithm(matrix, N, M, K, attack_order):

    for turn in range(1,K+1):
        # 1. 공격자 선정
        attacker = 5001
        attack = [-1, -1]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: pass
                else:
                    if matrix[i][j] < attacker:
                        attacker = matrix[i][j]
                        attack = [i,j]
                    elif matrix[i][j] == attacker:
                        if attack_order[attack[0]][attack[1]] < attack_order[i][j]:
                            attack = [i,j]
                        elif attack_order[attack[0]][attack[1]] == attack_order[i][j]:
                            if attack[0] + attack[1] < i+j:
                                attack = [i,j]
                            elif attack[0] + attack[1] == i+j:
                                if attack[1] < j:
                                    attack = [i,j]



        matrix[attack[0]][attack[1]] += (N+M)
        attack_order[attack[0]][attack[1]] = turn # 공격 최근 정의
        ####################################################################################
        # 공격 당할 사람 선택

        ed_attacker = 0
        ed_attack = [-1, -1]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 or [i,j] == attack: pass

                else:
                    if matrix[i][j] > ed_attacker: # 최대값이 크다
                        ed_attacker = matrix[i][j]
                        ed_attack = [i,j]

                    elif matrix[i][j] == ed_attacker:
                        if attack_order[ed_attack[0]][ed_attack[1]] > attack_order[i][j]:
                            ed_attack = [i,j]
                        elif attack_order[ed_attack[0]][ed_attack[1]] == attack_order[i][j]:
                            if ed_attack[0] + ed_attack[1] > i+j:
                                ed_attack = [i,j]
                            elif ed_attack[0] + ed_attack[1] == i+j:
                                if ed_attack[1] > j:
                                    ed_attack = [i,j]

        # 어떤 공격이 가능한지 체크 하기
        route = BFS(matrix,attack[0],attack[1], ed_attack[0], ed_attack[1], N, M) # matrix, 시작점 x,y , 끝나는 점 x,y

        effect = [attack, ed_attack]

        if route != []: # 레이저 공격 + 부서짐
            matrix,effect = razer(matrix, route, attack, ed_attack, effect)

        else: # 포탑 공격 + 부서짐
            matrix,effect = bomb(matrix, attack, ed_attack, N, M, effect)

        # 포탑정비
        sum_ = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    if [i,j] not in effect:
                        matrix[i][j] += 1
                    sum_ += 1
        if sum_ == 1:
            break;

    max_result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] >= max_result:
                max_result = matrix[i][j]
    return max_result


# 제출
N, M, K = map(int, input().split())
matrix = []
for j in range(N):
    a = list(map(int, input().split()))
    matrix.append(a)
attack_order = [[0 for i in range(M)] for j in range(N)] # 움직임 order
re = algrorithm(matrix, N, M, K, attack_order)
print(re)

# 삼성식 제출법

# import sys
# sys.stdin = open("D:/프로젝트/포탑 부수기_예제.txt", "r")
#
# T = sys.stdin.readline()
#
# for i in range(T):
#     n = int(sys.stdin.readline()) # 테스트 케이스
#     N, M, K = map(int, sys.stdin.readline().split())
#     matrix = []
#     for j in range(N):
#         a = list(map(int, sys.stdin.readline().split()))
#         matrix.append(a)
#
#     #print(matrix, N, M, K)
#     re = algrorithm(matrix, N, M, K)
#     print("#%d %d" %(n,re))
#

# T = int(input())
# for i in range(T):
#     n = int(input())
#     N, M, K = map(int, input().split())
#     matrix = []
#     for j in range(N):
#         a = list(map(int, input().split()))
#         matrix.append(a)
#
#     #print(matrix, N, M, K)
#     re = algrorithm(matrix, N, M, K)
#     print("#%d %d" %(n,re))

'''
4 4 3
6 8 0 1
0 0 0 0
0 0 0 0
0 0 8 0
'''
'''
6 5 7
9 0 0 8 0
3 4 0 4 0
0 0 0 2 0
0 0 9 2 4
5 0 4 0 0
0 5 5 0 0
'''