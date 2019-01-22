import math

t = int(input())

for i in range(t):
    r = int(input())
    c_x, c_y = input().split()
    c_x, c_y = int(c_x), int(c_y)
    s_x, s_y = input().split()
    s_x, s_y = int(s_x), int(s_y)
    s_c_x, s_c_y = input().split()
    s_c_x, s_c_y = int(s_c_x), int(s_c_y)
    c = 0

    dist_c_from_s = math.sqrt(abs(c_x - s_x) ** 2 + abs(c_y - s_y) ** 2)
    dist_s_from_s_c = math.sqrt(abs(s_x - s_c_x) ** 2 + abs(s_y - s_c_y) ** 2)
    dist_c_from_s_c = math.sqrt(abs(c_x - s_c_x) ** 2 + abs(c_y - s_c_y) ** 2)

    if dist_c_from_s <= r:
        c += 1
    if dist_s_from_s_c <= r:
        c += 1
    if dist_c_from_s_c <= r:
        c += 1

    if c >= 2:
        print("yes")
    else:
        print("no")