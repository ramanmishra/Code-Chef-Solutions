t = int(input())

for i in range(t):
    n = input()
    d = [int(temp) for temp in input().split()]
    print(len(set(d)))
