# 1300번 해설

[1300 K번째 수] (https://www.acmicpc.net/problem/1300)
난이도: 10

```python
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
```

**(모든 인덱스는 1부터 시작한다)**
배열B의 k번째 수 구하기
구해야 하는 것: n 이하인 수의 개수가 k 이상일 때의 n의 최솟값
n은 1 이상 k 이하의 수 이므로 이분 탐색 알고리즘을 이용한다.

`start = 1`, `end = k` 일때
`mid = (start+end)//2` 로 잡는다.
이때 mid 이하인 수의 개수는
코드의 12번째 줄을 통해 구한다.
> (만약 `N = 10`이고 20이하의 수의 개수를 찾을때)
> 10*10에서 20 이하의 수는
> 1\*1 ~ 1\*10 (10개)
> 2\*1 ~ 2\*10 (10개)
> 3\*1 ~ 3\*6 (6개)
> ...
> 10\*1 ~ 10\*2 (2개)
> 이렇게 존재할텐데 이는
> `20//1`: 10개 (단, N을 초과할 수 없다.)
> `20//2`: 10개 (마찬가지)
> `20//3`: 6개
> ....
> `20//10`: 2개
> 따라서 위 코드에서 `min(mid//i, n)` 이런식으로
> 표현하는 것이다.
만약 `cnt`가 `k` 이상이라면 `answer`에 `mid`값을 할당,
`n`은 `mid`보다 작아야하므로 `end`를 `mid-1`값으로 줄여주고,
만약 `cnt`가 `k` 미만이라면 `n`은 `mid`보다 커야하므로
`start`를 `mid+1`값으로 늘려준다.

while문이 끝나면 `answer`값을 `print`해준다.