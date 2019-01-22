t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 or y1 == y2:
        if x1 > x2:
            print('left')
        elif x1 < x2:
            print('right')
        elif y1 > y2:
            print('down')
        else:
            print('up')
    else:
        print('sad')