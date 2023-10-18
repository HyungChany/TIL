n=int(input())
arr=[]
arr1=[0]*8001
for i in range(n):
    x=int(input())
    arr.append(x)
    arr1[x+4000]+=1
a=sum(arr)

if (a/n)%1 >= 0.5:
    print(a//n+1)
elif (a/n)%1 <= -0.5:
    print(a//n-1) 
else: print(a//n)

arr.sort()
print(arr[n//2])

c=1
if arr1.count(max(arr1)) == 1:
    for i in range(8001):
        if max(arr1)==arr1[i]: print(i-4000)
else:
    for i in range(8001):
        if arr1[i]==max(arr1) and c==0: 
            print(i-4000)
            break
        elif arr1[i]==max(arr1) and c==1: 
            arr1[i]=0
            c-=1

print(max(arr)-min(arr))