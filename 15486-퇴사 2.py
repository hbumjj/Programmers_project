# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:00:46 2024

@author: user
"""

# N = 7
# duration = [3, 5, 1, 1, 2, 4, 2]
# reward = [10, 20, 10, 20, 15, 40 ,200]

# max_value = 0

'''
def DFS(start, value, depth):
    global max_value
    if depth > N:
        return
    else:
        if max_value < value:
            max_value = value
    
    for idx in range(N):
        start = start + duration[idx]
        depth = depth + 1
        value += reward[idx]
        DFS(start, value, depth)
        

DFS(0, 0, 0)
print(max_value)
'''

'''
DP - Dynamic programming

하나의 큰 문제를 여러개의 작은 문제로 해결
답을 저장하고 재활용 - 기억하며 풀기

Bottom-up 방식: 아래에서 부터 계산을 수행 하고 누적시켜서 전체 큰 문제를 해결하는 방식
Top-down 방식: 위에서 부터 바로 호출을 시작해서 결과 값을 재귀를 통해 전이시켜 재활용
'''

'''
풀이 핵심 방식
1일까지 밖에 없을 때의 최댓값
2일까지 밖에 없을 때의 최댓값
3일까지 밖에 없을 때의 최댓값
N일까지 밖에 없을 때의 최댓값
'''

# # 1 days
# dp = [0, 0, 0, 10, 0, 0, 0, 0] # 1일차에는 0원이나, 3일 뒤에 10원이 벌린다.

# # 2 days
# dp = [0, 0, 0, 10, 0, 0, 20, 0] # 2일차에는 0원이나, 5일 뒤에 20원이 벌린다.

# # 3 days
# dp = [0, 0, 0, 10, 0, 0, 20, 0] # 3일차에는 10원을 벌수 있다. 그러나 3일차까지는 10이다.

# # 4 days
# dp = [0, 0, 0, 10, 30, 0, 20, 0] # 4일차에는 20원이 벌려있다. 총 30원 번다.

# # 5 days
# dp = [0, 0, 0, 20, 30, 30, 45, 0] # 5일차에는 아직까지는 30이다. 그러나 이틀 일하면 15가 추가되서 45 가능하다.

# # 6 days
# dp = [0, 0, 0, 20, 30, 30, 45, 0] # 6일차에 얻을 수 있는 수익은 45,
# # 그러나 더 일할 수 있다면?
# # 5일차일보다, 6일차일이 더 이득이다.

# # example 
# dp = [0, 0, 0, 20, 30, 30, 30+15, 0] # 5일차 일을 하는 경우
# dp = [0, 0, 0, 20, 30, 30, 30+40, 0] # 6일차 일을 하는 경우



n = 7
t = [0, 3, 5, 1, 1, 2, 4, 2]
p = [0, 10, 20, 10, 20, 15, 40 ,200]


dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값
    fin_date = i + t[i] - 1  # 당일 포함
    
    if fin_date <= n:  # 최종일 안에 일이 끝나는 경우
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
        
        print(fin_date, dp[fin_date], i, dp[i-1], p[i])
        
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])

print(max(dp))
















