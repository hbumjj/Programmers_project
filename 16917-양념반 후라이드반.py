# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:56:10 2024

@author: user
"""

# a,b,c,x,y = 1500, 2000, 500, 90000 , 100000
# a,b,c,x,y = 1500, 2000, 1600, 3, 2

a,b,c,x,y = map(int, input().split())
total = 0

if a+b < 2*c:
    total = a*x + b*y
else:
    buy = min(x,y)
    total = 2*c*buy

    first = total + a*(x-buy) + b*(y-buy)# 남은것 각각 사기
    second = total + 2*c*max((x-buy),(y-buy))
    
    total = min(first, second)
    
print(total)
    