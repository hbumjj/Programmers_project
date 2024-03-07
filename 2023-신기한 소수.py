# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:45:01 2024

@author: user
"""

# 신기한 소수자
# 모든 자리수가 소수가 되는 숫자를 찾자. 단 N자리수가 정해진다.

N = 4

#N = int(input())

# =============================================================================
# 시간초과 - 완전탐색
# =============================================================================
'''
def prime_number_detection(a):
    result = 0
    for i in range(2, a+1):
        if a%i == 0: 
            if a == i:
                return 1
            break;
        else:
            pass
    return result 

# 4--> 1000
# 뒤부터 수행

start = 10**(N-1)+1
end = 10**(N)


for i in range(start, end, 2):
    number = str(i)
    
    count = 0
    for idx in range(0, N):
        #print(number, number[0:idx+1])
        result = prime_number_detection(int(number[0:idx+1])) # 소수일 경우 1
        if result == 0:
            break; # 이미 신비한 소수가 아니므로 나감
        else:
            count+=1
    
    if count == N:
        print(number)
'''
# =============================================================================
# DFS
# =============================================================================

N = int(input())


def prime_number_detection(a): # 소수 판별 함수
    result = 0
    for i in range(3, a+1, 2):
        if a%i == 0: 
            if a == i:
                return 1
            break;
        else:
            pass
    return result 

def is_prime(n): # 더 효율적으로 작성한 함수
    # 소수가 되려면 절반 영역에서 나누어지는 것이 없어야함
    for i in range(2, int(n/2)+1): # 절반으로 줄임
        if n % i == 0:
            return 0
    return 1

def DFS(number, depth, N):
    
    if depth == N-1:
        print(number)
        return
        
    for i in range(1, 10, 2):
        number2 = int(str(number) + str(i))
        if is_prime(number2):
            DFS(number2, depth+1, N)

DFS(2, 0, N)
DFS(3, 0, N)
DFS(5, 0, N)
DFS(7, 0, N)
