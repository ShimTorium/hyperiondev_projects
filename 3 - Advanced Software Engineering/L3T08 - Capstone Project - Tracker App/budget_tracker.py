import sqlite3

# Create a connection to the database.
# Get the cursor object.
db = sqlite3.connect("budget_tracker.db")
cursor = db.cursor()
cursor.execute("PRAGMA table_info(expenses)")
columns = cursor.fetchall()
budget_column_exists = any(column[1] == 'budget' for column in columns)


# Create a table called expenses.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL
        budget REAL)
''')

# Create a table called incomes.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS incomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL)
''')

# Create goals table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        target_amount REAL,
        current_amount REAL
    )
''')

# Create function for expense category and amounts to be added.
# Use try block to handle errors.
# Create empty list to hold the categories and amounts.
def add_expense_category():
    try:
        categories_and_amounts = []  

        # Create while loop
        # Get user input for categories and amounts
        while True:
            category = input("Enter expense category (or type 'done' to finish): ")
            if category.lower() == 'done':
                break

            amount = float(input(f"Enter amount for '{category}': "))
            categories_and_amounts.append((category, amount))

        # Insert categories and amounts into the database
        for category, amount in categories_and_amounts:
            cursor.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (category, amount))

        db.commit()
        print("Expense categories added successfully.")
    except sqlite3.Error as e:
        db.rollback()  # Rollback changes if an error occurs
        print(f"Error adding expense categories: {e}")


# Create function to update the expense category.
def update_expense_category():
    try:
        category = input("Enter the expense category you want to update: ")
        new_amount = float(input(f"Enter the new amount for '{category}': "))
        cursor.execute("UPDATE expenses SET amount = ? WHERE category = ?", (new_amount, category))
        db.commit()
        print(f"Expense category '{category}' updated successfully.")
    except sqlite3.Error as e:
        db.rollback()
        print(f"Error updating expense category: {e}")


# Create function to delete a expense category.
def delete_expense_category():
    category = input("Enter the expense category you want to delete: ")
    cursor.execute('SELECT id, category FROM expenses WHERE category = ?', (category,))
    category_list   = cursor.fetchone()
    if category_list:
        cursor.execute('DELETE FROM expenses WHERE category = ?', (category,))
        print(f"Deleting expense category: Category{category_list[0]}, Amount: {category_list[1]}")
    db.commit()
    print(f"Expense category '{category_list}' deleted .")


# Create function to view expenses.
# Use try block for error handling.
def view_expenses(category=None):
    try:
        if category:
            category = category.lower()
            cursor.execute("SELECT * FROM expenses WHERE LOWER(category) = ?", (category,))
        else:
            cursor.execute("SELECT * FROM expenses")

        expenses = cursor.fetchall()

        if expenses:
            for expense in expenses:
                print(expense)
        else:
            print("No expenses found.")

    except sqlite3.Error as e:
        print(f"Error viewing expenses: {e}")  

# Create function for income category to be added.
def add_income_category():
    category = input("Enter the income category you want to add: ")
    cursor.execute("INSERT INTO incomes (category, amount) VALUES (?, 0)", (category,))
    db.commit()
    print(f"Income category '{category}' added successfully.")

# Create function to add income amount.
def add_income():
    category = input("Enter income category: ")
    amount = float(input(f"Enter income amount for '{category}': "))

    cursor.execute("INSERT INTO incomes (category, amount) VALUES (?, ?)", (category, amount))
    db.commit()
    print(f"Income for '{category}' added successfully.")

# update the income category.
def update_income(category, amount):
    cursor.execute("UPDATE incomes SET amount = ? WHERE category = ?", (amount, category))
    db.commit()
    print(f"Income amount for '{category}' updated successfully.")

# Create function to delete a income category.
def delete_income_category():
    category = input("Enter the income category you want to delete: ")
    cursor.execute("DELETE FROM incomes WHERE category = ?", (category,))
    db.commit()
    print(f"Income category '{category}' deleted successfully.") 

# Create function to view income.
def view_incomes():
    cursor.execute("SELECT * FROM incomes")
    incomes = cursor.fetchall()
    for income in incomes:
        print(income) 
def view_incomes(category=None):
    try:
        if category:
            category = category.lower()
            cursor.execute("SELECT * FROM incomes WHERE LOWER(category) = ?", (category,))
        else:
            cursor.execute("SELECT * FROM incomes")

        incomes = cursor.fetchall()

        if incomes:
            for income in incomes:
                print(income)
        else:
            print("No income found.")

    except sqlite3.Error as e:
        print(f"Error viewing expenses: {e}")   

# If 'budget' column does not exist, add it
if not budget_column_exists:
    try:
        cursor.execute("ALTER TABLE expenses ADD COLUMN budget REAL")
        db.commit()
        print("Added 'budget' column to 'expenses' table.")
    except sqlite3.Error as e:
        db.rollback()
        print(f"Error adding 'budget' column to 'expenses' table: {e}")         

def set_budget_for_category(category, budget_amount):
    try:
        cursor.execute("UPDATE expenses SET budget = ? WHERE LOWER(category) = ?", (budget_amount, category.lower()))
        db.commit()
        print(f"Budget for category '{category}' set successfully.")
    except sqlite3.Error as e:
        db.rollback()
        print(f"Error setting budget for category '{category}': {e}")


# Create function to calculate the user's budget.
def calculate_budget():
    cursor.execute("SELECT SUM(amount) FROM expenses")

    total_expenses = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM incomes")
    total_income = cursor.fetchone()[0] or 0

    budget = total_income - total_expenses
    return budget
db.commit()


# Create function to view budget categories.
# Use try block to handle errors.
def view_budget(category=None):
    try:
        if category:
            category = category.lower()
            cursor.execute("SELECT * FROM expenses WHERE LOWER(category) = ?", (category,))
        else:
            cursor.execute("SELECT * FROM expenses")
        budgets = cursor.fetchall()
        if budgets:
            for budget in budgets:
                print(budget)
        else:
            print("No budgets found.")
    except sqlite3.Error as e:
        print(f"Error viewing expenses: {e}")  

# Create function to set financial goals.
def set_financial_goals():
    goal_name = input("Enter the name of your financial goal: ")
    goal_amount = float(input("Enter the target amount for your goal: "))

    cursor.execute("INSERT INTO goals (name, target_amount, current_amount) VALUES (?, ?, 0)", (goal_name, goal_amount))

    db.commit()
    print(f"Financial goal '{goal_name}' set successfully.")

# Create function to view financial goals progress.
def view_progress():
    cursor.execute("SELECT * FROM goals")
    goals = cursor.fetchall()

    if not goals:
        print("No financial goals set.")
    else:
        print("\nFinancial Goals:")
        for goal in goals:
            goal_id, goal_name, target_amount, current_amount = goal
            progress_percentage = (current_amount / target_amount) * 100 if target_amount != 0 else 0

            print(f"\nGoal ID: {goal_id}")
            print(f"Name: {goal_name}")
            print(f"Target Amount: R{target_amount}")
            print(f"Current Amount: R{current_amount}")
            print(f"Progress: {progress_percentage:.2f}%")  
db.commit()              

# Create a while loop and present a menu to the user.
while True:
    print("\nMenu:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View expenses by category")
    print("4. Update expense")
    print("5. Add income")
    print("6. View income")
    print("7. View income by category")
    print("8. Set budget for a category")
    print("9. View budget for a category")
    print("10. Set financial goals")
    print("11. View progress towards financial goals")
    print("12. Delete expense")
    print("13. Delete income")
    print("14. Quit")
    choice = input("Enter your choice 1-13: ")

    # Call function to add expense category if user chooses option 1
    if choice == '1':
        add_expense_category()
    
    # Call function to view expenses if user chooses option 2
    elif choice == '2':
        view_expenses()
    
    # Call function to view expense by category if user chooses option 3
    elif choice == '3':
        category = input("Enter expense category: ")
        view_expenses(category)

    elif choice == '4':
        update_expense_category()    

    # Call function to add income if user chooses option 5
    elif choice == '5':
        add_income()

    # Call function to view income if user chooses option 6
    elif choice == '6':
        view_incomes()

    # Call function to view incomes by category if user chooses option 7
    elif choice == '7':
        category = input("Enter income category: ")
        view_incomes(category)

    # Call function to set budget for expense category if user chooses option 8
    elif choice == '8':
        category = input("Enter expense category: ")
        budget_amount = float(input("Enter budget for the category: "))
        set_budget_for_category(category, budget_amount)

    # Call function to view budget by category if user chooses option 9
    elif choice == '9':
        category = input("Enter expense category: ")
        view_budget(category)

    # Call function to set financial goals if user chooses option 10
    elif choice == '10':
        set_financial_goals()

    # Call function to view financial goals progress if user chooses option 11
    elif choice == '11':
        view_progress()

    # Call function to delete expense category if user chooses option 12
    elif choice == '12':
        delete_expense_category()

    # Call function to delete income category if user chooses option 13
    elif choice == '13':
        delete_income_category()
   
    # Use break function to exit the loop if user chooses option 14
    elif choice == '14':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 13.")

# Commit all changes the database
# Close the connection to the database
db.commit()
db.close()
