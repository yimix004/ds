# Create a functions to create a bank account

def create_account():
    bank_account = []
    input_acount = int(input('Please enter your account account:'))
    print(input_acount)
    for i, input_acount in enumerate(bank_account):
        if input_acount[i] in bank_account:
            print("You have a vaid account\nHow may we help you today?\n1.Deposit Funds\n2.Withdraw Funds")
        else:
            print("You have an invalid account\nWould you like to open an account?\ny/n")
            new_account = input()
            if new_account == 'y' or 'Y':
                from random import randint
                new_account = randint((10**9),(10**9)-1)
                bank_account.append(new_account)
            else:
                print("Aww Ok, Maybe next time?")

Print("Good Try")

