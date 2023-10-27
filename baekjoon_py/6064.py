for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    f = 1
    while(x <= a*b):
        if x%b == y%b:
            print(x)
            f = 0
            break
        x += a
    if f: print(-1)