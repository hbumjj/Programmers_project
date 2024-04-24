# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:16:47 2024

@author: user
"""

#two_arr = list("1010")

#three_arr = list("212")

two_arr = list(str(input()))

three_arr = list(str(input()))

def two_to_ten(arr):
    answer = 0
    n = 0; lenth = len(arr)-1
    for i in arr:
        x = 2**(lenth-n)
        n+=1
        answer += x*int(i)
    return answer

def three_to_ten(arr):
    answer = 0
    n = 0; lenth = len(arr)-1
    for i in arr:
        x = 3**(lenth-n)
        n+=1
        answer += x*int(i)
    return answer


for i in range(len(two_arr)):
    two_arr[i] = str(1-int(two_arr[i]))
    
    for j in range(len(three_arr)):
        
        for dd in range(3): # 3진법으로 바꾸기
            if three_arr[j] != str(dd):
                point = three_arr[j]
                three_arr[j] = str(dd)
                
                #print(two_arr, three_arr)
                two_answer = two_to_ten(two_arr)
                three_answer = three_to_ten(three_arr)
                #print(two_answer, three_answer)
                if two_answer == three_answer:
                    print(two_answer)
            
                three_arr[j] = point
    two_arr[i] = str(1-int(two_arr[i]))
