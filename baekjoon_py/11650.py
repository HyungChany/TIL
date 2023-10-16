n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort()

for i in arr:
    print(*i)