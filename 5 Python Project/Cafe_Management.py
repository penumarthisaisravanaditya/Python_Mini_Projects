menu={
    'pizza': 50,
    'burger': 30,
    'fries': 20,
    'chicken puff': 25
}


    
def order_again():
    order_again = input("Do you want to order anything else? (yes/no)")
    if order_again.lower() == 'yes':
        return True
    else:    
        return False
    
    
def cafe_management():
    
    print("----- Welcome to Our Cafe -----")
    print("Here is our menu:")
    for item, price in menu.items():
        print(f'{item}: {price} Rs')
        
        
    order_total = 0

    while True:
        order_item = input("Enter your item:")
        if order_item in menu:
            order_total += menu[order_item]
            print(f'Your current bill is: {order_total} Rs')
            if not order_again():
                break
            continue
        else:
            print("Sorry, we don't have that item on the menu.")
            if not order_again():
                break
            continue
    print(f'Your final bill is: {order_total} Rs')


   
cafe_management()    
