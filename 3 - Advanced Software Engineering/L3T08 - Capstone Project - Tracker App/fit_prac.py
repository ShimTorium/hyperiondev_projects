import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('fitness_tracker.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS workout_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        name TEXT,
        progress INTEGER
    )
''')

# Add more tables for exercises, user routines, etc.

# Function to add a new workout category
def add_workout_category(name):
    cursor.execute('INSERT INTO workout_categories (name) VALUES (?)', (name,))
    conn.commit()

# Function to update a workout category
def update_workout_category(category_id, new_name):
    cursor.execute('UPDATE workout_categories SET name = ? WHERE id = ?', (new_name, category_id))
    conn.commit()

# Function to delete a workout category
def delete_workout_category(category_id):
    cursor.execute('DELETE FROM workout_categories WHERE id = ?', (category_id,))
    conn.commit()

# Function to add a workout goal
def add_workout_goal(category_id, name, progress=0):
    cursor.execute('INSERT INTO goals (category_id, name, progress) VALUES (?, ?, ?)', (category_id, name, progress))
    conn.commit()


# Example usage
add_workout_category('Cardio')
update_workout_category(1, 'Cardiovascular')
delete_workout_category(2)
add_workout_goal(1, 'Run 5k', 0)

# Close the database connection
conn.close()
