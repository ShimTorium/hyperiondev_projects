# Import libraries if necessary
# ...

# Define functions for various tasks

def login():
    # Prompt the user to enter a username and password
    # Check if the username and password are valid
    # Display appropriate messages for success or failure
    pass

def register():
    # Prompt the user to enter a new username and password
    # Confirm the password
    # Write the new username and password to user.txt
    pass

def add_task():
    # Prompt the user to enter task details (username, title, description, due date)
    # Write the new task to tasks.txt
    pass

def view_all_tasks():
    # Read tasks from tasks.txt and display them in an easy-to-read format
    pass

def view_my_tasks(username):
    # Read tasks from tasks.txt and display only the tasks assigned to the current user
    pass

# Main program loop
while True:
    # Display the menu options
    print("Menu:")
    print("1. Login")
    print("2. Register")
    print("3. Add Task")
    print("4. View All Tasks")
    print("5. View My Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        add_task()
    elif choice == "4":
        view_all_tasks()
    elif choice == "5":
        # Prompt the user for their username
        username = input("Enter your username: ")
        view_my_tasks(username)
    elif choice == "6":
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")
