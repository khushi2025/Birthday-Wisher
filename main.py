import smtplib
import datetime as dt
import pandas
import random
old_name="[NAME]"
my_email="20khushi.sharma@gmail.com"
password="joolfllxqiwwmnyd"
data_files=""
now=dt.datetime.now()
day=now.day
month=now.month
data=pandas.read_csv("birthdays.csv")
for i in range(0,len(data.index)):
    x=data.loc[i,"day"]
    y=data.loc[i,"month"]
    name = data.loc[i,"name"]
    email=data.loc[i,"email"]
    if day==int(x) and month==int(y):
        number=random.randint(1,3)
        with open(f"letter_templates/letter_{number}.txt",mode="r") as file:
            data_file=file.read()
            data_files=data_file.replace("[NAME]",str(name))
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=str(email),msg=f"Subject: HAPPY BIRTHDAY\n\n{data_files}")

