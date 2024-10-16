# Welcome to the Monday Motivation Quotes Generator!

import datetime as dt
import random
import smtplib

my_email = "jangisalive1650@gmail.com"
my_email_password = "jangisalive1650"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0: # Monday
    with open("Day32/Birthday Wisher (Day 32) start/MondayMotivationQuotes.py") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_email_password)
        connection.sendmail(from_addr=my_email, to_addrs="jwjang923@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")
        connection.close()
else:
    print("Not Monday")