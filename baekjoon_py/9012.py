for _ in range(int(input())):
    arr=input()
    while '()' in arr:
        arr=arr.replace('()','')
    if len(arr)==0: print('YES')
    else: print('NO')