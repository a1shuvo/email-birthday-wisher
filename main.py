import smtplib

my_email = "moulik.it@yahoo.com"
password = "hinncrzrbomzagkd"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="moulikittest@gmail.com",
                        msg="Subject:Hello\n\nThis is the message body of the email."
                        )
