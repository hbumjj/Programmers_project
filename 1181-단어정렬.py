n = int(input())
arr = []

for _ in range(n):
    string = str(input())
    length = len(string)
    
    if [length, string] not in arr:
        arr.append([length, string])

# sorted key 활용
result = sorted(arr, key = lambda arr : [arr[0], arr[1]])

for i in result:
    print(i[1])