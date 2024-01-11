# Ask user to input requested data.
name = input("Please enter the person's name: ")
age = int(input("Please enter the person's age: "))
eye_colour = input("Please enter the person's eye colour: ")
hair_colour = input("Please enter the person's hair colour: ")

# Create and define a parent class.
# Use constructor method to initialise attributes.
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
    
    # Create function to hold a can_drive call method.
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

# Create child subclass of the parent class.
# Use override method to alter inherited method from parent class.
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

# Use if statement to determine if the person is 18 or older.
# Use else statement to then state its a child if not == 18.
if age >= 18:
    person = Adult(name, age, eye_colour, hair_colour)
else:
    person = Child(name, age, eye_colour, hair_colour)

# Use the can_drive() call method to print whether the person can is eligible to drive or not.
person.can_drive()
