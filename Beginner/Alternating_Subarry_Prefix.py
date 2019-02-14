t = int(input())

for i in range(t):
    n = input()
    arr = [int(a) for a in input().split()]
    result = [1] * len(arr)
    for j in range(len(arr) - 1, 0, -1):
        if arr[j] > 0:
            if arr[j - 1] < 0:
                result[j - 1] = result[j] + 1
        else:
            if arr[j - 1] > 0:
                result[j - 1] = result[j] + 1

    print(*result)
