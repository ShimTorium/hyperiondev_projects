import sqlite3

# Insert data of new rows into the python_programming table.
initial_data = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

# Connect to the database.
# Get the cursor object.
db = sqlite3.connect("mydatabase.db")
cursor = db.cursor()

# Create table called python_programming
cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  grade INTEGER)''')
db.commit()

# Create function to enter new data
def data_entry():
    for item in initial_data:
        cursor.execute('INSERT INTO python_programming(id, name, grade) VALUES (?, ?, ?)', item)
    db.commit()
data_entry()


# Rest of your code...


# Select all records from the table with a grade between 60 and 80.
cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
selected_records = cursor.fetchall()
print("Records with grades between 60 and 80:")
for record in selected_records:
    id_value = str(record[0])
    name_value = str(record[1])
    grade_value = str(record[2])
    formatted_record = f"id: {id_value}, name: {name_value}, grade: {grade_value}"
    print(formatted_record)

# Change and update Carl Davis's grade to 65 in the table.
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")

# Delete Dennis Fredrickson's row from the table.
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")
print("Dennis Fredrickson's row has been deleted.")

# Change the grade of all people with an id less than 55 in the table.
cursor.execute("UPDATE python_programming SET grade = grade + 3 WHERE id < 55")
print("Students with ID below 55 are updated.")

# Commit the changes to the db, close the cursor, and close the connection.
db.commit()
cursor.close()
db.close()
print("Connection to the database closed.")
