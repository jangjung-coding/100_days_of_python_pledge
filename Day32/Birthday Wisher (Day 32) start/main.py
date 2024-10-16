# SMTP : Simple Mail Transfer Protocol
import smtplib

my_email = "jangisalive1650@gmail.com"
my_password = "jangisalive1650"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() # Transport Layer Security
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="jwjang923@gmail.com", msg="Subject:Hello\n\nThis is the body of my email.")
connection.close()