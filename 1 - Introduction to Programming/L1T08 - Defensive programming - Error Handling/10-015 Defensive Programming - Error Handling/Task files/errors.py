# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # print fuction contained syntax errors with no parantheses and a space between print string.
print("\n") # Contained syntax error with no parentheses.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = str(24)
age = int(age_Str) # Contains logical error for casting string to interger.
print("I'm " + str(age) + " years old.") # Contained runtime errors and age variable to string.

# Variables declaring additional years and printing the total years of age
years_from_now = float(3.5)

total_years = str(age + years_from_now)

# Contained syntax errors with no parentheses.
print("The total number of years " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = float(total_years) * 12
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # Contained syntax and runtime errors with no parentheses and casting float to string value

#HINT, 330 months is the correct answer

