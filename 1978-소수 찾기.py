# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:49:16 2024

@author: user
"""

# example
# n = 4
# number = [1, 3, 5 ,7]

answer = 0

def prime_number(a):
    global answer
    for i in range(2, a+1):
        if a%i == 0: 
            if a == i:
                answer = answer + 1
            break;
            
        else:
            pass
        
n = int(input())
number = list(map(int,input().split()))

for i in number:
    prime_number(i)

print(answer)