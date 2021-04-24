from datetime import datetime
import random

database = {}

today = datetime.now()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def intro():
    print("Welcome to Plucky Bank")
    print('It is %s' % today.strftime("%c"))

    have_account = int(input("Press 1 if you have a Plucky account\nPress 2 to register \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        intro()


def login():
    print('==* Account Login *==\n')

    account_number_from_user = int(input('Input your registered account number: \n'))
    password = input('Input your password: \n')

    for account_number, user_details in database.items():
        if account_number == account_number_from_user:
            if user_details[3] == password:
                bank_operation(user_details[0])

            else:
                print('\nInvalid password')
                login()
        else:
            print('\nInvalid account')
            login()


def register():
    print('\n== === * Account Registration * === ==\n')
    first_name = input('Your first name is?: \n')
    if first_name == '':
        print('Please input a valid name')
        register()

    elif len(first_name) < 3:
        print('Name should be more than 3 letters, try again.')
        register()

    else:
        last_name = input('Your last name is?: \n')
        if last_name == '':
            print('Please input a valid name')
            register()

        if len(last_name) < 3:
            print('Name should be more than three letters, try again.')
            register()

        else:
            email = input('Input your e-mail address: \n')
            if email == '':
                print('Please input a valid email')
                register()

            if len(email) < 6:
                print('Your email should be more than 6 letters, try again.')
                register()

            else:
                password = input('Input your password: \n')
                if password == '':
                    print('Please input a valid password')

                if len(str(password)) < 4:
                    print('Your password should be more than four characters, numbers, and symbols, try again.')

                else:
                    account_number = generate_account_number()
                    print(f'== --- Yippee! Your account is created on {today} --- ==\n')
                    print(' == Your account number is *%d*** ==\n' % account_number)
                    print(' -- Keep your details safe and beware of scammers. --\n')
                    database[account_number] = [first_name, last_name, email, password]
                    login()


def bank_operation(user):
    print(f'=== == Welcome %s , You logged in on the {today} == ===\n' % user)
    selected_option = int(input(
        '=== == What would you like to do? == ===\n(1) Withdrawal\n(2) Deposit\n'
        '(3) Complaint\n(4) Logout\n(5) Exit\n'))
    if selected_option == 1:
        withdrawal()
    elif selected_option == 2:
        deposit()
    elif selected_option == 3:
        complaint()
    elif selected_option == 4:
        logout()
    elif selected_option == 5:
        exit()
    else:
        print('Invalid option')
        bank_operation(user)
        


def withdrawal():
    money = input('How much would you like to withdraw: \n')
    print('Take your cash: \n %s' % money)
    print('Thank you for choosing Plucky Bank!')
    done()


def deposit():
    user_deposit = input('How much would you like to deposit: \n')
    print('Successful! Your account balance is: \n %s' % user_deposit)
    print('Thank you for choosing Plucky Bank!')
    done()


def complaint():
    print('We are available 24/7 to attend to your complaint')
    input('What issue will you like to report?\n')

    print('Received! Thank you for reporting this issue.')
    done()


def done():
    print('\n Would you love to do anything else or logout?\n')
    choose = int(input('Press 1 to continue\nPress 2 to logout\n'))
    if choose == 1:
        do = int(input(
            'What would you like to continue with?\n(1) Withdrawal\n(2) Deposit\n(3) Complaint\n'))
        if do == 1:
            withdrawal()
        elif do == 2:
            deposit()
        elif do == 3:
            complaint()
        else:
            print('Invalid option')

    elif 2 == choose:
        print('Bye for now!')
        logout()
    else:
        print('Invalid input')


def logout():
    login()


intro()

