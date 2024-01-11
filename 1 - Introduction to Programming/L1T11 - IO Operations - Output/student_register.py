# Ask student user to input total amount of students registering for the exam
total_students = int(input("How many students are registering for the exam?: "))

# Use with function to open the text document as a file
# Then use a for loop to find the range of input total students
# Then ask the student to input their student ID
# Use a write statement to enter student number and a underscore solid line for the students signature
with open("reg_form.txt", "w") as file:
        for i in range(total_students):
            student_id = input(f"Enter the student ID for student {i + 1}: ")
            file.write(f"\n{student_id}. ________________________\n\n") 

# Print the total amount of students and a message that thier ID's have been written to the text file
print(f"{total_students} student IDs have been written to reg_form.txt successfully.")



                                          