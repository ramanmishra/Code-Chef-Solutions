t = int(input())


def sum_n(n):
    return n * (n + 1) // 2


for i in range(t):
    n = int(input())
    h = 0
    while sum_n(h) <= n:
        h += 1

    print(h - 1)