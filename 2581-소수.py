# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:30:27 2024

@author: user
"""

a = 60
b = 100

# =============================================================================
# 
# =============================================================================

a = int(input())
b = int(input())

min_value = b+2
summation = 0

def is_prime(number):
    if number == 1: # 1은 소수가 아니다. 
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
        return True

for i in range(a, b+1):
    if is_prime(i):
        summation += i
        if min_value >= i:
            min_value = i

if summation == 0:            
    print(-1)    

else:
    print(summation)
    print(min_value)
