a=[int(input())]
c=0
while 1:
    if 1 in a: break
    aa=[]
    for i in a:
        if i%3==0: aa.append(i//3)
        if i%2==0: aa.append(i//2)
        aa.append(i-1)
    a=aa
    c+=1
print(c)