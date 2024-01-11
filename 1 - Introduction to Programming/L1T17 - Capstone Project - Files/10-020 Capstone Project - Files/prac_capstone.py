import datetime

# Function to read user credentials from user.txt
def read_user_credentials():
    user_credentials = {}
    with open('user.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split(', ')
            user_credentials[username] = password
    return user_credentials

# Function to write user credentials to user.txt
def write_user_credentials(username, password):
    with open('user.txt', 'a') as file:
        file.write(f"{username}, {password}\n")

# Function to read tasks from tasks.txt
def read_tasks():
    tasks = []
    with open('task2.txt', 'r') as file:
        for line in file:
            task_data = line.strip().split(', ')
            tasks.append(task_data)
    return tasks

# Function to write task to tasks.txt
def write_task(task):
    with open('task2.txt', 'a') as file:
        file.write(', '.join(task) + '\n\n')

# Function to display all tasks
def display_tasks(tasks):
    for task in tasks:
        print("\n".join(task))
        print("-" * 40)
 
# Function to display tasks assigned to a specific user
def display_user_tasks(username, tasks):
    for task in tasks:
        if task[0] == username:
         print("\n".join(task))
         print("-" * 40)

# Function to display statistics
def display_statistics(tasks, user_credentials):
    total_tasks = len(tasks)
    total_users = len(user_credentials)
    print(f"Total tasks: {total_tasks}")
    print(f"Total users: {total_users}")

def main():
    user_credentials = read_user_credentials()
    tasks = read_tasks()


    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in user_credentials and user_credentials[username] == password:
            print("Login successful!")
            if username == 'admin':
                print("Welcome, admin!")
                while True:
                    print("\nMenu:")
                    print("1. Register a user")
                    print("2. Add a task")
                    print("3. View all tasks")
                    print("4. View your tasks")
                    print("5. Display statistics")
                    print("6. Exit")
                    choice = input("Enter your choice: ")

                    if choice == '1' and username == 'admin':
                        new_username = input("Enter new username: ")
                        new_password = input("Enter new password: ")
                        confirm_password = input("Confirm password: ")
                        if new_password == confirm_password:
                            write_user_credentials(new_username, new_password)
                            print("User registered successfully!")
                        else:
                            print("Passwords do not match. User registration failed.")

                    elif choice == '2':
                        assigned_to = input("Enter username of assigned user: ")
                        task_title = input("Enter task title: ")
                        task_description = input("Enter task description: ")
                        due_date = input("Enter due date (YYYY-MM-DD): ")
                        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        new_task = [assigned_to, task_title, task_description, current_date, due_date, 'No']
                        write_task(new_task)
                        print("Task added successfully!")

                    elif choice == '3':
                        display_tasks(tasks)

                    elif choice == '4':
                        display_user_tasks(username, tasks)

                    elif choice == '5':
                        display_statistics(tasks, user_credentials)

                    elif choice == '6':
                        print("Exiting...")
                        break

                    else:
                        print("Invalid choice. Please choose again.")

            else:
                print(f"Welcome, {username}!")
                while True:
                    print("\nMenu:")
                    print("1. Add a task")
                    print("2. View your tasks")
                    print("3. Exit")
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
                        print("Exiting...")
                        break

                    else:
                        print("Invalid choice. Please choose again.")

            break
        else:
            print("Invalid username or password. Please try again.")

main()
