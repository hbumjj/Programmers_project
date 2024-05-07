# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:42:41 2024

@author: user
"""

while True:
    
    a,b = map(int,input().split())
    
    if a == 0 and b == 0:
        break;
    
    
    flag = True
    if a > b: # 배수인지 확인
        n = 1
        while a >= n*b:
            if n*b == a:
                print("multiple")
                flag = False
                break;
            n+=1
              
    elif a < b: # 약수인지 확인
        n = 1   
        while a <= b/n:
            if b/n == a:
                print("factor")
                flag = False
                break;
            n+=1
    
    if flag == True:
        print("neither")