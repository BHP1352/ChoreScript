# Henry Chipman
# Chorescript 1.2.0
# 10-4-2016

import datetime
from twilio.rest import TwilioRestClient

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
  for index, braj in enumerate(brajs):
    chore_index = (weeks + index) % len(chores)
    brajs[braj]['chore'] = chores[chore_index]

# returns number of weeks passed since the first day of 2016
def calculate_weeks():
  today = datetime.date.today()
  someday = datetime.date(2016, 1, 1)
  diff = today - someday
  weeks = int(diff.days / 7)
  return weeks

# iterates through all brajs and texts them their chore
def send_texts():
  ACCOUNT_SID = "ACa6b4755c8f58071c638a0b5f775e90e9" 
  AUTH_TOKEN = "0a64c4459d018e93c909b67290a31a95" 
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
  for braj in brajs:
    text = "BRAJ HOUSE MESSAGING\n" + braj + "\nYour chore for this week: " + brajs[braj]['chore'] 
    number = brajs[braj]['phone']
    # client.messages.create(from_='+12062020160',
    #                      to=number,
    #                      body=text)

# TODO email out list
def send_mail():
  print('yo')

### Execute ########################################################################

assign_chores() # assign everyone chores
send_texts() # send texts
# send_mail() # send emails