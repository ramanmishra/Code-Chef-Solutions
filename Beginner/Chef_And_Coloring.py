t = int(input())

for i in range(t):
    n = input()
    s = input()
    sorted_count = sorted([s.count('R'), s.count('G'), s.count('B')])
    print(sorted_count[0] + sorted_count[1])
