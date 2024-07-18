# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:46:33 2024

@author: rapa
"""

# 1436 - 영화감독 숌

# 1 -> 666
# n = 500


idx = 1
number = 666
n = int(input())

while idx != n:
    if idx >= 10000:
        break;
    number += 1
    if "666" in str(number):
        idx += 1
    
print(number)