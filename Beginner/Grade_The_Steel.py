t = int(input())

for i in range(t):
    ans = 0
    a, b, c = input().split()
    a, b, c = float(a), float(b), float(c)

    if a > 50 and b < 0.7 and c > 5600:
        ans = 10
    elif a > 50 and b < 0.7:
        ans = 9
    elif b < 0.7 and c > 5600:
        ans = 8
    elif a > 50 and c > 5600:
        ans = 7
    elif a > 50 or b < 0.7 or c > 5600:
        ans = 6
    else:
        ans = 5
    print(ans)