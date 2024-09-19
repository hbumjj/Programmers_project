# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:48:44 2024

@author: rapa
"""
# arr = [1,2,3,4,2,5,3,1,1,2]; target = 5
# =============================================================================
# 
# =============================================================================
# 풀이 코드
n, target = map(int, input().split())
arr = list(map(int, input().split()))

flag = 0; first = 0; ans = 0
for idx in arr:
    flag += idx
    
    if flag == target:
        ans += 1
        
    while flag >= target:
        
        flag -= arr[first]
        first += 1
        if flag == target:
            ans += 1
            break;
            
print(ans)
# =============================================================================
# 
# =============================================================================
# 모범 답안
'''
sum을 기준으로 더 크면 빼주고, 더 작으면 제거해준다.
같으면 cnt를 추가해준다.
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))

sum = a[0]
left = 0
right = 1
cnt = 0

while True:
    if sum < m:
        if right < n:
            sum += a[right]
            right += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= a[left]
        left += 1
    else:
        sum -= a[left]
        left += 1

print(cnt)