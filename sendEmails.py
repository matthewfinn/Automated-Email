# Settings
#!/usr/bin/env python


SMTP_SERVER = sys.argv[1]
print "SMTP Server : %s" % SMTP_SERVER

#SMTP_PORT = 465
SMTP_PORT = sys.argv[2]
print "SMTP Port : %s" % SMTP_PORT

SMTP_PASSWORD = 'taylor210'
SMTP_TO = 'matt.finn@hotmail.com'
SMTP_FROM = sys.argv[0]
SMTP_USERNAME = SMTP_FROM
#SMTP_SERVER = sys.argv[1]

TEXT_FILENAME = 'emailContent.txt'
MESSAGE = """This is the message
to be sent to the client.
"""

# Now construct the message
import smtplib, email
from email import encoders
import os
import sys

msg = email.MIMEMultipart.MIMEMultipart()
body = email.MIMEText.MIMEText(MESSAGE)
attachment = email.MIMEBase.MIMEBase('text', 'plain')
#attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(TEXT_FILENAME))
encoders.encode_base64(attachment)
subject = 'Test Email'
msg['Subject'] = subject
msg.attach(body)
msg.attach(attachment)
msg.add_header('From', SMTP_FROM)
msg.add_header('To', SMTP_TO)

# Now send the message
mailer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# EDIT: mailer is already connected
# mailer.connect()
mailer.ehlo()
mailer.starttls()
mailer.set_debuglevel(False)
mailer.login(SMTP_USERNAME, SMTP_PASSWORD)
print "User Logged In: %s" % SMTP_USERNAME
mailer.sendmail(SMTP_FROM, [SMTP_TO], msg.as_string())
print "Email Sent From: %s" % SMTP_FROM
print "Email Sent To: %s" % SMTP_TO
mailer.close()
