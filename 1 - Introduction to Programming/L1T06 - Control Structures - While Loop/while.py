# use while loop to always ask user to input various number/s
# total will calculate the total sum of all inputed numbers by user
# num_count calculates how much numbers are inputed  by user
total = 0
num_count = 0
number = int(input("Please enter a number (-1 to break): "))

# if the number is not = -1 in the while loop the user will be asked to enter a number again 
while number != -1:
    total += number
    num_count += 1
    
    number = int(input("Please enter a number (-1 to break): "))


    # if number is == to -1 the total and the average will be printed
    # break is used at the end to exit the while loop
    if number == -1:
        average = total/num_count
        print("the total is", total)
        print("the average is" , average)
        break
    
        









