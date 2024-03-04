# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:37:24 2024

@author: user
"""

# example
#people = [20, 7, 23, 19, 10, 15, 25, 8, 13]

people = []
for i in range(9):
    a = int(input())
    people.append(a)

total = sum(people)

one = 0
two = 0
for i in range(9):
    for j in range(9):
        if i == j:
            pass
        else:
            if total - people[i] - people[j] == 100:
               one = people[i]; two = people[j];
               break;

# 퀵 정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num == one or num == two:
            pass
        else:
            if num < pivot:
                lesser_arr.append(num)
            elif num > pivot:
                greater_arr.append(num)
            else:
                equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
    
result = quick_sort(people)
for i in result:
    print(i, end = ' ')
