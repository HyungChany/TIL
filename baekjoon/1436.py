a=int(input())
c=0
for i in range(10000000000):
    if '666' in str(i):
        c+=1
        if a==c: 
            print(i)
            break 