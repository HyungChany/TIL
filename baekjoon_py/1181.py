a=int(input())
arr=[]
arr1=[]
for _ in range(a):
    arr.append(input())
arr=list(set(arr))
arr.sort()
x=1
while len(arr1)<len(arr):
    for i in range(len(arr)):
        if len(arr[i])==x:
            arr1.append(arr[i])
            # arr.remove(arr[i])
    x+=1 
for i in arr1:
    print(i)