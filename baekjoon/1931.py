t=int(input())
arr=[list(map(int,input().split())) for _ in range(t)]
arr.sort(key=lambda x:(x[1],x[0]))
c,e=0,0
for i in range(t):
    if e<=arr[i][0]:
        c+=1
        e=arr[i][1]
print(c)