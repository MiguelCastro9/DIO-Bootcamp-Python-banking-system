menu = """
    [1] - REGISTER
    [2] - LIST OF USERS
    [3] - DEPOSIT
    [4] - WITHDRAW
    [5] - EXTRACT
    [6] - EXIT
"""

users_list = []
account_list = []
number_account = 0

def register_user():

    global number_account
    number_account += 1

    cpf = input('Inform your CPF: ')
    cpf = ''.join(filter(str.isdigit, cpf))
    
    for user in users_list:
        if user['CPF'] == cpf:
            print('This CPF already exists!')
            return

    address = {
        'street': input('Inform your street: '),
        'number': input('Inform the number: '),
        'neighborhood': input('Inform the neighborhood: '),
        'city': input('Inform the city: '),
        'state': input('Inform the state abbreviation: ')
    }

    user = {
        'name': input('Inform your name: '),
        'date_of_birth': input('Inform your date of birth: '),
        'CPF': cpf,
        'address': address,
        'agency': '0001',
        'number_account': number_account,
        'balance': 0.0,
        'historic_deposit': [],
        'historic_withdraw': [],
        'limit_withdraw': 3
    }
    for lu in users_list:
        if lu['CPF'] == user['CPF']:
            print('This CPF already exists!')
            return
    users_list.append(user)
    print('User registered successfully!')

def users_registers():
    for lu in users_list:
        print(lu)

def clear():
    for ln in range(1000):
        print()


def check_user_exists(user_cpf):
    user_found = False
    for lu in users_list:
        if lu['CPF'] == user_cpf:
            user_found = True
            break
    if not user_found:
        print('CPF not found. Please, first you need to register the user.')
    return user_found


def deposit():
    user_cpf = input('inform your CPF: ')
    if check_user_exists(user_cpf):
        for lu in users_list:
            if lu['CPF'] == user_cpf:
                value_deposit = input('how much you go deposit: ')
                if float(value_deposit) <= 0:
                    print('please, deposit positives values!')
                else:
                    lu['balance'] += float(value_deposit)
                    lu['historic_deposit'].append(f'- value of ${value_deposit} deposited.')
                    print(f'value of {value_deposit} was deposited with success in your account!')
                    break
    else:
        print('CPF not found. please, first do you need do a register of user.')


def withdraw():
    user_cpf = input('inform your CPF: ')
    if check_user_exists(user_cpf):
        for lu in users_list:
            if lu['CPF'] == user_cpf:
                value_withdraw = input('how much you go withdraw: ')
                if float(value_withdraw) <= 0:
                    print('please, withdraw values positives!')
                elif float(value_withdraw) > lu['balance']:
                    print('insufficient balance.')
                elif lu['limit_withdraw'] == 0:
                    print('daily withdrawal limit reached.')
                elif float(value_withdraw) > 500:
                    print('the limit value withdraw is $500.')
                else:
                    lu['balance'] -= float(value_withdraw)
                    lu['limit_withdraw'] -= 1
                    lu['historic_withdraw'].append(f'- value of ${value_withdraw} drawee.')
                    print(f'value of {value_withdraw} was drawee with success from your account!')
    else:
        print('CPF not found. please, first do you need do a register of user.')


def extract():
    user_cpf = input('inform your CPF: ')
    if check_user_exists(user_cpf):
        for lu in users_list:
            if lu['CPF'] == user_cpf:
                print(' ---------- $$$ EXTRACT $$$ ---------- ')
                if lu['historic_deposit'] == []:
                    print('HISTORIC DEPOSIT: did not have movimentation for deposits.')
                else:
                    print('HISTORIC DEPOSIT:')
                    for d in lu['historic_deposit']:
                        print(d)
                        print('---------------------------------------')
                        if lu['historic_withdraw'] == []:
                            print('HISTORIC WITHDRAW: did not have movimentation for withdraw.')
                        else:
                            print('HISTORIC WITHDRAW:')
                            for w in lu['historic_withdraw']:
                                print(w)
                        print('---------------------------------------')
                        print(f'BALANCE: ${lu['balance']}')
                        print(f'DAILY WITHDRAWAL: {lu['limit_withdraw']}')
                        break
    else:
        print('CPF not found. please, first do you need do a register of user.')


while True:
    option = input(menu)
    if option == '1': 
        clear()
        register_user()
    elif option == '2': 
        clear()
        users_registers()
    elif option == '3': 
        clear()
        deposit()
    elif option == '4':
        clear()
        withdraw()
    elif option == '5':
        clear()
        extract()
    elif option == '6':
        clear()
        print('exited with success, thank you for use our system!')
        break
    else:
        print('please, inform a value valid!')

