n,k=map(int,input().split())
a,b=1,1
for i in range(n-k+1,n+1):
    a*=i
for i in range(1,k+1):
    b*=i
print(a//b)