import math


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


try:
    t = int(input())
    for i in range(t):
        n = int(input())
        if is_prime(n):
            print("yes")
        else:
            print("no")
except Exception as e:
    print(e)
