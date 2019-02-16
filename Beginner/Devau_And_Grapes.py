t = int(input())

for i in range(t):
    ans = 0
    n, k = map(int, input().split())
    buckets = [int(temp) for temp in input().split()]
    for j in buckets:
        if j >= k:
            ans += min(j % k, k - (j % k))
        else:
            ans += k - (j % k)

    print(ans)
