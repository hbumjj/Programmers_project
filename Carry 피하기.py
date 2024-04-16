def cal(num1, num2): # 두 수에 대해서 가능여부 계산
    while num1 > 0 and num2 > 0:
        c1 = int(num1) % 10 # 자리수계산
        c2 = int(num2) % 10 # 자리수계산
        
        if c1 + c2 >= 10: # 자리수가 10이 넘는 경우에는 바로 탈락
            return False
        
        num1 /= 10
        num2 /= 10

    return True


def BackTracking(answer, arr, idx, count): # answer: 현재 누적값, arr: 주어진 배열, idx: 시작점, count: 현재 깊이
    global result
    
    result = max(count, result) # 지금까지 구한 깊이를 기반으로 최대값
    
    if len(arr) - idx + count <= result: # 이미 계산한 누적값과 그 이후에 얻을 값을 모두 포함해도 이미 result보다 작은 경우, return
        return
    
    for i in range(idx,len(arr)):
            if cal(answer, arr[i]): # 가능한 경우에만 간다.
                BackTracking(answer+arr[i], arr, i+1, count+1)


N = int(input())
arr = []
for i in range(N):
    a = int(input())
    arr.append(a)

result = 0 # 결과값

BackTracking(0, arr, 0,0)
print(result)