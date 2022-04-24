n,k = map(int,[*open(0)])
start = 1
end = k

while start <= end:
    mid = (start+end)//2
    cnt = sum([min(mid//i, n) for i in range(1,n+1)])
    if cnt >= k:
        answer = mid
        end = mid-1
    else:
        start = mid+1
print(answer)