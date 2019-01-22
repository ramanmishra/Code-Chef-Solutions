import math

a = int(input())

for i in range(a):
    b = int(input())
    print(math.floor(math.sqrt(b)))

    # another way to find square root without using any library function
    # print(int(b**0.5 * 10 // 10))
