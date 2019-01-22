t = int(input())

for i in range(t):
    triangle = []
    row = int(input())
    temp_row = row
    for j in range(row):
        temp = input().split()
        into_Int = [int(n) for n in temp]
        triangle += [into_Int]

    lr = len(triangle) - 1

    for row in range(lr, -1, -1):
        for column in range(row, 0, -1):
            diagonal_upper = triangle[row][column] + triangle[row - 1][column - 1]
            upper = triangle[row][column - 1] + triangle[row - 1][column - 1]
            triangle[row - 1][column - 1] = max(diagonal_upper, upper)

    print(triangle[0][0])
