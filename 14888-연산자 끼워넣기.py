# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:36:08 2024

@author: user
"""

# 연산자 끼워넣기

'''
# example
n = 6 # len(arr)
arr = [1, 2, 3, 4, 5, 6]
a,b,c,d = 2, 1, 1, 1 # 연산자 각각 + - * %
'''
# =============================================================================
# Input
# =============================================================================
n = int(input())
arr = list(map(int, input().split(' ')))
a, b, c, d = map(int, input().split(' '))

min_value =  int(1e9)
max_value = int(-1e9)
stack_arr = ['+']*a + ['-'] *b + ['*']*c + ['%']*d
# =============================================================================
# 방법 1 - 순열로 해결
# =============================================================================

# def calculation(a, b, stack):
#     if stack == '+':
#         c = a + b
#     elif stack == '-':
#         c = a - b
#     elif stack == '*':
#         c = a * b
#     elif stack == '%':
#         if a < 0:
#             c = -1 * ((-1 * a) // b)
#         else:
#             c = a//b
#     return c

# def module(arr, max_value, min_value, stack_combination):
#     for stack_in in stack_combination:
#         value = arr[0]
#         for factor, stack in zip(arr[1:], stack_in):
#             value = calculation(value, factor, stack)     
            
#         min_value = min(min_value, value)
#         max_value = max(max_value, value)
    
#     return min_value, max_value

# from itertools import permutations

# stack_combination = list(permutations(stack_arr, n-1))
# a, b = module(arr, max_value, min_value, stack_combination)
# print(b)
# print(a)

# =============================================================================
# 방법 2 - 백트래킹으로 해결
# =============================================================================
def recur(sum, a, b, c, d, idx):
    
    global min_value
    global max_value
    
    if idx == n:
        min_value = min(min_value, sum)
        max_value = max(max_value, sum)
        return
    
    if a:
        recur(sum + arr[idx], a-1, b, c, d, idx+1)
    if b:
        recur(sum - arr[idx], a, b-1, c, d, idx+1)
    if c:
        recur(sum * arr[idx], a, b, c-1, d, idx+1)
    if d:
        recur(int(sum / arr[idx]), a, b, c, d-1, idx+1)
            
recur(arr[0], a, b, c, d, 1) # arr[0]: total # 0: length
print(max_value)
print(min_value)
