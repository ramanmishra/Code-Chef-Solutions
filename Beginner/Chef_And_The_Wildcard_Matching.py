t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()

    l = len(s1)
    b = True

    for i in range(l):
        if s1[i] != s2[i] and (s1[i] != '?' and s2[i] != '?'):
            print("No")
            b = False
            break
    if b:
        print("Yes")
