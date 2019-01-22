t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1]:
        print(2)
    else:
        print(a[1])