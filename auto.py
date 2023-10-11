from datetime import datetime
from smtplib import SMTP
import pandas as pd
from random import randint

data = pd.read_csv("birthdays.csv")

MY_EMAIL = "wungbrandon27@gmail.com"
MY_PASSWORD = "syutaucitueonwcg"

# HINT 1: Only the month and day matter. 
today = datetime.now()
today_turple = (today.month, today.day)

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
birthday_dic = {(data_row["month"],data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
if today_turple in birthday_dic:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
    birthday_person = birthday_dic[today_turple]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        name_birth = content.replace("[NAME]",birthday_person["name"])
        print(name_birth)
        # 4. Send the letter generated in step 3 to that person's email address.
        # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
        
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday! \n\n {name_birth}")
    
    
    