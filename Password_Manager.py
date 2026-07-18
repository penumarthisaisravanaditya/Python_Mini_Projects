def add_pass():
    with open("passwords.txt", "a") as file:
        website = input("Enter the website name:")
        password = input("Enter the password:") 
        file.write(f"{website}: {password}\n")
    print("Password added successfully!")
    
def search_pass():
    try:
        with open("passwords.txt", "r") as file:
            data = file.readlines()
        website = input("Enter the website name to search:")
        found = False
        
        for line in data:
            if line.startswith(f"{website}:"):
                print("\nFound")
                print(line.strip())
                found = True
                break
        if not found:
            print("Password not found for the specified website !")
    except FileNotFoundError:
        print("No passwords saved yet. Please add a password first.")
    print()
    
def view_all():
    try:
        with open("passwords.txt", "r") as file:
            data = file.readlines()
        if not data:
            print("No passwords saved yet. Please add a password first.")
        else:
            print("\n==== SAVED PASSWORDS ====")
            for line in data:
                print(line.strip())
    except FileNotFoundError:
        print("No passwords saved yet. Please add a password first.")
    print()
    
def delete_pass():
    try:
        with open("passwords.txt", "r") as file:
            data = file.readlines()
        website = input("Enter the website name to delete:")
        found = False
        
        for line in data:
            if line.startswith(f"{website}:"):
                data.remove(line)
                found = True
                break
        if found:
            with open("passwords.txt", "w") as file:
                file.writelines(data)
            print("Password deleted successfully!")
        else:
            print("Password not found for the specified website!")
    except FileNotFoundError:
        print("No passwords saved yet. Please add a password first.")

def update_pass():
    try:
        with open("passwords.txt", "r") as file:
            data = file.readlines()
        website = input("Enter the website name to update:")
        new_password = input("Enter the new password:")
        found = False
        
        for i in range(len(data)):
            if data[i].startswith(f"{website}:"):
                data[i] = f"{website}: {new_password}\n"
                found = True
                break
            if found:
                with open("passwords.txt", "w") as file:
                    file.writelines(data)
                print("Password updated successfully!")
            else:
                print("Password not found for the specified website!")
    except FileNotFoundError:
        print("No passwords saved yet. Please add a password first.")
    print()
    
def main():
    while True:
        print("==== PASSWORD MANAGER ====")
        print("1. Add Password")
        print("2. Search Password")
        print("3. View All Passwords")
        print("4. Delete Password")
        print("5. Update Password")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_pass()
        elif choice == "2":
            search_pass()
        elif choice == "3":
            view_all()
        elif choice == "4":
            delete_pass()
        elif choice == "5":
            update_pass()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.\n")
            
main()
