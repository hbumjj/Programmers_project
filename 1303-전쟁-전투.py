# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:26:44 2024

@author: user
"""

'''
- DFS 풀이
- 각 좌표별로 시작점을 만들어서 수행 (2중 for문)
- 방문한 지점은 1로 수정 및 연속된 값일 때마다 개수 카운팅 (summer)
- DFS 알고리즘이 끝날때마다, 최종 결과값을 위한 합으로 추가
'''

# Input
matric = []
cols, rows = map(int, input().split())

for i in range(rows):
    inp = input()
    matric.append([str(inp)])


# Input Example
# rows, cols = 5,5
# matric = [["WBWWW"],['WWWWW'],['BBBBB'],['BBBWW'],['WWWWW']]

# =============================================================================
# DFS 풀이 방법
# =============================================================================
visit = [[0]*cols for i in range(rows)] # 방문한 지점 체크를 위한 빈 배열

way_x = [0,0,-1,1] # x,y 방향
way_y = [-1,1,0,0]

sum_w, sum_b = 0, 0 # 최종 결과 변수

def DFS(x,y, visit, upper, summer):
    visit[x][y] = 1 # 방문 시 1로 변환
    for nx, ny in zip(way_x, way_y):
        if nx+x >=0 and ny+y >= 0 and nx+x <rows and ny+y <cols: # 인덱스를 벗어나지 않기 위해
            if visit[nx+x][ny+y] == 0 and matric[nx+x][0][ny+y] == upper: # 해당 지점을 방문하지 않았으면서 (visit = 0) 찾고자하는 값 ('W' or 'B')
                summer = DFS(nx+x, ny+y, visit, upper, summer+1) # 구한 값을 return으로 반환
    return summer
    
for i in range(rows):
    for j in range(cols): # DFS 알고리즘이 중간에 끊기기 때문에 계속해서 새로운 좌표로 시작
        if visit[i][j] != 1:
            if matric[i][0][j] == 'W': # 'W' 일때를 찾아주기
                sum_w += (DFS(i,j, visit, 'W', 1))**2 # 끊길때마다 최종 결과값에 더해주기 ('W')
     
            elif matric[i][0][j] == 'B': # 'B' 일때를 찾아주기
                sum_b +=  (DFS(i,j, visit, 'B', 1))**2 # 끊길때마다 최종 결과값에 더해주기 ('B')

print(sum_w, sum_b)
