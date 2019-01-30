t = int(input())

for i in range(t):
    length = input()
    l = [int(j) for j in input().split()]
    r = [int(k) for k in input().split()]
    ans = (0, 0, 0)

    for m in range(len(l)):
        product = l[m] * r[m]

        if product > ans[0]:
            ans = (product, r[m], m + 1)
        if product == ans[0]:
            if r[m] > ans[1]:
                ans = (product, r[m], m + 1)
                if r[m] == ans[1]:
                    ans = (product, r[m], m + 1)
    print(ans[2])
