# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:22:00 2024

@author: user
"""
# example
# a = 24
# b = 18

a, b = map(int, input().split())

if a>=b:
    criteria = b
    big = a
else:
    criteria = a    
    big = b

answer1 = 0
answer2 = criteria

# 최대공약수
for i in range(1, criteria+1):
    if criteria%i == 0 and big%i == 0:
        if i >= answer1:    
            answer1 = i
            
# 최소공배수
index = 1
while answer2 <= big * criteria:
    answer2 = criteria * index
    if answer2 >= big and answer2%big == 0:
        break;
    index+=1

print(answer1, answer2)