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
q = [[1,1,1],[3,1,2],[6,1,1],[1,2,2,4],[8,2,2,4],[4,3,3,5,6]]


end = {1:5, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0} # 총 작업별로 걸리는 시간



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

# print(q, end)

for c, i in enumerate(q):
    subject_number = c+2
    pre_subject = i[2:]
    pre_time = i[0]
    # print(" ")
    max_ = 0
    for pre in pre_subject:
        # print(subject_number, pre, end, pre_time)
        sam = pre_time + end[pre]
        max_ = max(max_, sam)
    
    if max_ != 0:
        end[subject_number] = max_

print(max_)