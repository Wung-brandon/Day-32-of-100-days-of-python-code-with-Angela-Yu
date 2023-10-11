from datetime import datetime
from smtplib import SMTP
import random

now = datetime.now()
week_day = now.weekday()
if week_day == 2:
    with open("quotes.txt", encoding="utf-8") as file:
        all_quotes = file.readlines()
        #print(all_quotes)
        quote = random.choice(all_quotes)
        print(quote)
    my_email = ["wungbrandon27@gmail.com","ginabih404@gmail.com",
                "arreyashley21@gmail.com","juimokamto@gmail.com",
                "sanjichick30@gmail.com","borisbinwung@gmail.com",
                "enowdanlo@gmail.com","Wisdomudechi832gmail.com",
                "Besongngemtakor@gmail.com"]
    my_password = "syutaucitueonwcg"
#since our email provider is Gmail, we use the smtp.gmail.com 
    with SMTP("smtp.gmail.com") as connect:
    #securing our connection with our email provider
        connect.starttls()
        connect.login(user=my_email, password=my_password)
        connect.sendmail(from_addr=my_email, 
                        to_addrs=my_email,
                        msg=f"Subject:Tuesday Motivational Quotes. \n\n{quote}")
   