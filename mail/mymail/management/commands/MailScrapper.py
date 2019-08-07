import smtplib
from datetime import datetime
import time

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('SENDERS MAIL ID', 'PASSWORD')
    subject = "Reminder"
    body= "yo, howzzzzz life?"
    msg = f'Subject: {subject}\n\n{body}'


    server.sendmail(
        'xxxxxxxx@gmail.com',
        'xxxxxxxx@gmail.com',
        msg
    )
    print("yo")
    server.quit()

    
        

