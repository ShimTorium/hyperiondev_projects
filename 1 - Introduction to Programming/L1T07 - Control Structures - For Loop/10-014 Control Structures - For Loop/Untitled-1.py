# Ask user to input number of rows.
row = int(input("Number of rows: "))

# The for loop iterates the row * 2-1 to check the increasing and decreasing pattern.
# if-else statement within the for loop verifies value for i and determines print the increasing or decreasing pattern
for i in range(row * 2 - 1):
    if i < row:
        print("*" * (i + 1))
    else:
        print("*" * (2 * row - i - 1))

....Certainly! Here's the code that generates the star pattern using a single for loop and an if-else statement:

python
Copy code
row = 5

for i in range(row * 2 - 1):
    if i < row:
        print("*" * (i + 1))
    else:
        print("*" * (2 * row - i - 1))
In this code, row represents the number of rows in the star pattern. The for loop iterates row * 2 - 1 times to cover both the increasing and decreasing parts of the pattern.

The if-else statement inside the loop checks the value of i to determine whether to print the increasing or decreasing part. If i is less than row, it prints i + 1 asterisks. Otherwise, it prints 2 * row - i - 1 asterisks.

When you run this code, it will output the following star pattern:

markdown
Copy code
*
**
***
****
*****
****
***
**
*....