try:
    withdraw_amount, initial_back_balance = input().split()
    withdraw_amount, initial_back_balance = float(withdraw_amount), float(initial_back_balance)

    current_back_balance = 0

    # if thw withdraw_amount is multiple of 5 as well as the withdraw_amount is less than initial back balance
    # Then only we can do a transaction with the back fee 0.50

    if withdraw_amount % 5 == 0 and withdraw_amount + 0.50 <= initial_back_balance:
        current_back_balance = initial_back_balance - (withdraw_amount + 0.50)
    else:
        current_back_balance = initial_back_balance

    # To format out output for 2 decimal place

    print("{0:.2f}".format(current_back_balance))

except Exception as e:
    print(e)
