from datetime import datetime

today = datetime.now()
allowedUserCard = ['kelechi', 'precious', 'khokhmah']
allowedPasswords = ['passwordKelechi', 'passwordPrecious', 'passwordKhokhmah']
accountBalance = [5000, 10000, 15000]


cardname = input('Please insert your cardname \n')

if (cardname in allowedUserCard):
    password = input ('Enter your password \n')

    userID = allowedUserCard.index(cardname)

    if (password == allowedPasswords[userID]) :
        print('Welcome to Plucky Bank %s' % cardname.capitalize())
        print('Its %s' % today.strftime("%c"))

        print('What would you like to do')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Complaint')

        optionSelected = int(input('Please select an option \n'))

        #withdrawal
        if (optionSelected == 1) :
            amount = float(input('How much would you like to withdraw?\n'))

            if(amount > accountBalance[userID]):
                print('Transaction Failed! You have insufficient fund.')
            else:
                print('Take your cash')
            accountBalance[userID] -= amount
            print('Your account balance is: \n %s' % accountBalance[userID])
            print('Thank you for choosing Plucky Bank!')

        #deposit
        elif (optionSelected == 2) :
            deposit = float(input('How much would you like to deposit?\n'))
            accountBalance[userID] += deposit
            print('Your account balance is: \n %s' % accountBalance[userID])
            print('Thank you for choosing Plucky Bank!')

        #complaint
        elif (optionSelected == 3):
            print('We are available 24/7 to attend to your complaint')
            feedback =input ('What issue will you like to report?\n')

            print('Received! Thank you for reporting this issue.')

        else:
            print("Invalid option selected, please try again.")

    else:
        print("Password incorrect, input correct password.")

else:
    print("Name not found, input correct name.")