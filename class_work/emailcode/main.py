import emaillogic
subject = input("Enter email subject: ")
body = input("Enter email body: ")
choice = input("Do you want to send (1) single Email or (2) Bulk Emails? Enter 1 or 2:")
if choice == "1":
    recipent = input("Enter recipient email address: ")
    emaillogic.send_email(recipent, subject, body)
elif choice == "2":
    csv_file = input("Enter path to CSV file with email addresses: ")
    emaillogic.send_bulk_emails(csv_file, subject, body)
else:
    print("Invaild choice! please enter 1 or 2.")
