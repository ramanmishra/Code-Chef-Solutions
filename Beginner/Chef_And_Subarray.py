t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    count = 0
    for j in range(n):
        product = arr[j]
        addition = arr[j]
        for k in range(j + 1, n):
            if product == addition:
                count += 1
            product *= arr[k]
            addition += arr[k]
        if product == addition:
            count += 1
    print(count)
