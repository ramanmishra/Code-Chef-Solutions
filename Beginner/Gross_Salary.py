t = int(input())

for i in range(t):
    gross_salary = 0
    n = int(input())
    if n < 1500:
        hra = n * 0.1
        da = n * 0.9
        gross_salary = n + hra + da
    else:
        hra = 500
        da = n * 0.98
        gross_salary = n + hra + da

    print(gross_salary)