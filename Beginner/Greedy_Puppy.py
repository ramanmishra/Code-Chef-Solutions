t = int(input())

for i in range(t):
    n, k = input().split()
    n, k = int(n), int(k)
    maxBone = 0
    r = k // 2 + 1
    for i in range(2, k + 1):
        if maxBone < n % i:
            maxBone = n % i
    print(maxBone)
