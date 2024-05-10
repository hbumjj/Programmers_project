# 카드 n개를 가지고 있다.
# 정수 m이 주어졌을 때, 
# 첫째 줄에는 카드 개수
# 둘째줄에는 숫자 카드에 적효죠 있는 정수

# 셋째줄에는 m
# 넷째줄에는 

# 10을 서칭... n에 대해서... couter

# =============================================================================
# counter 풀이
# =============================================================================
# from collections import Counter

# N = int(input())

# n = list(map(int,input().split()))

# dic = Counter(n)

# M = int(input())

# m = list(map(int,input().split()))

# for c in m:
#     try:
#         print(dic[c], end = " ")
#     except:
#         print(0, end = " ")
        
      
# =============================================================================
# binary search
# =============================================================================
import sys
input = sys.stdin.readline

N = int(input())

n = list(map(int,input().split()))

M = int(input())

m = list(map(int,input().split()))

# N = 10
# n = [6,3,2,10,10,10,-10,-10,7,3]
# M = 8
# m = [10, 9, -5, 2, 3, 4, 5, -10]


'''
특정값 시작 --> ex. 10 --> 정렬된 상태에서, 같으면 +1 , 다르면 pass 만약에 더 크거나, 작으면 범위가 변경된다.
'''

n = sorted(n)
dic = {}
for i in n:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1


def binary(start, end, t):
    
    if start > end:
        return 0
    
    mid = (start + end)//2 # 중간 인덱스
    
    if n[mid] == t:
        return dic[t]
    
    elif n[mid] > t:
        end = mid - 1
    
    elif n[mid] < t:
        start = mid + 1
        
    return binary(start, end, t)
    
    
t = 9; start = 0; end = len(n)-1


for t in m:
    a = binary(start, end, t)
    print(a)
    

