import smtplib
import datetime as dt
import random

my_email = "moulik.it@yahoo.com"
password = "hinncrzrbomzagkd"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="moulikittest@gmail.com",
                            msg=f"Subject:Monday Motivation Quotes\n\n{quote}"
                            )
