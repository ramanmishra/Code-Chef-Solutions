import math

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    p, q = a // g, b // g
    print(p * q)