t = int(input())

for i in range(t):
    print(int(input()[::-1]))

    # Following is the alternate solution to reversing the number

    # ans = []
    # while n != 0:
    #     ans += [n % 10]
    #     n = n // 10
    #
    # print(int("".join(str(digit) for digit in ans)))
