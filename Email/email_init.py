import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


############
# change security on https://myaccount.google.com/u/2/lesssecureapps
# allow smtp  https://mail.google.com/mail/u/2/#settings/fwdandpop
###############

port = 465 # Adding values as default
sll = ssl.create_default_context() # ssl command for gmail


def send_values_to_user(sender_email,sender_password,receiver_email,subject,text): # text should be html, needs to configure the value on different module
    #trying to add the values in a json file - probably firebase to extract and consider the version
    with  smtplib.SMTP_SSL('smtp.gmail.com', port=port, context=sll) as smtpObj:
        smtpObj.login(user=sender_email, password=sender_password)
        smtpObj.sendmail(sender_email, receiver_email, create_message(sender_email, receiver_email,subject,text))

def create_message(from_e,to,subject,text):
    message = MIMEMultipart('related')
    message['Subject'] = 'Designing data'
    message['From'] = from_e
    message['To'] = to
    #html = open('message.txt','r')
    part2 = MIMEText(text, "html")
    #message.attach(part2)
    return message.as_string()

