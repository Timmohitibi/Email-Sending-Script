import smtplib  # Importing the module for sending emails using SMTP
import ssl  # Importing the module to create a secure connection
from email.message import EmailMessage  # Importing the module to create email messages

# Email subject and body content
subject = "Email From Python"
body = "This is an email from Python!"

# Sender and receiver email addresses
sender_email = "timothyitibi00@gmail.com"
receiver_email = "timothyitibi@gmail.com"

# Prompting the user to enter the email password securely
password = input("Enter your password: ")

# Creating an email message instance
message = EmailMessage()
message["From"] = sender_email  # Setting the sender's email
message["To"] = receiver_email  # Setting the recipient's email
message["Subject"] = subject  # Setting the email subject

# HTML email content
html = f"""
<html>
  <body> 
    <h1> {subject} </h1>
    <p> {body} </p>
  </body>
</html>
"""

# Adding the HTML content as an alternative to plain text
message.add_alternative(html, subtype="html")

# Creating a secure SSL context
context = ssl.create_default_context()
print("Sending Email...")

# Connecting to Gmail's SMTP server using SSL
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)  # Logging into the email account
    server.sendmail(sender_email, receiver_email, message.as_string())  # Sending the email
    print("Email sent successfully!")
