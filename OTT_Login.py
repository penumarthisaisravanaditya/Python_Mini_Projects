username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))
plan=input("Enter your subscription plan (Basic, Standard, Premium, VIP): ")

if username == "aadi" and password == "aadi123":
    print("Login successful!")
else:
    print("Wrong Credentials! Access Denied.")
    exit()
    
    
if plan not in ["Basic", "Standard", "Premium", "VIP"]:
    print("Invalid subscription plan. Please choose from Basic, Standard, Premium, or VIP.")
    exit()
    
    
if age<13:
    category="Kids"
elif age<18:
    category="Teen"
else:
    category="Adult"

hd = "yes" if plan in["Premium","VIP"] else "no"

match plan:
    case "Basic":
        screens =1
        price=99
    case "Standard":
        screens =2
        price=199
    case "Premium":
        screens =3
        price=299
    case "VIP":
        screens =4
        price=499
        
print(f"Welcome {username}!")
print(f"Plan: {plan.upper()} | {price}/month")
print(f"HD Available: {hd} | Screens: {screens} ")
print(f"Content Category: {category}")