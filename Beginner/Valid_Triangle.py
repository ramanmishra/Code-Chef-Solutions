t = int(input())
for i in range(t):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if a + b + c == 180:
        print("YES")
    else:
        print("NO")