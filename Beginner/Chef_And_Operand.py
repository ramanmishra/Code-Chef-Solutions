t = int(input())
for i in range(t):
    a, b = input().split()
    a, b = int(a), int(b)

    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")