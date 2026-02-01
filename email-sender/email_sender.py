import smtplib

send_to = input("Enter email of receipent:\n")

content = input("enter the content of email:\n")

def email(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender@gmail.com','1234')
    server.sendmail('sender@gmail.com',to,content)
    server.close()

email(send_to, content)