t = int(input())

for i in range(t):
    d, n = input().split()
    d, n = int(d), int(n)

    initial_sum = (n * (n + 1)) // 2
    for i in range(d-1):
        initial_sum = (initial_sum * (initial_sum + 1)) // 2

    print(initial_sum)