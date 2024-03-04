# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:16:38 2024

@author: user
"""

train = 0
result = 0
for station in range(10):
    out, in_ = map(int, input().split())
    train = train + in_ - out
    if train > result:
        result = train

print(result)