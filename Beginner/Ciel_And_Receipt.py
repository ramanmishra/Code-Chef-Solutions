a = int(input())

for i in range(a):
    b = int(input())
    if b <= 4095:
        print(str(bin(b)).count('1'))
    else:
        c = 0
        while b > 4095:
            c += 1
            b -= 2048
        c += int(str(bin(b)).count('1'))
        print(c)