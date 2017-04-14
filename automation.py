#!/usr/bin/env python import sendEmails

import time
import random
import sys
from threading import Thread

SMTP_SERVER_OUTLOOK = 'smtp-mail.outlook.com'
SMTP_SERVER_HOTMAIL = 'smtp.live.com'
SMTP_SERVER_GMAIL = 'smtp.gmail.com'
SMTP_SERVER_YAHOO = 'smtp.mail.yahoo.com'
CHAR_HOT = 'hotmail'
CHAR_YAH = 'yahoo'
CHAR_GM = 'gmail'
CHAR_OUT = 'outlook'
PORT_H = 587
PORT_G = 587
PORT_Y = 465
PORT_O = 587
FILENAME = 'emails.txt'


with open(FILENAME, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

for i in range(len(array)):
    print "Executing automated email script passing in email: %s" % array[i]
    server = []
    sys.argv = [array[i]]
    server = array[i].split("@")
    if CHAR_OUT in server[1]:
        sys.argv.append(SMTP_SERVER_OUTLOOK)
        sys.argv.append(PORT_O)
    elif CHAR_HOT in server[1]:
        sys.argv.append(SMTP_SERVER_HOTMAIL)
        sys.argv.append(PORT_H)
    elif CHAR_GM in server[1]:
        sys.argv.append(SMTP_SERVER_GMAIL)
        sys.argv.append(PORT_G)
    elif CHAR_YAH in server[1]:
        sys.argv.append(SMTP_SERVER_YAHOO)
        sys.argv.append(PORT_Y)
    execfile('sendEmails.py')
    tm = random.randint(1, 11)
    print "Sleep Time: %d." % tm
    time.sleep(tm)
