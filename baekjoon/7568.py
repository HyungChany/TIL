a=int(input())
arr=[list(map(int,input().split())) for _ in range(a)]

for i in range(a):
    c=1
    for j in range(a):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1] and i != j:
            c+=1
    print(c,end=' ')