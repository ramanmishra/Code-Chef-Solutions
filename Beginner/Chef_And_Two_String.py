t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()

    l = len(s1)
    maxDiff = 0
    minDiff = 0

    for i in range(l):
        if s1[i] != s2[i] and (s1[i] != '?' and s2[i] != '?'):
            minDiff += 1
            maxDiff += 1
        if s1[i] == '?' or s2[i] == '?':
            maxDiff += 1

    print(minDiff, maxDiff)
