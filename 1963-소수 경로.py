# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:36:26 2024

@author: user
"""

# 1033 1733 3733 3739 3779 8779 8179

a,b = 1033, 8179

# 최소횟수 - 6



# 우선 a와 b사이의 소수를 찾자

# check_list = []
# for i in range(a, b):
#     answer = dec(i)
#     if answer == True:
#         print(i)
        
        
# =============================================================================
# 
# =============================================================================
def dec(number):
    for _ in range(2, number):
        if number%_ == 0:
            return False
    return True

def sep(number):
    q = number//1000
    w = number//100 - 10*(number//1000)
    e = number//10 - 10*(number//100)
    r = number//1 - 10*(number//10)
    return q,w,e,r

def su(q,w,e,r):
    return 1000*q + 100*w + 10*e + r

total = 0
def dfs(a, b, total):
    print(a, b, total)
    if a == b:
        return
    elif a > b or dec(a) == False:
        return
    else:    
        q,w,e,r = sep(a)
        for i in range(1,10):
            if q+i <= 9 and dec(su(q+i,w,e,r)) == True:
                dfs(su(q+i,w,e,r), b, total+1)
            if w+i <= 9 and dec(su(q,w+i,e,r)) == True:
                dfs(su(q,w+i,e,r), b, total+1)
            if e+i <= 9 and dec(su(q,w,e+i,r)) == True:
                dfs(su(q,w,e+i,r), b, total+1)
            if r+i <= 9 and dec(su(q,w,e,r+i)) == True:
                dfs(su(q,w,e,r+i), b, total+1)

                
dfs(a, b, total)







