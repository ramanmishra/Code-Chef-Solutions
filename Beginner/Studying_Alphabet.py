s = input()
t = int(input())

for i in range(t):
    w = input()
    z = all((j in s) for j in w)

    if z:
        print('Yes')
    else:
        print('No')
