n,k = map(int,input().split())
min = k*(k+1)//2
if min > n: 
    print(-1)
elif (n-min)%k==0:
    print(k-1)
else:
    print(k)