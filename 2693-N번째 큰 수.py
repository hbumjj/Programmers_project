# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:25:01 2024

@author: user
"""

n = int(input())

result = []
for i in range(n):
    a = list(map(int,input().split()))
    after_a = sorted(a)
    print(after_a[-3], end = ' ')