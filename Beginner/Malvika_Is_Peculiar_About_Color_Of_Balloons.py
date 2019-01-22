t = int(input())

for i in range(t):
    s = input()
    count_a = s.count('a')
    count_b = s.count('b')
    print(min(count_a, count_b))