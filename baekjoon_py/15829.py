a=int(input())
arr=list(input())
c=0
for i in range(a):
    c+=31**i*(ord(arr[i])-96)
print(c%1234567891)