# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:58:21 2024

@author: user
"""
# =============================================================================
# 
# =============================================================================
string = "55-50+40"

string = "10+20+30+40"
string = "00009-00009"
# string = "55-50+40"
# string = "55-50+40"
# =============================================================================
# 
# =============================================================================
string = str(input())
a = string.split('-')

count = 0
for i in a:
    b = i.split('+')
    b_sum = sum(list(map(int,b)))
    
    if count == 0:
        answer = b_sum
        count += 1
    else:
        answer -= b_sum

print(answer)