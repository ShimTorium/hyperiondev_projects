# define function to hold two values
# Use if statement to see if index is == 0 then return the first element in the list
# Return the sum of the current element and the sum of previous elements
def adding_up_to(nums, index):
    if index == 0:
       return nums[0]
    return nums[index] + adding_up_to(nums, index - 1)

# Create a numbers list
# Create a index variable to hold the single interger outside the list
# Create a result variable to hold the total data of the added up list
nums = [2, 4, 5, 7, 10, 15, 17]
index = 5
result = adding_up_to(nums, index)
# Print the results
print(f"adding_up_to({nums}, {index}) => {result}")
