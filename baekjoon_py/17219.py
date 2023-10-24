a,b=map(int,input().split())
arr={}
for _ in range(a):
    x,y=input().split()
    arr[x]=y

for _ in range(b):
    print(arr[input()])
