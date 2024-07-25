# -*- coding: utf-8 -*-
"""

1차, 2차

B에 비해 서류 심사 결과와 면접 성적이 모두 떨어지면 A 선별 불가

'''
서류를 기준으로 정렬 후,
criteria = 최소한의 값을 선정한다. 뽑일 때마다.
이 criteria보다 순위가 높으면 갱신
'''

"""

n = 7
arr = [[3,6],[7,3],[4,2],[1,4],[5,7],[2,5],[6,1]]

n = 5
arr = [[3,2],[1,4],[4,1],[2,3],[5,5]]

# =============================================================================
# 
# =============================================================================
# Tn = int(input())

# for test in range(Tn):

#     arr = []
#     number = int(input())
#     for app in range(number):
#         a = list(map(int, input().split()))
#         arr.append(a)

#     sarr = sorted(arr, key = lambda arr: arr[0])
    
    
#     result = []
#     criteria = 0
#     for i in sarr:
#         if result == []:
#             result.append(i)
#             criteria = i[1]
        
#         if criteria > i[1]:
#             result.append(i)
#             criteria = min(criteria, i[1])
    
#     print(len(result))
    
# =============================================================================
# 
# =============================================================================

import sys

Tn = int(sys.stdin.readline())
# n = 5
# arr = [[3,2],[1,4],[4,1],[2,3],[5,5]]

for test in range(Tn):
    
    number = int(sys.stdin.readline()); dir_ = {}
    
    for idx in range(number):
        dir_[idx+1] = 0
    
    for app in range(number):
        a = list(map(int, sys.stdin.readline().split()))
        dir_[a[0]] = a[1] # 딕셔너리 화
    
    # 정렬된 딕셔너리
    criteria = dir_[1]; ans = 1
    
    for i in dir_.values():
        if criteria > i:
            ans += 1
            criteria = min(criteria, i)
    
    print(ans)
    
# =============================================================================
# 
# =============================================================================
