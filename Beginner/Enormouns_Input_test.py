number_of_input, divisor = input().split()

number_of_input, divisor = int(number_of_input), int(divisor)

number_divisable_by_divisor = 0

for i in range(number_of_input):
    number = int(input())
    if number % divisor ==0:
        number_divisable_by_divisor+=1

print(number_divisable_by_divisor)