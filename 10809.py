# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:53:56 2024

@author: user
"""

# -*- coding: utf-8 -*-
# 10809번

"""
Created on Wed May 29 13:23:02 2024

@author: rapa
"""

alpha = ['a','b','c','d',
         'e','f','g','h',
         'i','j','k','l',
         'm','n','o','p',
         'q','r','s','t',
         'u','v','w','x',
         'y','z']
dic = {}

for i in alpha:
    dic[i] = -1

string = str(input())
#string = 'baekjoon'

for idx, s in enumerate(string):
    if dic[s] == -1:
        dic[s] = idx
    
for c in (list(dic.values())):
    print(c, end = " ")