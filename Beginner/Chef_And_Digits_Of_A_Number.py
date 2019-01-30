t = int(input())

for i in range(t):
    n = input()
    ones = n.count('1')
    zeros = n.count('0')

    if (len(n) - ones == 1 or len(n) - zeros) == 1:
        print('Yes')
    else:
        print('No')
