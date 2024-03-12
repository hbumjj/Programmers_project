# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:42:21 2024

@author: user
"""

# arr = [3, 1, 2, 3, 4, 1, 1, 2]
# arr = [3, 1, 1 ,1, 4, 1, 1, 2]

n,a = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
criteria = 0

c = max(arr)
count = 0
while count <= c:
    for i in range(1, len(arr)-1):
        
        front_max = max(arr[:i])
        back_max = max(arr[i+1:])
        
        criteria = min(front_max, back_max)
    
    
        if criteria > arr[i]:
            result += (criteria- arr[i])    
            arr[i] += (criteria-arr[i])
        
        count += 1
        
        #print(criteria, arr[i], result)

print(result)
        
        
