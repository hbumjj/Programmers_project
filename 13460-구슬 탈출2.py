# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:37:14 2024

@author: user
"""
from collections import deque

N,M = map(int, input().split())

matrix = []
rx = 0; ry = 0; bx = 0; by = 0;

for i in range(N):
    row = list(input())
    matrix.append(row)
    for j in range(len(row)):
        if row[j] == 'R':
            rx, ry = i, j
        if row[j] == 'B':
            bx, by = i, j


dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]

que = deque()
que.append([rx,ry,bx,by, 1])

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def move(x, y, idx): # 방향에 맞추어서 진행
    # 위, 좌, 아래, 우
    
    cnt = 0
    
    while matrix[x+dx[idx]][y+dy[idx]] != '#' and matrix[x][y] != 'O':
        x +=dx[idx]
        y +=dy[idx]
        cnt+=1
    return x, y, cnt

while que:
    rx,ry,bx,by,depth = que.popleft()
    go = 0
    if depth > 10:
        break;
        
    for i in range(4):
        rrx, rry, rcnt = move(rx, ry, i)
        bbx, bby, bcnt = move(bx, by, i)
        
        if matrix[bbx][bby] != 'O':
            if matrix[rrx][rry] == 'O':
                go = 1
                break;
        
            if rrx == bbx and rry == bby: # 겹치는 부분에 대해서 제거
                if rcnt > bcnt:
                    rrx = rrx-dx[i]
                    rry = rry-dy[i]
                
                elif rcnt < bcnt:
                    bbx = bbx - dx[i]
                    bby = bby - dy[i]
            
            if not visited[rrx][rry][bbx][bby]:
                visited[rrx][rry][bbx][bby] = True
                que.append([rrx,rry,bbx,bby, depth+1])
    if go == 1:
        print(depth)
        break
    
if go == 0:
    print(-1)

'''
N, M = 5, 5

# matrix = [['#','#','#','#','#'],['#','.','.','B','#'],['#','.','#','.','#'],['#','R','O','.','#'],['#','#','#','#','#']]
# #matrix = [['#','#','#','#','#'],['#','.','.','B','#'],['#','.','#','.','#'],['#','R','O','.','#']]

N,M = map(int, input().split())

matrix = []
rx = 0; ry = 0; bx = 0; by = 0;

dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]
# dx = [1,0,-1,0] 
# dy = [0,-1,0,1]

for i in range(N):
    row = list(input())
    matrix.append(row)
    for j in range(len(row)):
        if row[j] == 'R':
            rx, ry = i, j
        if row[j] == 'B':
            bx, by = i, j


def move(x, y, idx): # 방향에 맞추어서 진행
    # 위, 좌, 아래, 우
    
    cnt = 0
    
    while matrix[x+dx[idx]][y+dy[idx]] != '#' and matrix[x][y] != 'O':
        x +=dx[idx]
        y +=dy[idx]
        cnt+=1
    return x, y, cnt
    


answer = 11

def DFS(rx, ry, bx, by, depth):
    global answer
    if depth > 10:
        return
    
    
    for i in range(4):
        rrx, rry, rcnt = move(rx, ry, i)
        bbx, bby, bcnt = move(bx, by, i)
        
        if matrix[bbx][bby] == 'O':
            return
        
        if matrix[rrx][rry] == 'O':
            answer = min(answer, depth)
            return
        
        if rrx == bbx and rry == bby:
            if rcnt > bcnt:
                rrx = rrx-dx[i]
                rry = rry-dy[i]
            
            elif rcnt < bcnt:
                bbx = bbx - dx[i]
                bby = bby - dy[i]
        
        #print("######", rrx,rry,bbx,bby, i, depth)
        
        DFS(rrx,rry,bbx,bby,depth+1)


DFS(rx,ry,bx,by, 1)

if answer == 11:
    print(-1)
else:
    print(answer)        
    












'''









#상하좌우에 따라서 각각 작성
# def up(matrix):
#     for i in range(M):
#         turn = False
#         for j in range(N-1, -1, -1):
#             point = matrix[j][i]
#             print(point)
            
#             if point == 'R':
#                 turn = True
            
#             if turn == True:
#                 if point != '#' or point != 'B':
                    
#         print()


# def up(matrix):
#     for i in range(M):
#         for j in range(N):
#             point = matrix[j][i]
            
#             if point == 'R':
#                  for move in range(M):
#                      if matrix[move][i] == '#' or matrix[move][i] == 'B':
#                          pass;
#                      else:
#                          matrix[move][i] = point
#                          matrix[j][i] = '.'
#                          break;
                         
#             if point == 'B':
#                 for move in range(M):
#                     if matrix[move][i] == '#' or matrix[move][i] == 'R':
#                         pass
#                     else:
#                         if move == j:
#                             pass;
#                         else:
#                             matrix[move][i] = point
#                             matrix[j][i] = '.'
#                             break;
#     return matrix

# def down(matrix):
#     for i in range(M):
#         for j in range(N-1, -1, -1):
#             point = matrix[j][i]
#             if point == 'R':
#                   for move in range(M-1, -1, -1):

#                       if matrix[move][i] == '#' or matrix[move][i] == 'B':
#                           pass
#                       else:
                          
#                           if move == j:
#                               pass
#                           else:
#                               matrix[move][i] = point
#                               matrix[j][i] = '.'
#                               break;
                         
#             if point == 'B':
#                 for move in range(M-1,-1,-1):
#                     if matrix[move][i] == '#' or matrix[move][i] == 'R':
#                         pass
#                     else:
#                         if move == j:
#                             pass
#                         else:
#                             matrix[move][i] = point
#                             matrix[j][i] = '.'
#                             break;

#     return matrix

# def left(matrix):
#     for i in range(M):
#         for j in range(N):
#             point = matrix[i][j]
#             print(point)
#         print()
    #         if point == 'R':
    #              for move in range(M):
    #                  if matrix[move][i] == '#' or matrix[move][i] == 'B':
    #                      pass;
    #                  else:
    #                      matrix[move][i] = point
    #                      matrix[j][i] = '.'
    #                      break;
                         
    #         if point == 'B':
    #             for move in range(M):
    #                 if matrix[move][i] == '#' or matrix[move][i] == 'R':
    #                     pass
    #                 else:
    #                     if move == j:
    #                         pass;
    #                     else:
    #                         matrix[move][i] = point
    #                         matrix[j][i] = '.'
    #                         break;
    # return matrix



# a = down(matrix)
# print(a)

