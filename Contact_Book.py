print("*" * 30)
print("Contact Book")
print("*" * 30)

contact_book = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact phone number: ")
        contact_book[name] = number
        print(f"\nContact '{name}' added successfully!")
    elif choice == "2":
        if len(contact_book) == 0:
            print("\nNo contacts available.")
        else:
            print("\nContacts:")
            for name, number in contact_book.items():
                print(f"Name: {name}, Phone Number: {number}")
                
    elif choice == "3":
        search_name = input("Enter contact name to search: ")
        found = False
        for name, number in contact_book.items():
            if name.lower() == search_name.lower():
                found = True
                print(f"\nContact found: Name: {name}, Phone Number: {contact_book[name]}")
                break
        if not found:
            print("\nContact not found !!")
            
    elif choice == "4":
        delete_name = input("Enter contact name to delete: ")
        if delete_name in contact_book:
            del contact_book[delete_name]
            print(f"\nContact '{delete_name}' deleted successfully!")
        else:
            print("\nContact not found !!")
            
    elif choice == "5":
        print("\nThank you for using the Contact Book!")
        break