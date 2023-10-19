while 1:
    arr1=['[',']','(',')']
    arr=list(input())
    if arr[0]=='.' : break
    a=[]
    for i in arr:
        if i in arr1: a.append(i) 
    c=0
    while len(a)%2==0:
        for i in range(len(a)):
            if (a[i]=='['and a[i+1]==']') or (a[i]=='('and a[i+1]==')'):
                a.pop(i)
                a.pop(i)
                break
            if i==len(a)-2:
                c=1
                break
        if len(a)==0 or c==1:break
            
    if not a: print('yes')
    else: print('no')