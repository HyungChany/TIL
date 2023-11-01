y,x=map(int,input().split())
a=list(map(int,input().split()))
arr=[[0]*x for _ in range(y)]
for i in range(x):
    for j in range(y):
        if j<a[i]: arr[j][i]=1
        else: break
l,c,co=0,0,0
for i in range(y):
    for j in range(x):
        if j==0: 
            l=0
            co=0
        if arr[i][j]==1 and co==0: l=1
        elif arr[i][j]==0 and l==1: co+=1
        elif arr[i][j]==1 and l==1: 
            c+=co
            co=0

print(c)