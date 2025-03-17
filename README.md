# Email Sending Script (Python)

## Overview
This Python script allows you to send an email using Gmail's SMTP server. The email includes an HTML-formatted message.

## Requirements
- Python 3.x installed
- Internet connection
- Gmail account with SMTP enabled

## Libraries Used
- `smtplib`: Used for sending emails via SMTP.
- `ssl`: Provides secure communication using SSL.
- `email.message`: Used to create email messages with HTML content.

## How to Use
1. Make sure you have enabled "Less secure app access" in your Google account settings (or use an App Password if 2FA is enabled).
2. Run the script in a Python environment.
3. Enter your email password when prompted.
4. The script will log in to your Gmail account and send an email.

## Code Breakdown
- The script defines the sender and receiver email addresses.
- It prompts the user to enter the email password.
- It creates an HTML-formatted email message.
- It connects securely to the Gmail SMTP server and sends the email.

## Security Note
Do not hardcode your password in the script. Use environment variables or secure input methods instead.

## Future Improvements
- Use OAuth 2.0 for authentication instead of a password.
- Add support for attachments.
- Implement error handling for SMTP failures.

