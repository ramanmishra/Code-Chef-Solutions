number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    num_a, num_b = map(int, input().split())

    print(num_a - num_b * (num_a // num_b))

