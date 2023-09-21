a=int(input())
arr=list(map(int,input().split()))
print(round((((sum(arr)/max(arr))*100)/a),6))