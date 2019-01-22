from math import gcd

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    a.remove(a[0])
    first_gcd = gcd(a[0], a[1])
    for j in range(1, len(a) - 1):
        first_gcd = gcd(first_gcd, a[j + 1])

    for x in a:
        print(x // first_gcd, end=" ")