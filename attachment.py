
#sending images/files via mail


import smtplib
from email.message import EmailMessage
import imghdr
from password import user, pswd

# password script contains:- user: sender_mail_address, pswd: sender_mail_password.
# It is always good practice to generate token for login.

receiver = [receiver1_mail, receiver2_mail]

msg = EmailMessage()

msg["Subject"] = "Sending an image"
msg["From"] = user
msg["To"] = ", ".join(receiver)

msg.set_content("Hey! Look at this.")
files = ["img1.jpg"]

for file in files:
     with open(file,"rb") as f:
          file_data = f.read()
          file_type = imghdr.what(f.name)
          file_name = f.name
     #for pdf file maintype=application and subtype=octet-stream
     msg.add_attachment( file_data, maintype="image", subtype= file_type, filename= file_name)

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
     smtp.login(user,pswd)
     smtp.send_message(msg)
