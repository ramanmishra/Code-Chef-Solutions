t = int(input())

for i in range(t):
    length = input()
    n = input()
    if 'I' in n:
        print("INDIAN")
    elif n.count('N') == len(n):
        print("NOT SURE")
    else:
        print("NOT INDIAN")