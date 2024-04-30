# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:33:44 2024

@author: user
"""

N = int(input())
A = list(map(int,input().split()))
A = sorted(A)
M = int(input())

B = list(map(int,input().split()))

# for i in B:
#     if i in A:
#         print(1)
#     else:
#         print(0)


### 정답 풀이 # 이진탐색
for i in B:
    # 이진탐색은 중간이 핵심
    # 초기 인덱스 번호 정의
    start, end = 0, N-1
    idx = False
    
    while start <= end:
        
        mid = int((end+start)/2)
    
        if A[mid] == i:
            idx = True
            print(1)
            break;
            
        elif A[mid] > i: # 중간값보다 작은 경우 --> 중간 값을 더 작게 변경
            end = mid-1
        
        elif A[mid] < i:
            start = mid+1
    
    if idx == False:
        print(0)
            