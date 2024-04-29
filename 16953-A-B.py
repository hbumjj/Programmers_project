# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:58:34 2024

@author: user
# """
# start = 100
# end = 40021

# DFS 풀이

start, end = map(int, input().split())

def DFS(a, b, depth):
    global answer
    #print(a, depth)
    if a == b:
        ## 내용 추가하기
        answer = min(answer, depth)
        return
    
    elif a>b:
        return
    
    DFS(a*2,b, depth + 1)
    DFS(int(str(a)+str(1)),b, depth + 1)
    
    

answer = 100000000
DFS(start, end, 0)
if answer == 100000000:
    print(-1)
else:
    print(answer+1)


# BOTTOM UP 풀이 방식

# 뒤가 1일 경우에는 1을 빼고, 짝수이면 2로 나눈다.