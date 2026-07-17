print("Welcome to the Currency Calculator!")
print("-" * 30)
usd_rate = 96.36  # Example conversion rate from USD to INR
while True:
    print("\n 1.USD to INR")
    print("\n 2.INR to USD")
    print("\n 3.Exit")
    
    choice = input("\nEnter your choice : ")
    if choice == "3":
        print("Thank you for using the Currency Calculator!")
        break
    amount = float(input("Enter the amount: "))
    if choice == "1":
        result = amount * usd_rate
        print(f"$ {amount} is equal to \u20B9 {result:.2f}")
    elif choice == "2":
        result = amount / usd_rate
        print(f"\u20B9 {amount} is equal to ${result:.2f}")
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
