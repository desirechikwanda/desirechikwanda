import os
import time


running = True

while running:
    balance = 0
    print('Welcome to Mpamba')
    print("""
1.Register
2.Deposit
3.Withdraw
4.Send Money

""")
    print('Hit "m" to view all accounts registered and 5 to log into you account')

    option = input('Select option:')
    if option == '1':
        print('Register')
        print()
        name = input('Enter Name:')
        all_accounts = os.listdir()
        if name  in all_accounts:
            print('You are already Registered!')
        else:
            number = input('Phone Number')
            with open (name, 'w') as f:
                f.write(name+ '\n')
                f.write(number+ '\n')
                print('Registration is successful! Welcome',name ,'our new member')
        

    elif option == '2':
        print('Deposit')
        name = input('Enter name:')
        with open(name, 'r+') as f:
            file_data = f.read()
            file_data = file_data.split('\n')
            name = file_data[0]
            numbere = file_data[1]

            all_accounts = os.listdir()
            if name not in all_accounts:
                print('Sorry You are not Registered')
            else:
                print('Welcome', name)
                print()
                number = input('Number:')
                if number == numbere:
                    amount = input('Enter amount' )
                    balance = balance + int(amount)
                    with open(name, 'w') as f:
                        f.write(name+ '\n')
                        f.write(number+ '\n')
                        f.write(str(balance)+ '\n')
                        
                        print('Deposit is successful and amount is ', balance,'on', time.asctime())
                else:
                    print('Enter a correct number for your account')

    elif option == '3':
        print('Withdraw')
        print()
        print('Select your account!')
        name = input('Enter Name:')
        all_accounts = os.listdir()
        with open(name, 'r+') as f:
            file_data = f.read()
            file_data = file_data.split('\n')
            lname = file_data[0]
            if name == lname:
                print('Print Welcome ', lname)
                print()
                print('Enter amount to withdraw')
                amount = input('Enter amount:')
                if int(amount) > balance:
                    print('Insuffient Balance')
                else:
                    balance = balance - int(amount)
                    f.write(str(balance)+ '\n')
                    print('Withdraw is sucessful and balance is', balance)
                    running = False       
           
            else:
                all_accounts = os.listdir()
                if name not in all_accounts:
                    print('File Not known')

    elif option == 'm':
        all_accounts = os.listdir()
        if all_accounts == '':
            print('No one has Registered')
        else:
            print(all_accounts)

    elif option == '4':
        all_acounts = os.listdir()
        print('First Login!')
        name = input('Enter Name:')
        with open(name, 'r') as f:
            file = f.read()
            file = file.split('\n')
            logname = file[0]
            if logname == name:
                print('Welcome', name)
                print("""
1.Tnm
2.Airtel
""")

                net = input('Select your option:')
                if net == '1':
                    print('Send money to Tnm')
                    tnm = input('Enter Number:')
                    if (tnm.startswith('088')):
                        amount = input('Enter amount:')
                        amount = amount
                        print('You have requested to Send MWK', amount, 'to ', tnm)
                        print("""
1.Yes
2.No
""")
                        option = input('Option:')
                        if option == '1':
                            print('Money successfully sent to', tnm, 'Amount= MWK', amount)
                            running = False
                        else:
                            print('Sorry Try again')
                            running = False
                    else:
                        print('Please Enter a Tnm number')
                        running = False
            
            else:
                if lname !=name:
                    print('You are not registered! First Sing Up!')


            
            if net == '2':
                print('Send to Airtel Number!')
                number = input('Enter Number')
                if (number.startswith('09' or '099')):
                    print('How much do you want to send?')
                    amount  = input('Enter amount:')
                    amount = amount
                    print('Requesting to send MWK', amount,'to', number)
                    print("""
1.Yes
2.No
""")
                    option = input('Enter option :')
                    if option == '1':
                        print('You have succesfully sent MWK', amount, 'to', number)
                        running = False
                    else:
                        print('Transaction Failed! Please Try Agian')
                        running = False
                else:
                    print('Enter Airtel Number!')
                    running = False
    if option == '5':
        print('Login')
        name = input('Enter Name:')
        with open(name, 'r') as f:
            file = f.read()
            name = file[0]
            balance = file[1]
            phone = file[2]
            file = file.split('\n')

            if name == name:
                for info in file:
                    print(info)
            else:
                all_accounts = os.listdir()
                if name not in all_accounts:
                    print('You are not registered')

