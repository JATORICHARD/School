def show_balance(balance):
    print(f"your balance is ${balance: .2f}")

def deposit():
    amount=float(input("Enter an amount to be deposited: "))
    if amount<0:
        print("That is not a valid amount")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount=float(input("Enter an amount to be withdrawn: "))
    
    if amount>balance:
        print("Insufficient funds")
        return 0
    elif amount<0:
        print("the amount must be greater than 0")
        return 0
    else:
        return amount

    
def main():
    
    
    balance=0
    is_running=True
    
    while is_running:
        print("********************")
        
        print("  Banking program  ")
        print("********************")

        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. Exit")
        print("********************")

        choice=input("Enter your choice(1-4): ")
        if choice =='1':
            show_balance(balance)
            print("********************")
        elif choice=="2":
            balance=deposit()
            print("********************")
        elif choice=="3":
            balance -=withdraw(balance)
            print("********************")
        elif choice=="4":
            is_running=False
        else:
            print("********************")
            print("That is not a valid choice")
            print("********************")
    print("Thank you! Have a niceday!!!")
    print("********************")
if __name__=='__main__':
    main()
