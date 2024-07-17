# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:17:15 2024

@author: rapa
"""

'''
백준 9663
n x n 체스판
n개의 퀸
서로 공격할 수 없게 배치

4일때의 경우
0100
0000
0000
1000

'''


n = int(input())
ans = 0
row = [0] * n

def checking(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True


def BackTracking(x):
    global ans
    if x == n: # 전부 놨다.
        ans += 1
        return
    
    for i in range(n): # 행 당 한개만 놓을 수 있으므로
        row[x] = i
        if checking(x) == True:
            BackTracking(x+1)
        
    

BackTracking(0)
print(ans)