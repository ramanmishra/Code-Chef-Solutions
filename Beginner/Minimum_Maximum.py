t = int(input())

for i in range(t):
    n = input()
    c = list(map(int, input().split()))
    minimum = min(c)
    print(minimum * (len(c) - 1))