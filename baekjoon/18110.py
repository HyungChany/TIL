a=int(input())
if a==0:
    print(0)
else:
    arr=[int(input()) for _ in range(a)]
 
    b=a*0.15
    if b%1 >= 0.5:
        b=int(b)+1
    else: 
        b=int(b)
    arr=sorted(arr)[b : a-b]
    
    if sum(arr)/len(arr)%1 >=0.5:
        print(sum(arr)//len(arr)+1)
    else: print(sum(arr)//len(arr))
     