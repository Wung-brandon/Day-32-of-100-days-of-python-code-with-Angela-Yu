""" import smtplib

my_email = "wungbrandon27@gmail.com"

password = "psyooadqjqisganq"
#since our email provider is Gmail, we use the smtp.gmail.com 
with smtplib.SMTP("smtp.gmail.com") as connect:
    #securing our connection with our email provider
    connect.starttls()
    connect.login(user=my_email, password=password)
    connect.sendmail(from_addr=my_email, 
                    to_addrs="kumbrandino10@gmail.com",
                    msg="Subject:Hello wung. How are you doing?\n\nThis is the content")
     """

#working with datatime module
from datetime import datetime

now = datetime.now()
month = now.month
minute = now.minute
hour = now.hour
print(f"{hour}:{minute}")
day_week = now.weekday()
print(day_week)
#print(minute)
#print(month)
date_of_birth = datetime(year=2003, month=4, day=4)
print(date_of_birth)
#print(now)