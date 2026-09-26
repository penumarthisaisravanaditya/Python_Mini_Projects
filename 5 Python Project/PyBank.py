balance = 0.0
transactions = []


def deposit(amount):
    global balance

    balance += amount
    transactions.append(f"Deposited: Rs {amount}")
    print(f"Successfully deposited Rs {amount}\n")


def withdraw(amount):
    global balance

    if balance < amount:
        print("Insufficient balance. Cannot withdraw.\n")
    else:
        balance -= amount
        transactions.append(f"Withdrew: Rs {amount}")
        print(f"Successfully withdrew Rs {amount}\n")


def check_balance():
    print(f"Current balance: Rs {balance}\n")


def view_transactions():
    if not transactions:
        print("No transactions yet.\n")
    else:
        print("Transaction History:")

        for transaction in transactions:
            print("-", transaction)

        deposits = sum(
            1 for transaction in transactions
            if "Deposited" in transaction
        )

        withdrawals = sum(
            1 for transaction in transactions
            if "Withdrew" in transaction
        )

        print(f"\nTotal deposits: {deposits}")
        print(f"Total withdrawals: {withdrawals}\n")


def menu():
    while True:
        print("------- Welcome to PyBank! -------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions History")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            deposit(amount)

        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            withdraw(amount)

        elif choice == '3':
            check_balance()

        elif choice == '4':
            view_transactions()

        elif choice == '5':
            print("Thank you for using PyBank. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


menu()