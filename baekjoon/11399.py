n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
c=0
for i in range(1,n+1):
    c+=(i*arr[i-1])
print(c)