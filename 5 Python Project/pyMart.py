products = {
    1: {"name": "Apple", "price": 50},
    2: {"name": "Banana", "price": 20},
    3: {"name": "Orange", "price": 30},
    4: {"name": "Grapes", "price": 40},
    5: {"name": "Mango", "price": 60}
}

cart = {}

def show_products():
    print("----- Available Products -----")
    for pid, details in products.items():
        print(f"{pid}. {details['name']} - Rs {details['price']}")
    
def view_cart():
    print("----- Your Cart -----")
    if not cart:
        print("Your cart is empty.\n")
    else:
        total = 0
        
        for pid, item in cart.items():
            name = item['name']
            price = item['price']
            quantity = item['quantity']
            sub_total = price * quantity
            total += sub_total
            print(f"{pid} | {name} (X{quantity}) - Rs {sub_total}")
        print(f"Total: Rs {total}\n")

def add_to_cart():
    
    show_products()
    
    try:
        pid=int(input("Enter the product ID to add to cart: "))
        if pid in products:
            quantity = int(input("Enter quantity: "))
            if pid in cart:
                cart[pid]['quantity'] += quantity
            else:
                cart[pid] = {
                    "name": products[pid]['name'],
                    "price": products[pid]['price'],
                    "quantity": quantity
                }
            print(f"{quantity} X {products[pid]['name']} added to cart.\n")
        else:
            print("Invalid product ID. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a valid product ID.\n")
       
def remove_from_cart():
    view_cart()
    if not cart:
        return
        
    try:
        pid = int(input("Enter the product ID to remove from cart: "))
        if pid in cart:
            quantity = int(input("Enter quantity to remove: "))
            current_quantity = cart[pid]['quantity']
            
            if quantity == current_quantity:
                del cart[pid]
                print(f"{products[pid]['name']} removed from cart.\n")
            elif quantity < current_quantity:
                cart[pid]['quantity'] -= quantity
                print(f"{quantity} X {products[pid]['name']} removed from cart.\n")
            else:
                print(f"You only have {current_quantity} X {products[pid]['name']} in your cart. Cannot remove {quantity}.\n")
        else:
            print("Product not found in cart. Please try again.")
            
    except ValueError:
            print("Invalid input. Please enter a valid product ID.\n")
        
def checkout():
    view_cart()
    
    if cart:
        confirm = input("Do you want to proceed to checkout? (yes/no): ")
        
        if confirm.lower() == 'yes':
            print("Checkout successful! Thank you for shopping with PyMart.\n")
        else:
            print("Checkout cancelled. You can continue shopping.\n")


def menu():
    while True:
        print("----- Welcome to PyMart-Mini Shopping Cart -----")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            show_products()
            
        elif choice == '2':
            add_to_cart()
            
        elif choice == '3':
            remove_from_cart()
            
        elif choice == '4':
            view_cart()
            
        elif choice == '5':
            checkout()
            
        elif choice == '6':
            print("Thank you for shopping with PyMart. Goodbye!\n")
            break
        
        else:
            print("Invalid choice. Please select 1-6.\n")

menu()