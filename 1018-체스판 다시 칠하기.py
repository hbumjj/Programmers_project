# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:09:08 2024

@author: rapa
"""

'''
mn개의 단위 정사각형

검 혹은 흰
8 x 8 사이즈

번갈아서 칠해져야한다.
각 칸이 검과 흰 중 하나로 색칠
변 공유 시, 다른 색으로 칠해

이 경우 두 가지만 존재, 맨 오른쪽 위가 흰 또는 검

다시 칠해야하는 최소 갯수

2개 존재

'''
n, m = 8, 8
arr =[["W","B","W","B","W","B","W","B"],
      ["B","W","B","W","B","W","B","W"],
      ["W","B","W","B","W","B","W","B"],
      ["B","W","B","W","B","W","B","W"],
      ["W","B","W","B","W","B","W","B"],
      ["B","B","B","W","B","W","B","W"],
      ["W","B","W","B","W","B","W","B"],
      ["B","W","B","W","B","W","B","W"]]

# =============================================================================
# 
# =============================================================================
# n, m = map(int, input().split())

# arr = []
# for i in range(n):
#     arr.append(list(str(input())))

n, m = 10, 13
s = ["BBBBBBBBWBWBW",
"BBBBBBBBBWBWB",
"BBBBBBBBWBWBW",
"BBBBBBBBBWBWB",
"BBBBBBBBWBWBW",
"BBBBBBBBBWBWB",
"BBBBBBBBWBWBW",
"BBBBBBBBBWBWB",
"WWWWWWWWWWBWB",
"WWWWWWWWWWBWB"]
arr = []
for i in s:
    arr.append(list(i))
# =============================================================================
# 
# =============================================================================

def turn(x, flag):
    if flag == False:
        return x
    else:
        if x == "B": 
            return "W"
        elif x == "W":
            return "B"
        
start = ["B","W"]

answer = 10000000 # 수정
for start_point in start:
    # print(start_point)
    
    ans = 0; flag = False
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(start_point, (i,j))
            flag = True
            if arr[i][j] != start_point:
                ans += 1
            start_point = turn(start_point, flag)
    start_point = turn(start_point, flag)    
            
    #print(ans)
    answer = min(answer, ans)

print(answer)

# =============================================================================
# 
# =============================================================================
    
    
    
    
    
    