class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Initialize as unread

# Initialize an empty Inbox list
Inbox = []

def populate_inbox():
    # Create and populate three sample email objects
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Thank you for joining our platform.")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "You're making excellent progress.")
    email3 = Email("sender3@example.com", "Your excellent marks!", "You've achieved top marks in your courses.")

    Inbox.extend([email1, email2, email3])

def list_emails():
    # List the emails in the Inbox along with their indexes
    print("Your Inbox:")
    for index, email in enumerate(Inbox):
        status = "Read" if email.has_been_read else "Unread"
        print(f"{index} {status}: {email.subject_line}")

def mark_and_view_unread_emails():
    # Mark selected emails as read and view unread emails
    list_emails()
    indexes = input("Enter the indexes of the emails you want to mark as read (comma-separated): ").split(",")
    
    for index_str in indexes:
        index = int(index_str.strip())
        if 0 <= index < len(Inbox):
            email = Inbox[index]
            if not email.has_been_read:
                email.has_been_read = True
                print(f"Email from {email.email_address} marked as read: {email.subject_line}")
            else:
                print(f"Email from {email.email_address} is already read: {email.subject_line}")
        else:
            print(f"Invalid email index: {index}")

    # Display unread emails
    print("\nUnread Emails:")
    for index, email in enumerate(Inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line}")

# Populate the Inbox with sample emails
populate_inbox()

# Main menu loop
while True:
    print("Email Simulator Menu:")
    print("1. Read an email")
    print("2. Mark and view unread emails")
    print("3. Quit application")
    choice = input("Enter your choice: ")

    if choice == "1":
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
    elif choice == "2":
        mark_and_view_unread_emails()
    elif choice == "3":
        print("Exiting the email simulator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.\n")
