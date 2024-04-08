'''
첫째줄,
N, Q = 채팅방 수, 명령
Q개의 명령 정보

1. 사내 메신저 준비
100,p1, p2, p3..., a1 a2 a3...
1 ~ N 각 그 뒤는 초기 권한 세기
처음은 모두 ON으로

2. 알라밍 설정
200 C --> C의 알람만 ON, OFF 바꾸기

3. 권한 세기 -> 권한 값 바꾸기

4. 부모 채팅방 교환
'''
N,Q = 8, 10
####################################################################
first_order = [100, 0, 0, 1, 1, 2, 2, 4, 4,     1, 1, 2, 1, 2, 2, 1, 1]
orders = [[500,1],[300,8,3],[500,1],[200,4],[500,1],[400,4,5],[500,2],[200,4],[500,2]]
####################################################################
N, Q = map(int, input().split())

first_order = list(map(int,input().split()))
orders = []
for i in range(Q-1):
    orders.append(list(map(int,input().split())))


####################################################################

from collections import deque
tree = {}

j = 1;
for i in range(0,N):
    if j not in tree:
        tree[j] = [first_order[i+1],1,first_order[i+N+1]] # 부모, on(1)/off(0), power
    j += 1


def two_(c):
    change = tree[c][1]
    if change == 1:
        tree[c][1] = 0
    else:
        tree[c][1] = 1

def three_(c, power):
    tree[c][2] = power

def four_(c1, c2):
    tree[c1][0], tree[c2][0] = tree[c2][0], tree[c1][0]

def five_(c0): # example 500,1 # bfs
    #print("#######################")
    answer = 0
    queue = deque()
    queue.append([c0,0,tree[c0][1],tree[c0][2]])
    visited = []
    while queue:
        [c,depth,onoff, power] = queue.popleft()
        visited.append([c,depth,onoff,power])
        if depth == 20:
            break;
        # 여기 부분에 통신 가능한 여부를 확인하는 알고리즘을 추가한다.
        if c != c0:
            if depth - power <= 0:
                answer +=1
                #print(c,depth,onoff, power)
            elif depth - power > 0:
                pass
        for factor in tree:
            if tree[factor][0] == c and factor not in visited and tree[factor][1] == 1:
                queue.append([factor,depth+1, tree[factor][1],tree[factor][2]])
    #print(visited) # 번호, 깊이, onoff , power
    #print(answer)
    return answer

for order in orders:
    if order[0] == 500:
        print(five_(order[1]))
    elif order[0] == 400:
        four_(order[1], order[2])
    elif order[0] == 300:
        three_(order[1], order[2])
    elif order[0] == 200:
        two_(order[1])