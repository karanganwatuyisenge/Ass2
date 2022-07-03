print("Automatic Teller Machine(ATM")
print("--------------------------")
pin=int(input("create pin :"))
user={'pin':pin,'balance':0}

#This function used to deposit cash
def deposit():
    while True:
        amount=int(input("Enter the amount of money you want to deposit:"))
        if amount>0:
            user['balance']=user['balance']+amount
            print(f"{amount}successfully deposited your new balance is{user['balance']}")
            print("")
            return False
#Used in withdrawing money
def withdraw():
    amount=int(input("Enter the amount of money you want to withdraw:"))
    if amount >user['balance']:  #if amount of money withdrawn is greater than balance it display below message
        print("you don't have sufficient balance to make this witdrawal")

    #else display this message
    else:
        user['balance']=user['balance']-amount
        print(f"{amount} successfully withdrawn your remaining balance is{user['balance']}")
        print("")

#Display a total balance on your account
def current_balance():
    print(f"Total balance {user['balance']}")
    print("")

is_quit=False
print("")

pin=int(input('Please enter your pin:'))

print("---------------------------------")

#Enter your pin and choose an option according to what you want to perform
if pin==user['pin']:
    while is_quit==False:
        print("what do you want to do?")
        print("Enter 1 to depositcash\n Enter 2 to withdraw cash \n Enter 3 for balance Enquiry \n enter 4 to Quit")

        query=int(input("Enter the number corresponding to the activity you want to do:"))
        print("---------------------------------------------")

        if query==1:
            deposit()
        elif query==2:
            withdraw()
        elif query==3:
            current_balance()

        elif query==4:
            is_quity=True

        else:
            print("Please enter a correct value shown")
else:
    print("you entered wrong pin")

