tasks=[]
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        user_task = input("Enter the task you want to add: ")
        tasks.append(user_task)
        print("\nTask added successfully!")
        
    elif choice == "2":
        if len(tasks)==0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choice == "3":
        if len(tasks)==0:
            print("\nNo tasks available to delete.")
        else:
            del_task = input("Enter the task you want to delete: ")
            if del_task in tasks:
                tasks.remove(del_task)
                print("\nTask deleted successfully!")
            else:
                print("\nTask not found in the list.")
                
    elif choice == "4":
        print("\nThank you for using the To-Do List!")
        break