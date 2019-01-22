t = int(input())

for i in range(t):
    b_array = [False] * 101
    m, x, y = map(int, input().split())
    m_arr = list(map(int, input().split()))
    distance = x * y
    for houseWithCops in range(len(m_arr)):
        lower_limit = m_arr[houseWithCops] - distance
        upper_limit = m_arr[houseWithCops] + distance
        if lower_limit <= 1:
            lower_limit = 1
        if upper_limit > 100:
            upper_limit = 100

        b_array[lower_limit] = True
        b_array[upper_limit] = True
        for j in range(lower_limit, upper_limit):
            b_array[j] = True
    print(b_array[1:].count(False))
