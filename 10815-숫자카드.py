# 백준 10815

# input
n = int(input())
parr = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# 배열 정렬
arr = sorted(parr)

# 같은 값 찾는 알고리즘
def algorithm(x):
    start = 0; end = n-1 # idx 
    while True:
        mid_idx = int((end + start)/2) # 중간지점 # 2, 0, 4
        
        if arr[mid_idx] <= x and x <= arr[end]: #뒷영역
            start = mid_idx + 1
        elif arr[mid_idx] >= x and x >= arr[start]: # 앞영역
            end = mid_idx - 1
        else:
            return 0
        
        if arr[mid_idx] == x or arr[end] == x or arr[start] == x:
            return 1
            
        if start >= end:
            return 0

# 결과 추출
for check in b:
    a = algorithm(check)
    print(a, end = " ")


