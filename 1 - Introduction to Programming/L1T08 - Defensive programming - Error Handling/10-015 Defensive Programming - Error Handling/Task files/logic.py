# Ask user to enter name
# Ask user to input temperature.
# Use if statement in accordance with inputed temperatue to print the correct message.
name = input("What is your name?: ")
temp = int(input("what is the temperature today?: "))

if temp >= 20: # Logical error in if statement with temp being greater than the set temp and printing the wrong message.
    print("Its " + str(temp) + " degrees...dont forget your jacket " + name +", it's cold!") # 

else:
    print("It's " + str(temp) + " degrees...dont forget your sun screen " + name +", it's hot!") # The wrong message is again printed as a result of the logical error in line 4.

