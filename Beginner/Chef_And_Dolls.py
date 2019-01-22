t = int(input())

for i in range(t):
    n = int(input())
    c = []
    ans = 0
    for j in range(n):
        c += [int(input())]

    sc = set(c)

    for k in sc:
        if c.count(k) % 2 != 0:
            ans = k
            break
    print(ans)