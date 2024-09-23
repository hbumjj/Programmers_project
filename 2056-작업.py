# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:46:31 2024

@author: user
"""

# 걸리는 시간, 작업에 대한 선형 관계에 있는 작업들 개수, 선형 단계 개수

# work = {0: }
'''

1 5초
2 1개 - 1, 1초 -> 6초
3 1개 - 2, 3초 -> 9초
4 1개 - 1, 6초 -> 11초
5 2개 - 2,4 1초 -> 

'''
n = int(input())
end = {}
q = []
for c_n in range(n):
    nn = list(map(int, input().split()))
    if c_n == 0:
        end[c_n + 1] = nn[0]
    else:
        end[c_n +1] = 0
        q.append(nn)

for c, i in enumerate(q):
    subject_number = c+2 #  2번째 작업부터 시작
    pre_subject = i[2:] # 선행작업리스트
    pre_time = i[0] # 작업하는데 걸리는 시간
    if i[1] == 0:
        end[subject_number] = pre_time
    else:
        max_ = 0 # 초기화
        for pre in pre_subject:
            max_ = max(max_, pre_time + end[pre])
        
        end[subject_number] = max_

print(max(end.values()))