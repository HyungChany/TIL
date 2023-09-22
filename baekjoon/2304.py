n=int(input())
arr=[]
for _ in range(n):
    a,b= map(int,input().split())
    arr.append([b,a])
arr.sort()

c=arr[n-1][0]
s,e=arr[n-1][1],arr[n-1][1]
for i in range(n-2,-1,-1):
    if s<arr[i][1]<e:continue
    elif arr[i][1]>e: 
        c+=(arr[i][1]-e)*arr[i][0]
        e=arr[i][1]  
    elif arr[i][1]<s:
        c+=(s-arr[i][1])*arr[i][0]
        s=arr[i][1]

print(c)