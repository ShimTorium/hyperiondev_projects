# Datetime is imported to create date user functionality in the task manager.
import datetime

# define function to read the user credentials in the user text file.
# Use a with  block to open the text file.
# Use a for loop and return the users credentials.
def read_user_credentials():
    user_credentials = {}
    with open('user.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split(', ')
            user_credentials[username] = password
    return user_credentials

# Define function to write user credentials to the user text file.
# Use with block to open the text file.
def write_user_credentials(username, password):
    with open('user.txt', 'a') as file:
        file.write(f"{username}, {password}\n")

# Define function to read the users task in the task text file.
# Use with block to open the text file.
# Use for loop and then return the task.
def read_tasks():
    tasks = []
    with open('tasks.txt', 'r') as file:
        for line in file:
            task_data = line.strip().split(', ')
            tasks.append(task_data)
    return tasks

# Define function to write to the task text file.
# Use with block with 'a' to append the text file. 
def write_task(task):
    with open('tasks.txt', 'a') as file:
        file.write(', '.join(task) + '\n')
        
# Define function to display the task.
def display_tasks(tasks):
    for task in tasks:
        print('\n'.join(task).strip())
        print("_" * 40)

# Function to display tasks assigned to a specific user69
def display_user_tasks(username, tasks):
    for task in tasks:
        if task[0] == username:
         print('\n'.join(task).strip())
         print("_" * 40) 

# Define function to display statistics.
def display_statistics(tasks, user_credentials):
    total_tasks = len(tasks)
    total_users = len(user_credentials)
    print(f"Total tasks: {total_tasks}")
    print(f"Total users: {total_users}")

# Define function used to ensure the main function is executed.
def main():
    user_credentials = read_user_credentials()
    tasks = read_tasks()

    # Use while true loop to present a menu to the user.
    # First ask the user to login.
    while True:
        print("Log into Task Manager")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Use if statement to send message of successfull login if user credentials are met.
        if username in user_credentials and user_credentials[username] == password:
            print("Login successful!")
            if username == 'admin':
                print("Welcome, admin!")

                # Use while loop present the menu to the user.   
                # Use functions to track user credentials and user task within the program 
                while True:
                    user_credentials = read_user_credentials()
                    tasks = read_tasks()
                    print("\nMenu:")
                    print("1. Register a user")
                    print("2. Add a task")
                    print("3. View all tasks")
                    print("4. View your tasks")
                    print("5. Display statistics")
                    print("6. Exit")
                    choice = input("Enter your choice: ")

                    # Use if statement to allow admin to register new users and passwords.
                    if choice == '1' and username == 'admin':
                        new_username = input("Enter new username: ")
                        new_password = input("Enter new password: ")
                        confirm_password = input("Confirm password: ")
                        if new_password == confirm_password:
                            write_user_credentials(new_username, new_password)
                            print("User registered successfully!")
                        else:
                            print("Passwords do not match. User registration failed.")

                    # Use else if statement to assign tasks and task descriptions to users.
                    elif choice == '2':
                        assigned_to = input("Enter username of assigned user: ")
                        task_title = input("Enter task title: ")
                        task_description = input("Enter task description: ")
                        due_date = input("Enter due date (YYYY-MM-DD): ")
                        current_date = datetime.datetime.now().strftime('%Y-%m-%d') # Used string format time formular to format the datetime
                        new_task = [assigned_to, task_title, task_description, current_date, due_date, 'No']
                        write_task(new_task)
                        print("Task added successfully!")

                    # Used else if statement to display users task if user choice if == to 3
                    elif choice == '3':
                        display_tasks(tasks)

                    # Used else if statement to view admins specific task if user choice is == to 4
                    elif choice == '4':
                        display_user_tasks(username, tasks)

                    # Used else if statement to display how many users ther are and hows many task there are is user choice is == to 5 
                    elif choice == '5':
                        display_statistics(tasks, user_credentials)
 
                    # Used else if statement to to exit the loop with a break if user is done and if user choice is == to 6
                    elif choice == '6':
                        print("Exiting...Goodbye!")
                        break
                         
                    # Use else statement to let user know if invalid choice has been made
                    else:
                        print("Invalid choice. Please choose again.")
            
            # Use else statement to welcome admin.
            # Use while loop to allow admin to only add task for users.
            # Use functions to track user credentials and user task.
            else:
                print(f"Welcome, {username}!")
                while True:
                    user_credentials = read_user_credentials()
                    tasks = read_tasks()
                    print("\nMenu:")
                    print("1. Add a task")
                    print("2. View your tasks")
                    print("3. View all tasks")
                    print("4. Exit")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        task_title = input("Enter task title: ")
                        task_description = input("Enter task description: ")
                        due_date = input("Enter due date (YYYY-MM-DD): ")
                        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        new_task = [username, task_title, task_description, current_date, due_date, 'No']
                        write_task(new_task)
                        print("Task added successfully!")

                    elif choice == '2':
                        display_user_tasks(username, tasks)

                    elif choice == '3':
                        display_tasks(tasks)
                        
                    elif choice == '4':
                        print("Exiting...Goodbye!")
                        break

                    else:
                        print("Invalid choice. Please choose again.")
           
            #  Use break statement to exit the while loop
            break
        # Use else statement to let user know that either incorrect username or password is used and that they should try again till correct credentials are validated.
        else:
            print("Invalid username or password. Please try again.")
main()



