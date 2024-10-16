##################### Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "jangisalive1650@gamil.com"
password = "jangisalive1650"

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()} # Dictionary comprehension

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open('file_path') as letter_file:
        birthday_person = birthdays_dict[today_tuple]
        letter = letter_file.read()
        letter = letter.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person['email'], 
            msg=f"Subject:Happy Birthday\n\n{letter}")
        
    
    

