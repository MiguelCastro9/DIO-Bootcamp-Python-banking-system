menu = """
    [1] - DEPOSIT
    [2] - WITHDRAW
    [3] - EXTRACT
    [4] - EXIT
"""

balance = [0]
limit_withdraw = [3]
historic_withdraw = []
historic_deposit = []

def clear():
    for ln in range(1000):
        print()

def deposit(balance):
    value_deposit = input('how much you go deposit: ')
    if float(value_deposit) <= 0:
        print('please, deposit positives values!')
    else:
        balance[0] += float(value_deposit)
        historic_deposit.append(f'- value of ${value_deposit} deposited.')
        print(f'value of {value_deposit} was deposited with success in your account!')

def withdraw(balance, limit_withdraw):
    value_withdraw = input('how much you go withdraw: ')
    if float(value_withdraw) <= 0:
        print('please, withdraw values positives!')
    elif float(value_withdraw) > balance[0]:
        print('insufficient balance.')
    elif limit_withdraw[0] == 0:
        print('daily withdrawal limit reached.')
    elif float(value_withdraw) > 500:
        print('the limit value withdraw is $500.')
    else:
        balance[0] -= float(value_withdraw)
        limit_withdraw[0] -= 1
        historic_withdraw.append(f'- value of ${value_withdraw} drawee.')
        print(f'value of {value_withdraw} was drawee with success from your account!')

def extract():
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
        print(f'BALANCE: ${balance[0]}')
        print(f'DAILY WITHDRAWAL: {limit_withdraw}')

while True:
    option = input(menu)
    if option == '1': 
        clear()
        deposit(balance)
    elif option == '2':
        clear()
        withdraw(balance, limit_withdraw)
    elif option == '3':
        clear()
        extract()
    elif option == '4':
        clear()
        print('exited with success, thank you for use our system!')
        break
    else:
        print('please, inform a value valid!')

