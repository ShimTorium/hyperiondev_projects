# Ask user to input atleast two full names.
full_name = input("Please enter your full name: ")

if len(full_name) == 0: # if user enters zero characters a error message will be printed and ask the user to enter full names again.
    print("You have not entered anything. Please enter your full name. ")

elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make  sure you have entered your full name and surname")
# If the user uses less than 4 letters a error message will be printed.

elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure you enter your full name. ")    
# If the user enters more than 25 characters a error messge will be printed.

else:
    full_name == full_name # Only if characters/full names are entered will a validating message be printed along with the full name.
    print("Thank you for entering full name")
    print(full_name)   

