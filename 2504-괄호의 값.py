# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:31:53 2024

@author: user
"""
from collections import deque

'''
string = '(()[[]])([])'

visit = [0 for _ in range(len(string))]
# de_string = deque(string)
# print(len(string))

# for i in range(int(len(string)/2)):
#     pass    

da = ['(', ')', '[', ']']

def pase(string):
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            print(visit)
            if visit[i] == 0:
                if da.index(string[i]) == da.index(string[j])+1:
                    visit[i] = 1; visit[j] = 1
                    break;
                
pase(string)
'''
# =============================================================================
# stack을 통한 풀이
# =============================================================================

# string = '(()[[]])([])'

# #string = '[][]((])'

# s1 = ['(', ')']
# s2 = ['[', ']']

# array = deque()

# result = ['(']
# idx = 0
# for i in range(len(string)):
#     if string[i] == '(' or string[i] == '[':
#         array.append(string[i])
#     else:
#         print(array[-1], string[i])
#         if array[-1] in s1 and array[-1] != s1[1] and string[i] in s1: #짝이라면 # ')'            
#             array.pop()
#             if '(' in array:
#                 result.append('+2')
#             elif array == deque([]):
#                 if i == len(string)-1:
#                     result.append(')*2')
#                 else:    
#                     result.append(")*2+(") # ()*2+
#             else:
#                 result.append('*2')
#         elif array[-1] in s2 and array[-1] != s2[1] and string[i] in s2: # 짝이라면 # ']'
#             array.pop()
            
#             if '[' in array:
#                 result.append('+3')
                
#             elif array == deque([]):
#                 if i == len(string)-1:
#                     result.append(")*3")
#                 else:
#                     result.append(")*3+(") #()*3+
                
#             else:
#                 result.append('*3')
#         else:
#             array.append(string[i])
    
#     print(string[i], array)

# print(result)

# =============================================================================
# 
# =============================================================================

string = '(()[[]])([])'

#string = '[][]((])'

s1 = ['(', ')']
s2 = ['[', ']']

array = deque()

result = 0
idx = 1


# for i in range(len(string)):
#     if string[i] == '(' or string[i] == '[':
#         array.append(string[i])
#     else:
#         print(array[-1], string[i])
#         if array[-1] in s1 and array[-1] != s1[1] and string[i] in s1: #짝이라면 # ')'            
#             array.pop()
            
#         elif array[-1] in s2 and array[-1] != s2[1] and string[i] in s2: # 짝이라면 # ']'
#             array.pop()

#         else:
#             array.append(string[i])
    
#     print(string[i], array)

# print(result)

# =============================================================================
# 
# =============================================================================
from collections import deque


#string = input()
string = "[][]((])"
array = deque()

result = 0
idx = 1

for i in range(len(string)):
    if string[i] == '(':
        array.append(string[i])
        idx*=2
        
    elif string[i] == '[':
        array.append(string[i])
        idx*=3
        
    elif string[i] == ')':
        if not array or array[-1] == '[':
            result = 0
            break; # 예외처리
        
        if string[i-1] == '(':    
            #print(array[-1], string[i-1])
            result+=idx
            
        idx = int(idx/2)
        array.pop()

    else:
        if not array or array[-1] == '(':
            result = 0
            break;
        if string[i-1] == '[':
            
            result += idx
            
        idx = int(idx/3)
        array.pop()

if array:
    result = 0
print(result)

# result = 0
# tmp = 1



# for i in range(len(string)):
#     if string[i] == '(':
#         array.append(string[i])
#         idx*=2
        
#     elif string[i] == '[':
#         array.append(string[i])
#         idx*=3
        
#     elif string[i] == ')':
#         if not array or array[-1] == '[':
#             result = 0
#             break; # 예외처리
        
#         if array[-1] == '(':    
#             result+=idx
            
#         idx = int(idx/2)
#         array.pop()

#     else:
#         if not array or array[-1] == '(':
#             result = 0
#             break;
            
#         if array[-1] == '[':
            
#             result += idx
            
#         idx = int(idx/3)
#         array.pop()
#     print(array, result, idx)
