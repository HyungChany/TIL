a=int(input())
arr=list(map(int,input().split()))
arr1=[1]*a
for i in range(1,a):
    x=[]
    for j in range(i):
        if arr[i]>arr[j]: x.append(arr1[j])
    if x: arr1[i]=max(x)+1
print(max(arr1))