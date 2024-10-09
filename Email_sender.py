import smtplib

sender_email = "richardobinna993@gmail.com"
rec_email = "richardokeke24@gmail.com"
password = input(str("Please enter the password: "))
message = "Hey this is Richard and i am your student."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
server.close()
print("Server closed")