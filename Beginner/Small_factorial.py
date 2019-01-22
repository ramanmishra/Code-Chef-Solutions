number_of_test_cases = int(input())


def fact(n, answer_array):
    temp = 0
    j = 0
    while answer_array[j] is not None:
        intermidiate_answer = answer_array[j] * n + temp
        answer_array[j] = intermidiate_answer % 10
        temp = intermidiate_answer // 10
        j += 1

    while temp != 0:
        answer_array[j] = temp % 10
        temp //= 10
        j+=1

    return (answer_array, j)


for i in range(number_of_test_cases):
    answer_array = [None] * 200
    answer_array[0] = 1
    number_of_element = 1
    number = int(input())
    for n in range(1, number + 1):
        answer, number_of_element = fact(n, answer_array)

    answer = answer_array[:number_of_element]
    print(''.join(str(elem) for elem in answer)[::-1])
