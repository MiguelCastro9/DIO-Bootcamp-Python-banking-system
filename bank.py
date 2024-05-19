menu = """
    [1] - DEPOSIT
    [2] - WITHDRAW
    [3] - EXTRACT
    [4] - EXIT
"""

LINES = 1000
balance = 0
limit_withdraw = 3
historic_withdraw = []
historic_deposit = []

while True:
    
    option = input(menu)

    if option == '1': 
        for ln in range(LINES):
            print()
        value_deposit = input('how much you go deposit: ')
        if float(value_deposit) <= 0:
            print('please, deposit positives values!')
        else:
            balance += float(value_deposit)
            historic_deposit.append(f'- value of ${value_deposit} deposited.')
            print(f'value of {value_deposit} was deposited with success in your account!')

    elif option == '2':
        for ln in range(LINES):
            print()
        value_withdraw = input('how much you go withdraw: ')
        if float(value_withdraw) <= 0:
            print('please, withdraw values positives!')
        elif float(value_withdraw) > balance:
            print('insufficient balance.')
        elif limit_withdraw == 0:
            print('daily withdrawal limit reached.')
        elif float(value_withdraw) > 500:
            print('the limit value withdraw is $500.')
        else:
            balance -= float(value_withdraw)
            limit_withdraw -= 1
            historic_withdraw.append(f'- value of ${value_withdraw} drawee.')
            print(f'value of {value_withdraw} was drawee with success from your account!')

    elif option == '3':
        for ln in range(LINES):
            print()
        print(' ---------- $$$ EXTRACT $$$ ---------- ')
        if len(historic_deposit) == 0:
            print('HISTORIC DEPOSIT: did not have movimentation for deposits.')
        else:
            print('HISTORIC DEPOSIT:')
            for d in historic_deposit:
                print(d)
        print('---------------------------------------')
        if len(historic_withdraw) == 0:
            print('HISTORIC WITHDRAW: did not have movimentation for withdraw.')
        else:
            print('HISTORIC WITHDRAW:')
            for h in historic_withdraw:
                print(h)
        print('---------------------------------------')
        print(f'BALANCE: ${balance}')
        print(f'DAILY WITHDRAWAL: {limit_withdraw}')
    elif option == '4':
        for ln in range(LINES):
            print()
        print('exited with success, thank you for use our system!')

        break
    else:
        print('please, inform a value valid!')

