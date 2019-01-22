def merge_sort(input_array):
    mid = len(input_array) // 2

    if len(input_array) > 1:
        left = input_array[:mid]
        right = input_array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                input_array[k] = left[i]
                i += 1
            else:
                input_array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            input_array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            input_array[k] = right[j]
            j += 1
            k += 1

    return input_array


number_of_test_cases = int(input())

numbers = []
for n in range(number_of_test_cases):
    numbers += [int(input())]

sorted_array = merge_sort(numbers)
for elem in sorted_array:
    print(elem)
