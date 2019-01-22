a = int(input())
x = []
prev_si = 0
prev_ti = 0
for i in range(a):
    si, ti = input().split(" ")
    si = int(si)
    ti = int(ti)
    prev_si += si
    prev_ti += ti
    if (prev_si > prev_ti):
        x += [(1, prev_si - prev_ti)]
    else:
        x += [(2, prev_ti - prev_si)]
ans = max(x, key=lambda key: key[1])
print(*ans)