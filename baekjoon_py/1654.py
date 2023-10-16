k,n = map(int,input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
s = 1
e = max(arr)

while s<=e:
    m = (s+e) // 2
    c = 0
    for i in range(k):
        c += arr[i] // m
    if c >= n:
        s = m+1
    else:
        e = m-1
print(e)