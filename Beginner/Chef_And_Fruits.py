t = int(input())

for i in range(t):
    a, o, c = input().split()
    a, o, c = int(a), int(o), int(c)

    orangeAppleDiff = abs(a - o)

    if c >= orangeAppleDiff or orangeAppleDiff == 0:
        print(0)
    else:
        print(orangeAppleDiff - c)