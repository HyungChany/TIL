a=[0]*26 

for _ in range(int(input())):
    x=input()
    for i in range(len(x)):
        a[ord(x[i])-65]+=10**(len(x)-i-1)
a.sort(reverse=True)

c,co=9,0
for i in a:
    if i==0: break
    else: co += i*c
    c-=1

print(co)