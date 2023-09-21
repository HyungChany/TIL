a,b=map(int,input().split())

arr=[]
for i in range(1,a+1):
    arr.append(i)
x=b-1
arr1=[]

while len(arr1)<a:  
    arr1.append(arr[x])
    arr.remove(arr[x])
    if not arr: break
    x+=b-1
    if x>=len(arr): 
        x%=len(arr)
    if len(arr)==1: arr1.append(arr[0])
print('<',end='')    
print(*arr1,sep=', ',end='')
print('>')