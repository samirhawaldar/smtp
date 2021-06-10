
#Simpe text mail

import smtplib
from email.message import EmailMessage
from password import user, pswd

# password script contains:- user: sender_mail_address, pswd: sender_mail_password.
# It is always good practice to generate token for login.

msg = EmailMessage()

msg['Subject'] = 'Learning... !'
msg['From'] = sender_mail
msg['To'] = receivers_mail

msg.set_content('Hey!')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(user=user, password=pswd)
	smtp.send_message(msg)
