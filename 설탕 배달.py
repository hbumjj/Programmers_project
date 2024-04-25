# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:33:32 2024

@author: user
"""

# 설탕 배달

# 최대한 적은수로 배달을 해야한다.

a = int(input())

start = int(a/5) # 2
answer = 0
for i in range(start, -1, -1):
    
    n = a - (i * 5)
    if n%3 == 0: # 나머지가 0이라면
        answer = i + int(n/3)
        break;

if answer == 0:
    answer = -1

print(answer)
        

