import sqlite3

# Create a connection to the database.
# Get the cursor object.
db = sqlite3.connect("ebookstore.db")
cursor = db.cursor()

# Create table called book.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
''')


# Existing data with id, name, author and stock values.
data_books = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
]

# Create define function for data entry.
# Use try block to incorperate exception handling.
# Insert existing data into table using defining function.
def data_entry():
    try:
        for item in data_books:
            cursor.executemany('INSERT INTO book(id, title, author, qty) VALUES (?, ?, ?, ?)', item)
        db.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        db.rollback() 
data_entry()

# Create define function to add a book to the database.
# Use try block for exception handling to increment the max id if new books are added.
# Ask user to input id, title, author and quantity.
# Insert added books into the table and commit the changes
def add_book():
    try:
        cursor.execute('SELECT MAX(id) FROM book')
        max_id = cursor.fetchone()[0]
        next_id = max_id + 1 if max_id is not None else 3000

        title = input("Enter book title: ")
        author = input("Enter book author: ")
        qty = int(input("Enter book quantity: "))
        cursor.execute('INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', (next_id, title, author, qty))
        db.commit()
        print(f"Book added successfully with ID {next_id}.")
    except ValueError:
        print("Invalid input. Please enter a valid numerical value for quantity.")
    except sqlite3.IntegrityError as e:
        print(f"An error occurred while adding the book: {e}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Create define function to update the book database.
# Ask user to input the book id.
# Ask user to input the quantity.
# Update and set the database and commit the changes.
def update_book():
    id = int(input("Enter book ID to update: "))
    qty = int(input("Enter new quantity: "))
    cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (qty, id))
    db.commit()
    print("Book updated successfully.")

# Create define function to delete books from table.
# Ask user to input id
# Use cursor object to delete books and commit changes.
def delete_book():
    id = int(input("Enter book ID to delete: "))
    cursor.execute('SELECT id, title FROM book WHERE id = ?', (id,))
    book_info = cursor.fetchone()
    # Use if statement to print what book id and title is being deleted.
    if book_info:
        print(f"Deleting book: ID {book_info[0]}, Title: {book_info[1]}")
        cursor.execute('     FROM book WHERE id = ?', (id,))
        db.commit()
        print("Book deleted successfully.")
    else:
        print("Book not found with the given ID.")
    title = cursor.fetchall()
    db.commit()

# Create define function to search for books.
# Ask user to enter search title or author.
# Use cursor object to select all where title/ author relates.
# Use cursor to fetch all that relates.
def search_books():
    search_term = input("Enter book title or author to search: ")
    cursor.execute('SELECT * FROM book WHERE title LIKE ? OR author LIKE ?', ('%' + search_term + '%', '%' + search_term + '%'))
    books = cursor.fetchall()
    if not books:
        print("No books found.")
    else:
        print("Books found:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

# Use while loop to present a menu to the user.
while True:
    db = sqlite3.connect("ebookstore.db")
    cursor = db.cursor()
    data_entry()
    print("\nMenu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")
    choice = input("Enter your choice: ")


    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '0':
        print("You have quit the program.")
        break
    else:
        print("Invalid choice. Please try again.")


# Close the database connection
db.commit()
db.close()
