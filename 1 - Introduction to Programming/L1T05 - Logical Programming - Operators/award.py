# Ask the user to enter triatholon times

swimming_time = float(input("Whats your swimming time?: ")) # Enter swimming time
cycling_time = float(input("Whats your cycling time?: ")) # Enter cycling time
running_time = float(input("Whats your running time?: ")) # Enter running time

triatholon_time = swimming_time + cycling_time + running_time # Total time of triatholon for all three combined sporting events
print(triatholon_time)

qualifying = 100

if triatholon_time <= float(100): # If time is less than or equal to  the qualifying 100 minutes 
    print("Congratulations! You qualify for Provincial Colours")
elif triatholon_time <= float(105): # If time is within less than or equal to 5 minutes of qualifying time
    print("Congrtatulations! You qualify for Half Provincial Colours")  
elif triatholon_time <= float(110): # If time is within less than or equal to 10 minutes of qualifying time
    print("Congratulations! You qualify for  Provincial Scroll")  
else:
    triatholon_time > float(110) # If time is greater than 10 minutes after the qualifying 100 minutes
    print("No award")

