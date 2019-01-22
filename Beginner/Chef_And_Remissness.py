t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a != b:
        print(max(a, b), a + b)
    else:
        print(a)
