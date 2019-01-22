t = int(input())

for i in range(t):
    n = input()
    sn = set(n)
    f=False
    d = {}
    for i in sn:
        d[i] = n.count(i)

    for ch in sn:
        if d[ch] == len(n)-d[ch]:
            f=True
            break
        else: continue

    if f:
        print("YES")
    else:
        print("NO")