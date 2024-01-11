# Ask user to input number of rows.
row = int(input("Number of rows: "))
#row = 5
# The for loop iterates the row * 2-1 to check the increasing and decreasing pattern.
# if-else statement within the for loop verifies value for i and determines print the increasing or decreasing pattern
for i in range(row * 2 - 1):
    if i < row:
        print("*" * (i + 1))
    else:
        print("*" * (2 * row - i - 1))








    
    
