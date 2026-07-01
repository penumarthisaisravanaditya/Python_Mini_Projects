balance = 1000
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        print("Balance:",balance)
        print("-----------------------")
    elif choice == 2:
        amount =  int(input("Enter deposit amount: "))
        balance +=amount
        print("Amount Deposited Successfully!")
        print("-----------------------")
    elif choice == 3:
        amount =  int(input("Enter Withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn Successfully!")
            print("-----------------------")
        else:
            print("Insufficient Balance!")
            print("-----------------------")
    elif choice == 4:
        print("Thank You!")
        print("-----------------------")
        break
    else:
        print("Invalid Choice!")
        print("-----------------------")