# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:44:16 2024

@author: user
"""

# 코딩테스트에서 유용한 모듈

# =============================================================================
# 순열과 조합 툴
# =============================================================================
from itertools import permutations, combinations

'''
permutations: 순서 중요
combinations: 순서 중요하지않음
'''
a = ['a' , 'b', 'c'] 

#print(list(permutations(a, 2)))
#print(list(combinations(a, 3)))

# =============================================================================
# 순열과 조합 구현 
# =============================================================================

# 순열 permutations
used = [0]*len(a)
arr = []

def permu(arr, n, input_list):
    if n == len(input_list):
        print(arr)
        return # 다 배열 완료했으면 출력
    
    for i in range(len(input_list)):
        if not used[i]:
            used[i] = 1 # 방문
            arr.append(input_list[i]) # arr에 추가
            permu(arr, n+1, input_list) # 재귀로 계속해서 배열 수행            
            arr.pop()  # 백트래킹 방문 해제
            used[i] = 0 
        
permu([],0, a)


# 조합 combinations
answer_list = []
def combi(n, ans, input_list):
    if n == len(input_list):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(input_list[n])
    combi(n+1, ans, input_list)  
    ans.pop()
    combi(n+1, ans, input_list)

combi(0, [], a)
print(answer_list)

# =============================================================================
# n 진수 변환
# =============================================================================
bit = 10
bit >> 2
print(bit)