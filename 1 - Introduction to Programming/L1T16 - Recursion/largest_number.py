# Define function that holds num  value
# Use if statement with the len function to return num value
# Use else statement to return max num
def largest_num(num):
    if len(num) == 1:
        return num[0]
    else:
        return max(num[0], largest_num(num[1:]))
# Create a numbers list
# Create max_num variable to hold the largest number
num = [3, 9, 7, 15, 1, 11]
max_num = max(num)
# Print the results
print(f"The largest number in the list is:({num}) => {max_num}")

