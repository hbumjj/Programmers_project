# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:53:32 2024

@author: rapa
"""

'''
온라인 저지에 가입한 사람들 나이와 이름
회원들 나이가 증가하는 순, 같으면 가입한 사람 순

20 Sunyoung
21 Junkyu
21 Dohyun

'''

age = [21, 21, 20]
name = ['Junkyu', 'Dohyun', 'Sunyoung']

arr = [(21, 0, 'Junkyu'), (21, 1, 'Dohyun'), (20, 2, 'Sunyoung')]


N = int(input()) 
arr = []
for i in range(N):
    a = list(map(str, input().split()))
    
    c = (int(a[0]), i, a[1])
    arr.append(c)

s_age = sorted(arr)


for ss in s_age:
    print(ss[0], ss[2])

