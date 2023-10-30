for _ in range(int(input())):
    a = int(input())
    cz,co=1,0
    for i in range(a):
        cz,co = co,cz+co
    print(cz,co)