# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:06:51 2024

@author: user
"""
# =============================================================================
# 
# =============================================================================

#matrix = [[3,3,0,1],[4,2,1,3],[4,2,2,1]]


# =============================================================================
# 
# =============================================================================


N = int(input())
matrix = []

for i in range(N):
    a = list(map(int,input().split()))
    matrix.append(a)

# =============================================================================
# 
# =============================================================================

def rotation(direction): # 반시계 방향으로 90도 회전
    if direction == 0:
        return 1
    elif direction == 1:
        return 2
    elif direction == 2:
        return 3
    elif direction == 3:
        return 0

def dracon_curve(x,y, direction, N):
    dx = [0,-1,0,1] # 오, 위, 왼, 아
    dy = [1,0,-1,0]   
    
    line = []#deque()
    sub = [[x,y],[x+dy[direction],y+dx[direction]]]
    line.append([(x,y),direction])
    line.append([(x+dy[direction],y+dx[direction]),direction])
    
    counter = False
    
    for i in range(N):
        pre = line
        s = sub
        for idx in range(len(line)-1, 0, -1):   
            end_point = line[-1][0]
            direction = line[idx][1]
            
            after_direction = rotation(direction)
            nx = end_point[0] + dy[after_direction]; ny = end_point[1] + dx[after_direction]
            
            if nx >= 0 and nx <= 100 and ny >= 0 and ny<=100: 
                line.append([(nx,ny),after_direction])
                sub.append([nx,ny])
            else:
                line = pre
                sub = s
                counter = True
                break;
        if counter == True:
            break;
    return sub

result = []
for x,y,d,n in matrix:
    l = dracon_curve(x,y,d,n)
    result.extend(l)

# # =============================================================================
# # 결과구하기    
# # =============================================================================

decision_x = [1,0,1]
decision_y = [0,1,1]
answer = 0

avoid = []
for i in result:
    coin = 0
    for j in range(3):
        re_x = i[0] + decision_x[j]
        re_y = i[1] + decision_y[j]
        if [re_x, re_y] in result:
            coin += 1
    
    if coin == 3 and i not in avoid:
        #print(i)
        answer += 1
        avoid.append(i)

print(answer)



    