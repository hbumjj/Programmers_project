# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:35:56 2024

@author: user
"""

N,M,dx,dy,K = 4, 2, 0, 0 ,8

number = [[0,2],[3,4],[5,6],[7,8]]

K_num = [4,4,4,1,3,3,3,2]

# =============================================================================
# 
# =============================================================================
number = []

N,M,dx,dy,K = map(int,input().split())

for i in range(N):
    b = list(map(int, input().split()))
    number.append(b)

K_num = list(map(int,input().split()))

# print(number)
# print(K_num)

# =============================================================================
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
# =============================================================================

def Dice(order, dice,dx,dy):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if order == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
        dy+=1
    elif order == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
        dy-=1
    elif order == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
        dx-=1
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
        dx+=1
    return dice, dx, dy

dice = [0, 0, 0, 0, 0, 0]

for order in K_num:
    dice, dx, dy = Dice(order, dice,dx,dy)
    
    if dx < 0 or dx >= N or dy < 0 or dy >= M:
        if order == 1:
            dice, dx, dy = Dice(2, dice,dx,dy)
        elif order == 2:
            dice, dx, dy = Dice(1, dice,dx,dy)
        elif order == 3:
            dice, dx, dy = Dice(4, dice,dx,dy)
        else:
            dice, dx, dy = Dice(3, dice,dx,dy)
        
    else:
        if number[dx][dy] == 0:
            number[dx][dy] = dice[0]
        else:
            dice[0] = number[dx][dy]
            number[dx][dy] = 0
        print(dice[-1])


            
            
            
            
            
            