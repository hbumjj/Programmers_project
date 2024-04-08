# 회전초밥은 한 의자에 여러개
# 1초에 한칸씩 시계 회전
# 처음에는 벨트에 초밥과 사람 없음

# 3가지 규칙
# 시각 t에 위치 x 앞에 있는 벨트위에 name 이름을 부착한 회전초밥 하나 # 같은 위치에 여러번 가능,
# (100 t x name) - t시각에 x 위치에 name 제공

# 손님 입장 - name이 사람이 시각 t에 위치 x로 가서 먹는다
# 정확히 n개를 먹고 떠난다. # 사람이 없음을 가정
# (200 t x name n) - t 시각에 x 위치에 name인 사람이 n개를 먹음

# 촬영한다. 시각 t에는 1. 초밥 회전일어나고, 2. 먹고, 3. 촬영
# 촬영시, 가게의 있는 사람 수와 초밥 수 출력
# (300 t) 시각 t

L, order = 5, 10

main = [[100,1,1,'sam'],[100,1,2,'sam'],[100,2,2,'teddy'],[100,3,2,'june'],[300,6],[200,7,4,'june',2],[200,8,3,'teddy',1],[300,9],[200,10,3,'sam',1],[100,11,4,'june'],[300,13]]
main = [[100,1,1,'sam'],[100,2,2,'teddy'],[100,3,2,'june'],[0],[0],[300,6],[200,7,4,'june',2],[200,8,3,'teddy',1],[300,9],[200,10,3,'sam',1],[100,11,4,'june'],[0],[300,13]]
####################################### 입력 #############################################

import sys
input = sys.stdin.readline
L, order = map(int, input().split())
main = []

start = 0

for i in range(order):
    a = list(input().split())
    if a[0] == str(100):
        a[0] = int(a[0]);a[1] = int(a[1]);a[2] = int(a[2])

    elif a[0] == str(200):
        a[0] = int(a[0]);
        a[1] = int(a[1]);
        a[2] = int(a[2])
        a[4] = int(a[4])
    elif a[0] == str(300):
        a[0] = int(a[0]);a[1] = int(a[1])

    if a[1] != start + 1:
        for k in range(a[1]-start-1):
            main.append([0])

    start = a[1]
    main.append(a)

#print(main)

####################################### 입력 #############################################
from collections import deque

queue = deque([0]*L) # 개수만 저장
name = deque([""]*L) # 이름만 저장
seat = []

def one_(factor, queue, name):

    idv = factor[3]
    location = factor[2]
    if idv in name[location]: # 같은 사람이 있을 때
        find = name[location]
        idx = find.index(idv)
        queue[location][idx] += 1

    else: # 같은 사람이 없을 때
        if queue[location] == 0:
            queue[location] = [1]
            name[location] = [idv]
        else:
            queue[location] = queue[location] + [1]
            name[location] = name[location] + [idv]

    return queue,name

def two_(factor, queue, name, seat):
    idv = factor[3]
    location = factor[2]
    eat = factor[4]

    seat.append([idv,location,eat])
    return seat


for i in range(len(main)):
    a = queue.pop()
    queue.appendleft(a)
    b = name.pop()
    name.appendleft(b)

    #print(queue,name, seat)
    if main[i][0] == 100:
        queue, name = one_(main[i], queue, name)
    elif main[i][0] == 200:
        seat = two_(main[i], queue, name, seat)

    if seat != []:
        # print("##############")
        # print(i, queue, name, seat)
        for f in range(len(seat)):
            idv_ = seat[f][0]; lo = seat[f][1]; eat_ = seat[f][2]
            if idv_ in name[lo]:
                index_ = name[lo].index(idv_)
                s = queue[lo][index_]
                queue[lo][index_] -= eat_
                if queue[lo][index_] >= 0: # 다 먹은 상태
                    #seat.remove(seat[f])
                    seat[f] = ['_',0,0] # 나가기
                else: # 다 먹지 않고 남은 상태
                    queue[lo][index_] = 0
                    name[lo][index_] = " "
                    seat[f][2] -= s
        # print(queue, name, seat)
        # print("##############")

    if main[i][0] == 300:

        # 사람수 세기
        seat_n = 0; food_n = 0
        for i in seat:
            if i[0] == '_':
                pass
            else:
                seat_n += 1

        for j in queue:
            if j != 0:
                food_n += sum(j)
        print(seat_n, food_n)

