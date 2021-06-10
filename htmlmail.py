
# HTML page rendering in receivers mail


import smtplib
from email.message import EmailMessage
from password import user, pswd

# password script contains:- user: sender_mail_address, pswd: sender_mail_password.
# It is always good practice to generate token for login.

msg = EmailMessage()

receiver = [receiver1]

msg["Subject"] = "How is it looking"
msg["From"] = sender_mail
msg["To"] = ", ".join(receiver)

msg.set_content("alternate plain text")
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
<title> Simple page </title>
<style>
h1{
color: blue;
font-style:cursive, san-serif;
}
</style>
</head>
<body>
<h1> Title </h1>
<h4> Heading</h4>
</body>
</html>
""", subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
     smtp.login(user=user, password=pswd)
     smtp.send_message(msg)
