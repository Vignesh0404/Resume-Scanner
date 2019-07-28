from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import getpass

msg = MIMEMultipart()

msg['From'] = input('Enter sender mail address:\n')
msg['To'] = input('Enter receiver mail address:\n')
msg['Subject'] = input('Enter subject')
if int(input('Attaching image? (0/1)')):
    msg.attach(MIMEImage(open(input('Enter image path'),'rb').read()))
msg.attach(MIMEText(input('Enter Message:\n'),'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], getpass.getpass())
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print ("successfully sent email to %s:" % (msg['To']))
