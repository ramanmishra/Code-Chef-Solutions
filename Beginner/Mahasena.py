t = int(input())

n_list = list(map(int, (input().split())))
ls = 0
us = 0
for n in n_list:
    if n % 2 == 0:
        ls += 1
    else:
        us += 1
if ls > us:
    print("READY FOR BATTLE")
else:
    print("NOT READY")