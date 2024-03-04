# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:49:56 2024

@author: user
"""

# 이진수 계산, *모듈 없이

# input
count = int(input())

test_case = []

for i in range(count):
    a = int(input())
    test_case.append(a)

# example
#n = 13

# algorithm
def nex(n):
    idx = 0
    while n>=2:
        if n%2 == 1:
            print(idx, end = ' ')
        idx+=1
        n = n//2
    print(idx, end = ' ')

for test in test_case:    
    nex(test)