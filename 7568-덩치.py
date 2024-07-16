# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:04:25 2024

@author: rapa
"""
# 백준 7568 덩치
n = 5
arr = []
arr.append((55, 185, 0))
arr.append((58, 183, 1))
arr.append((88, 186, 2))
arr.append((60, 175, 3))
arr.append((46, 155, 4))

n = 6
arr = []
arr.append((55, 181, 0))
arr.append((54, 181, 1))
arr.append((56, 181, 2))
arr.append((55, 179, 3))
arr.append((56, 182, 4))
arr.append((54, 190, 5))

'''
3
1 2
2 2
2 3

22 22222789
11 98721

99 99
100 100

6
55 181
54 181

56 181

55 179

56 182
54 190

Output)
3 3 2 3 1 3

Answer)

2 2 1 3 1 1
'''
# =============================================================================
# 풀이본
# =============================================================================

n = int(input()); arr = []
for i in range(n):
     inn = list(map(int, input().split()))
     arr.append((inn[0], inn[1]))

rank = [1] * len(arr)
for idx, f in enumerate(arr):
    for compare in arr:
        # print(f, compare)
        if f[0] < compare[0] and f[1] < compare[1]:
            rank[idx] += 1
for i in rank:
    print(i, end = " ")

# =============================================================================
# 이전 풀이본
# =============================================================================
# n = int(input()); arr = []
# for i in range(n):
#     inn = list(map(int, input().split()))
#     arr.append((inn[0], inn[1], i))

# print(arr)

# sorted_arr = sorted(arr, reverse = True, key = lambda x : (x[0] + x[1]))

# checker = [[x[2], 1] for x in sorted_arr[:]]; c = 1
# print(sorted_arr)

# # ranking = [1] * len(arr); c = 1
# for idx in range(1, len(arr)):
#     pre = sorted_arr[idx-1]; nex = sorted_arr[idx] # 두개를 비교
    
#     # print(pre, nex)
#     if (pre[0] > nex[0]) and (pre[1] > nex[1]): # 덩치가 더 크다면
#         #ranking[idx] = ranking[idx-1] + c
#         checker[idx][1] = checker[idx-1][1] + c
#         # c = 1
#     elif (pre[0] > nex[0]) and (pre[1] >= nex[1]):
#         checker[idx][1] = checker[idx-1][1] + c
#         # c = 1
    
#     else:
#         #ranking[idx] = ranking[idx-1]
#         checker[idx][1] = checker[idx-1][1]
#         # c+=1


# for i in sorted(checker, key = lambda x : x[0]):
#     print(i[1], end = " ")
