while 1:
    arr=list(map(int,input().split()))
    if sum(arr)==0: break
    arr.sort()
    
    if arr[2]**2==arr[0]**2+arr[1]**2:
        print('right')
    else: print('wrong')