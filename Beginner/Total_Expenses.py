t = int(input())

for i in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    price = a * b
    if a > 1000:
        ans = price - price * .1
        print("%.6f" % ans)
    else:
        print("%.6f" % price)