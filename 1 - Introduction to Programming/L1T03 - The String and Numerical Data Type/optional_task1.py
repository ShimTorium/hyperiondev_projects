# Ask user to enter 3 values to calculate the area of a triangle.

side1 = int(input("Enter value: ")) # Ask user to enter value 1 

side2 = int(input("Enter value: ")) # Ask user to enter value 2

side3 = int(input("Enter value: ")) # Ask user to enter value 3

perimeter = (side1 + side2 + side3) # Add all 3 values to get the sum value of the perimeter.

s = (perimeter / 2) # Divide perimeter by 2 to get the "S" value.

area = (s*(s-side1)*(s-side2)*(s-side3))**0.5 # Use the formular to calcute the area of the triangle

print(area) # Print the value of the area