from django.core.management.base import BaseCommand, CommandError
from .MailScrapper import send_mail
from datetime import datetime
import time
#two options if you run python manage.py runserver then mail will be sent every monday to the mail address specified in
#MailScrapper.py.
#if you go for submit option like on the local host then mail will be sent once to the specified address in 
# new/mail/mymail/views.py


class Command(BaseCommand):
    

    

    def handle(self, *args, **options):
    
        flag=True
        while True :

            current_date=datetime.today()
            current_day=current_date.weekday()
            
            if(current_day==1 ):
                if flag:

                    send_mail()
                    flag=False

            time.sleep(60*60*24)
            flag=True


