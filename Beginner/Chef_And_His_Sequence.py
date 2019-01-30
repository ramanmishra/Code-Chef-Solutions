t = int(input())

for i in range(t):
    n = input()
    arr = [int(elem) for elem in input().split()]
    f = input()
    sub_arr = [int(e) for e in input().split()]

    flag = True

    for j in sub_arr:
        if j in arr:
            flag = True
        else:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")

