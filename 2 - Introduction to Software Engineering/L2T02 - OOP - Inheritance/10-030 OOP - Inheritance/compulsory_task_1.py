# Create parent course class
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = "Cape Town"
    
    # Create function to hold contact details of website
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Create function to set the head office location
    def head_office_location(self):
        print("Head office location: Cape Town") 

# Define the subclass OOPCourse
# Create constructor method
# Use super function to give access to inherited methods from the parent class 
class OOPCourse(Course):
    def __init__(self):
        super().__init__()
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    # Create function to hold course and trainer details
    def trainer_details(self):
        print(f"Course: {self.description}")
        print(f"Trainer: {self.trainer}")

    # Create function to show course ID
    def show_course_id(self):
        print("Course ID: #12345")

# Create an object of the subclass OOPCourse and name it course_1
course_1 = OOPCourse()

# Call methods on the course_1 object
course_1.contact_details()
course_1.head_office_location()
course_1.trainer_details()
course_1.show_course_id()
       






