t = int(input())

for i in range(t):
    n = int(input())
    c = []
    ans = 0
    for j in range(n):
        c += (list(map(int, input().split())))
        ans = ans ^ (j + 1)

    print(ans)