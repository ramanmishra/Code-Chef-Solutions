from math import gcd

t = int(input())

for i in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    hcf = gcd(a, b)
    lcm = a * b // hcf

    print(hcf, lcm)