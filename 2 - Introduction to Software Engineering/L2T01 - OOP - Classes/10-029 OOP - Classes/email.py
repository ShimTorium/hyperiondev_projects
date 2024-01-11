# Create email class.
class Email:
    # Class variable initialised to false because email has not yet been read.
    has_been_read = False
   
    # Create constructor method to withhold 3 parameters.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create function to set has been read to True
    def mark_as_read(self):
        self.has_been_read = True

# Create a empty Inbox list.
Inbox = []
# Create function to populate the inbox with email data.
def populate_inbox():
    email1 = Email("onlineshop@store.co.za", "Welcome to our online store", "Thank you for registering an online account.")
    email2 = Email("onlineshop@store.co.za", "Thank you for making a purchase", "You're purchase is being processed.")
    email3 = Email("courier@courierserv.co.za", "Your package is being dispatched", "Someone will make contact with you shortly.")
    Inbox.extend([email1, email2, email3])

# Create a function to list the mail in the inbox.
# Use for loop with enumerate function to loop through the mail to check if mails read status
def list_emails():
    print("Inbox:")
    for index, email in enumerate(Inbox):
        if email.has_been_read:
            status = "Read"
            
        else:
            status = "Unread"
            print(f"{index} {status}: {email.subject_line}")
        
# Create function  to read the mail
# Use if statememnt to display the selected email and mark it as read
def read_email(index):
    if 0 <= index < len(Inbox):
        email = Inbox[index]
        print(f"\nEmail from {email.email_address}:")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}\n")
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")
    else:
        print("Invalid email index. Please choose a valid email to read.\n")

    # Use for loop with enumerate function to display and check unread emails
    for index, email in enumerate(Inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line}")       

# Populate the emails inbox with mail data
populate_inbox()

# Create a while loop to display main menu to the user.
while True:
    print("Email Menu:")
    print("1. Read mail")
    print("2. View unread mail")
    print("3. Exit email")
    choice = (input("Enter your choice: "))
    
    # Use if statement if users choice is == 1 to present the list of emails.
    if choice == "1":
        list_emails()   
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
          
    # Use else-if statement if users choice == 2 check mails read status.
    # Use for loop with enumerate function to display and check unread mails.
    elif choice == "2":      
        print("\nUnread Emails:")
        for index, email in enumerate(Inbox):
            if not email.has_been_read == True:
                status = "Unread"
                print(f"{index}. {status}: {email.subject_line}")

    # Use else-if statement if users choice == 3 to break the loop and exit the program.    
    elif choice == "3":
        print("Exiting the email...Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.\n")
