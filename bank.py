menu = """
    [1] - DEPOSIT
    [2] - WITHDRAW
    [3] - EXTRACT
    [4] - EXIT
"""

balance = 0


while True:

    option = input(menu)


    if option == '1':
        value_deposit = input('how much you go deposit: ')
        if int(value_deposit) <= 0:
            print('please, deposit positives values!')
        else:
            balance += int(value_deposit)
            print(f'value of {value_deposit} was deposited with success in your account!')

    elif option == '2':
        print('withdraw...')


    elif option == '3':
        print('$$$ ---------- EXTRACT ---------- $$$')
        print(f'BALANCE: {balance}')

    elif option == '4':
        print('exited with success, thank you for use our system!')


        break
    else:
        print('please, inform a value valid!')