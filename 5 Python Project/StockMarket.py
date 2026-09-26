
import random


wallet =int(input("Enter your initial wallet amount: "))

stocks = {
    "TATA": 100,
    "RELIANCE": 200,
    "HDFC": 300,
    "OLA": 400
}

portfolio = {}

def update_prices():
    for stock in stocks:
         change = random.randint(-20, 20)
         new_price = stocks[stock] + change
         stocks[stock] = max(10, new_price)

while True:
    print()
    print("------- Stock Market ------")
    for name, price in stocks.items():
        print(f"{name} - {price}")
        
    print(f"Your wallet balance: Rs {wallet}")
    print(f"Portfolio: {portfolio if portfolio else 'Empty'}")
    
    
    choice = input("\nBuy - B\nSell - S\nQuit - Q\nEnter your choice: ").lower()
    
    if choice == 'b':
        
        stock = input("Enter the stock name to buy: ").upper()
        if stock not in stocks:
            print("Invalid stock ")
            continue
        
        quantity = int(input("Enter the quantity to buy: "))
        cost = stocks[stock] * quantity
        if cost > wallet:
            max_quantity = wallet // stocks[stock]
            print(f"Not enough funds in wallet. You can buy a maximum of {max_quantity} shares of {stock}.")
        else:
            wallet -= cost
            if stock in portfolio:
                portfolio[stock] += quantity
            else:
                portfolio[stock] = quantity
            print(f"Bought {quantity} shares of {stock} for Rs {cost}.")
            
            
    elif choice == 's':
        
        stock = input("Enter the stock name to sell: ").upper()
        if stock not in portfolio or portfolio[stock] == 0:
            print("You do not own any shares of this stock.")
            continue
        
        quantity = int(input("Enter the quantity to sell: "))
        
        if quantity > portfolio[stock]:
            print(f"You only own {portfolio[stock]} shares of {stock}. Cannot sell {quantity}.")
        else:
            earnings = stocks[stock] * quantity
            wallet += earnings
            portfolio[stock] -= quantity
            if portfolio[stock] == 0:
                del portfolio[stock]
            print(f"Sold {quantity} shares of {stock} for Rs {earnings}.")
    
    
    
    elif choice == 'q':
        print(f"Final wallet balance: Rs {wallet}")
        print(f"Final portfolio: {portfolio if portfolio else 'Empty'}")
        print("Thank you for Trading")
        break
    else:
        print("Invalid choice. Please try again.")
    
    update_prices()