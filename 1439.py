# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:54:24 2024

@author: user
"""

'''
1439
다솜이는 0과 1로 이루어진 문자열,
행동: 연속된 하나의 이상의 숫자를 잡고 뒤집기

최소의 수를 찾자.
그룹으로 나누면?

ex. 11 00 11 00 11 00 11 00000 1
최소 그룹수가 정답이다.
'''

arr = [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1]
arr = [0,0,1,1,0,0]
arr = [1,1,1,0,1,1,0,1]

import math
arr = list(str(input()))

c = 0
start = arr[0]

for i in arr[1:]:
    if start != i:
        c += 1
        start = i

# print(c)
# # if c == 1:
# #     print(1)
# # else:
print(math.ceil(c/2))
