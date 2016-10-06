# Henry Chipman
# Chorescript 1.2.0
# 10-4-2016

import datetime
from twilio.rest import TwilioRestClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

brajs = {
  'Kelly': {
      'phone':'+12068192190',
      'email':'bkpratt@uw.edu',
      'chore':''
    },
  'Nicky': {
      'phone':'+12063590744',
      'email':'nick.garzon@gmail.com',
      'chore':''
    },
  'Jake': {
      'phone':'+15092209113',
      'email':'jwmouser@gmail.com',
      'chore':''
    },
  'Torin': {
      'phone':'+12063309704',
      'email':'torin206@gmail.com',
      'chore':''
    },
  'Jeremy': {
      'phone':'+12062912466',
      'email':'perezje43@gmail.com',
      'chore':''
    },
  'Chip': {
      'phone':'+12062406461',
      'email':'hdchipman@msn.com',
      'chore':''
    }
}

# Need this to maintain the order that was used in the last script
# perhaps we can get rid of this once we make a full rotation through the chores
braj_order = ["Jeremy", "Chip", "Kelly", "Nicky", "Jake", "Torin"]

chores = [
  'Take out full trashes in the house as needed and to curb on Tuesday',
  'Sweep and Clean kitchen/dining room/living room floor on Weekend',
  'Clean bathroom (floor/sink/toilet) (tub if dirty) on Weekend',
  'Organize kitchen (Dishes/stovetop/counters) on Weekend',
  'Groundskeeping (clean trash/mow/clean porch) on Weekend',
  'Bye week'
]

### Methods ###################################################################### 

# assigns chores to people based on the week
def assign_chores():
  weeks = calculate_weeks()
  for index, braj in enumerate(braj_order):
    chore_index = (weeks + index) % len(chores)
    brajs[braj]['chore'] = chores[chore_index]

# returns number of weeks passed since the first day of 2016
def calculate_weeks():
  today = datetime.date.today()
  someday = datetime.date(2016, 10, 2)
  diff = today - someday
  weeks = int(diff.days / 7)
  return weeks

# iterates through all brajs and texts them their chore
def send_texts():
  ACCOUNT_SID = "ACa6b4755c8f58071c638a0b5f775e90e9" 
  AUTH_TOKEN = open('twilio_token.txt', 'r').read()
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
  for braj in brajs:
    text = "BRAJ HOUSE MESSAGING\n" + braj + "\nYour chore for this week: " + brajs[braj]['chore'] 
    number = brajs[braj]['phone']
    client.messages.create(from_='+12062020160',
                         to=number,
                         body=text)


# emails all chores to everyone
# password for gmail account must be kept in password.txt
def send_mail():
  for braj in brajs:
    fromaddr = "brajhouse2016@gmail.com"
    toaddr = brajs[braj]['email']
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "House duties for this week"
    body = mail_text()
    password = open('password.txt', 'r').read()
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("brajhouse2016@gmail.com", password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

# creates content of email
def mail_text():
  body = ""
  for braj in brajs:
    body = body + '\n' + braj + ': ' + brajs[braj]['chore'] 
  return body

### Execute ########################################################################

assign_chores() # assign everyone chores
send_texts() # send texts
send_mail() # send emails