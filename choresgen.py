# Chore script
import datetime
from datetime import date
import requests
import smtplib

today = list(str(datetime.date.today()))
today_s = str(today[5] + today[6] + '/' + today[8] + today[9])

now = datetime.date.today()
today_date = date(now.year, now.month, now.day)
start_date = date(2016, 9, 12)
delta = today_date - start_date


def send_email(user, pwd, recipient, subject, body):

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"



## Main_______________________________________________________________________
#_____________________________________________________________________________

ppl = ['Kelly','Nicky','Jake','Torin','Jeremy','Chip']
chores = ['Take out full trashes in the house as needed and to curb on Tuesday',\
          'Sweep and Clean kitchen/dining room/living room floor on Weekend',\
          'Clean bathroom (floor/sink/toilet) (tub if dirty) on Weekend',\
          'Organize kitchen (Dishes/stovetop/counters) on Weekend',\
          'Groundskeeping (clean trash/mow/clean porch) on Weekend',\
          'Bye week']

emails = ['torin206@gmail.com','bkpratt@uw.edu','hdchipman@msn.com',\
            'jwmouser@gmail.com', 'perezje43@gmail.com','nick.garzon@gmail.com']

sub = 'Chore assignments for the week of %s' % today_s


if delta.days > 42:
    while delta.days > 42:
        delta.days -= 42
    print delta.days


# This works but it needs some desperate cleanup
if (delta.days == 42):
    body = '%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s' % \
              (ppl[1],chores[0],ppl[2],chores[1],ppl[3],chores[2],ppl[4],\
              chores[3],ppl[5],chores[4],ppl[0],chores[5])
elif (delta.days == 35):
    body = '%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s' % \
              (ppl[2],chores[0],ppl[3],chores[1],ppl[4],chores[2],ppl[5],\
              chores[3],ppl[0],chores[4],ppl[1],chores[5])
elif (delta.days == 28):
    body = '%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s' % \
              (ppl[3],chores[0],ppl[4],chores[1],ppl[5],chores[2],ppl[0],\
              chores[3],ppl[1],chores[4],ppl[2],chores[5])
elif (delta.days == 21):
    body = '%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s' % \
              (ppl[4],chores[0],ppl[5],chores[1],ppl[0],chores[2],ppl[1],\
              chores[3],ppl[2],chores[4],ppl[3],chores[5])

elif (delta.days == 14):
    body = '%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s' % \
              (ppl[5],chores[0],ppl[0],chores[1],ppl[1],chores[2],ppl[2],\
              chores[3],ppl[3],chores[4],ppl[4],chores[5])

elif (delta.days == 7):
    body = '%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s' % \
              (ppl[0],chores[0],ppl[1],chores[1],ppl[2],chores[2],ppl[3],\
              chores[3],ppl[4],chores[4],ppl[5],chores[5])


send_email(YOUR_EMAIL, YOUR_EMAIL_KEY, emails, sub, body)
