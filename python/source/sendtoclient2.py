#importing the Yagmail library
import yagmail

try:
    #initializing the server connection
    yag = yagmail.SMTP(user='aviation@rare-air.co.uk', password='R@r€@!r20')
    #sending the email
    yag.send(to='ericv@rare-air.co.uk', subject='Sending Attachment', contents='Please find the image attached', attachments='../Resources/GenericQuote.pdf')
    print("Email sent successfully")
except:
    print("Error, email was not sent")
