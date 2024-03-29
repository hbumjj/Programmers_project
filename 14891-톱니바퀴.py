# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:14:39 2024

@author: user
"""

from collections import deque

a = deque(list(map(int, list(input()))))
b = deque(list(map(int, list(input()))))
c = deque(list(map(int, list(input()))))
d = deque(list(map(int, list(input()))))

rotation = []
N = int(input())
for i in range(N):
    alpha = list(map(int,input().split()))
    rotation.append(alpha)

# =============================================================================
# 
# =============================================================================
# a = deque([1,0,0,0,1,0,1,1])
# b = deque([1,0,0,0,0,0,1,1])
# c = deque([0,1,0,1,1,0,1,1])
# d = deque([0,0,1,1,1,1,0,1])

# rotation = [[1,1],[2,1],[3,1],[4,1],[1,-1]]

# a = deque([0,0,1,0,0,0,0,1])
# b = deque([1,1,1,1,1,1,0,1])
# c = deque([1,0,0,0,0,0,0,0])
# d = deque([0,0,0,0,0,0,0,0])

# rotation = [[3,1]]



# =============================================================================
# 
# =============================================================================

dic = {'a':1, 'b':2, 'c':3, 'd': 4}

def BACK(r, way, visited):
    
    if all(visited) == True:
        return
    
    visited[r-1] = 1
    if r == 1:
        flag = a
        #around = [[],(b,2)]
        around = [(b,2), []]
    elif r == 2:
        flag = b
        #around = [(a,1),(c,3)]
        around = [(c,3),(a,1)]
    elif r == 3:
        flag = c
        #around = [(b,2),(d,4)]
        around = [(d,4),(b,2)]
    else:
        flag = d
        #around = [(c,3),[]]
        around = [[],(c,3)]
    point = [flag[2], flag[6]]
    
    if way == 1:
        s = flag.pop()
        flag.appendleft(s)
    elif way == -1:
        s = flag.popleft()
        flag.append(s)
    else:
        pass
    #print(flag, r, way, visited)
    for n,(i,p) in enumerate(zip(around, point)):
        if i != [] and visited[i[1]-1] == 0:
            #print(flag, r, way, visited, p)
           
            if n == 0:
                check = i[0][6]
            elif n == 1:
                check = i[0][2]

            if check == p:
                preway = 0
            else:
                preway = way*-1
                
            #print(i, check, way)

            BACK(i[1], preway, visited)
        
for r in rotation:
    visited = [0] * 4
    BACK(r[0],r[1], visited)
#    print(a,b,c,d)
    
sum_ = 0
for i,score in zip([a,b,c,d],[1,2,4,8]):
    if i[0] == 0:
        sum_ += 0
    elif i[0] == 1:
        sum_ += score


print(sum_)