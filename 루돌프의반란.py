

################################ 입력 #################################
# N, M, P, C, D = 5, 10, 5, 1, 2
# rudolf = [5,5]
# santas = [[100,100],[3,2],[1,4],[5,3],[2,4],[1,3]]
#print(santas)
#
# N, M, P, C, D = 5, 7, 4, 2, 2
# rudolf = [3,2]
# santas = [[100,100],[1,3],[3,5],[5,1],[4,4]]
# print(santas)
#
# N, M, P, C, D = 3, 5, 2, 1, 1
# rudolf = [2,2]
# santas = [[100,100],[1,3],[1,2]]
#print(santas)

# N, M, P, C, D = 4, 26, 6, 1, 1
# rudolf = [2,1]
# santas = [[100,100],[2,4],[2,3],[3,2],[3,3],[3,4],[4,4]]

################################ 입력 #################################

N,M,P,C,D = map(int,input().split())
rudolf = list(map(int,input().split()))
pre_santas = []

pre_santas.append([0, 100,100])

for i in range(P):
    a = list(map(int,input().split()))
    pre_santas.append(a)

pre_santas = sorted(pre_santas, key = lambda x:x[0])

santas = []
for i in pre_santas:
    santas.append(i[1:])

################################ 입력 #################################
from collections import deque

score = [0] * len(santas)
grog = [0] * len(santas)
grog[0] = "stop"
def distance(r1,c1, r2, c2): # 거리 계산용
    return (r1- r2)**2 + (c1- c2)**2

def santa_distance(r1,c1,r2,c2):
    return abs(r1-r2) + abs(c1-c2)

def out_range(x,y):
    if x<1 or y<1 or x > N or y > N:
        return False
    return True

def conflict(main, dx, dy, id): # 충돌 함수
    #grog[id] = 2 # 기절시키기
    # print("충돌발생")
    if main == "R":
        grog[id] = 2  # 기절시키기
        x = santas[id][0]
        y = santas[id][1]
        score[id] += C
        nx = x + (C*dx); ny = y + (C*dy)
    elif main == "S":
        grog[id] = 1  # 기절시키기
        x = santas[id][0] - dx;
        y = santas[id][1] - dy
        score[id] += D
        nx = x + (D * dx); ny = y + (D * dy)

    if out_range(nx, ny) == True: # 범위내면
        santas[id][0] = nx; santas[id][1] = ny # 이동 시키기
        answer = True
    else:
        grog[id] = "stop" # 탈락시키기
        santas[id] = [100,100]
        answer = False
    return nx, ny, answer # 날라간뒤 도착하는 위치

def plus(start_x, start_y, dx, dy, id): # 상호작용 함수
    # x,y는 날라간 위치, dx, dy는 방향
    queue = deque()

    queue.append([start_x,start_y])
    visited= [id]
    while queue:
        x,y = queue.popleft()
        for idx, santa in enumerate(santas):
            if [x, y] == santa and idx not in visited: # 지점에 산타가 있는지? 단, 자신을 제외한.
                # 산타가 있다면 이동한다.
                nx = santa[0] + dx; ny = santa[1] + dy
                if out_range(nx, ny) == True:
                    queue.append([nx,ny]) # 평가를 완료함
                    santa[0] = nx; santa[1] = ny
                    visited.append(idx)

                elif out_range(nx,ny) == False:
                    grog[idx] = "stop"
                    santas[idx] = [100,100]

# 루돌프 이동
# 8방향
r_dx_ = [1,-1,0,0, 1,-1,-1,1]
r_dy_ = [0,0,1,-1, 1,-1,1,-1]

s_dx_ = [-1,0,1,0] # 상우하좌 우선수위이므로, 반대로 평가 --> 좌하우상
s_dy_ = [0,1,0,-1]

for ss in range(1,M+1): # M+1
    rudolf_min = N**2; rudolf_min_2 = N**2
    fx = 0; fy = 0
    final_santa = [100,100]

    for santa in sorted(santas[1:]):
        x = rudolf[0]; y = rudolf[1]
        cal_dis = distance(santa[0], santa[1], x, y)

        if cal_dis <= rudolf_min: # 최소 산타를 찾기
            final_santa = santa # 가장 가까운 산타 찾기
            rudolf_min = cal_dis

    for r_dx, r_dy in zip(r_dx_, r_dy_):
        x = rudolf[0]; y = rudolf[1]
        nx = x + r_dx; ny = y + r_dy
        cal_dis_2 = distance(nx,ny,final_santa[0], final_santa[1])
        if cal_dis_2 <= rudolf_min_2:
            rudolf_min_2 = cal_dis_2
            fx, fy = r_dx, r_dy

    rudolf[0] += fx; rudolf[1] += fy

    # 충돌있는지 확인
    for id, santa in enumerate(santas):
        if rudolf == santa:
            sr_x, sr_y, flag = conflict("R", fx, fy, id) # 충돌이 있는 경우 작동 # 여기서 주체는 루돌프, 방향(fx,fy), santa 번호
            if flag == True:
                # 상호작용 검사 필요 (방향, fx, fy, 주체 산타는 id)
                plus(sr_x, sr_y, fx, fy, id)
            else:
                pass
        else: # 없으면 일단 패스
            pass

    # 산타 움직임
    for number, santa in enumerate(santas):
        if grog[number] != 0 and grog[number] != "stop": # 그로기 상태거나 탈락시에는 하지 않는다.
            grog[number] -= 1

        elif grog[number] == 0: # 기절이나 탈락이 아닐때만 수행한다.
            min_santa_distance = [] # 갈 수 있는 후보 설정
            min_direction = [] # 그에 따른 방향 설정
            final_nx = santa[0]; final_ny = santa[1]
            for dx, dy in zip(s_dx_, s_dy_):
                ss2 = distance(rudolf[0],rudolf[1], santa[0]+dx, santa[1]+dy)
                ss1 = distance(rudolf[0],rudolf[1], santa[0], santa[1])
                if ss2 < ss1:
                    min_santa_distance.append(ss2)
                    min_direction.append([dx,dy])

            min_santa_arr = sorted(min_santa_distance) # 최소 거리

            count = False
            for estimate in min_santa_arr: # 최소거리순으로 평가 수행
                for ad in range(len(min_santa_distance)):
                    if estimate == min_santa_distance[ad]:
                        s1, s2 = min_direction[ad] # 해당 방향 찾기

                        if out_range(santa[0]+s1,santa[1]+s2) == True and [santa[0]+s1,santa[1]+s2] not in santas:
                            # 이동한 산타가 범위안에 있으면서, 산타가 없어여한다.
                            final_nx= santa[0]+s1; final_ny  = santa[1]+s2 # 이동하기

                            if rudolf == [final_nx, final_ny]:
                                final_nx, final_ny, flag = conflict("S", -s1, -s2, number)
                                if flag == True:
                                    plus(final_nx, final_ny, -s1, -s2, number)
                            count = True
                            break;
                if count == True:
                    break;
            santa[0] = final_nx; santa[1] = final_ny # 이동한다.

    re = 0
    for j,santa in enumerate(santas): # 도중에 멈추거나 스코어 보이는 것
        if santa != [100,100]:
            score[j] += 1
        elif santa == [100,100]:
            re += 1
    if re == len(santas):
        break;

    # print("############")
    # print(ss)
    # print(santas)
    # print(rudolf)
    # print(grog)
    # print(score)
    # print("############")

result = (score[1:])
for i in result:
    print(i, end = " ")
