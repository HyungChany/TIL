n = int(input())
arr = list(map(int,input().split()))
x = {}

arr1 = sorted(set(arr))

for i in range(len(arr1)):
    x[arr1[i]] = i

for j in arr:
    print(x[j], end=' ')