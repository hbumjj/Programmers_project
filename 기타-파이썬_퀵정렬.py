# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:06:12 2024

@author: user
"""

# 기타 - 파이썬 퀵정렬
arr = [20, 7, 23, 19, 10, 15, 25, 8, 13]

def quick_sort(arr):
    left, equal, right = [], [], []
    
    if len(arr) <= 1:
        return arr
    else:
        criteria = arr[len(arr)//2]
        for i in arr:
            if i > criteria:
                right.append(i)
            elif i < criteria:
                left.append(i)
            else:
                equal.append(i)
        return quick_sort(left) + equal + quick_sort(right)

print(quick_sort(arr))