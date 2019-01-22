t = int(input())

for i in range(t):
    n_student = int(input())
    time_so_far = 0
    student = 0
    time_allowed = list(map(int, input().split()))
    time_required = list(map(int, input().split()))
    for time in range(len(time_allowed)):
        if time_allowed[time] - time_so_far >= time_required[time]:
            student += 1
        time_so_far = time_allowed[time]
    print(student)