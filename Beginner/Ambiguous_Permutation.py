while int(input()) != 0:
    a = list(map(int, input().split()))
    ans = [None] * len(a)
    for j in range(0, len(a)):
        ans[a[j]-1] = j + 1
    if ans == a:
        print("ambiguous")
    else:
        print("not ambiguous")