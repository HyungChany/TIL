for tc in range(int(input())):
    a=int(input())
    b=int(input())
    
    arr=[[0]*15 for _ in range(15)]
    for i in range(15):
        arr[0][i]=i

    for i in range(1,15):
        for j in range(1,15):
            arr[i][j]=arr[i][j-1]+arr[i-1][j]

    print(arr[a][b])