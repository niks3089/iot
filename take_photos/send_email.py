import smtplib
import datetime
import argparse
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

toaddr = "niks3089@gmail.com"
parser = argparse.ArgumentParser(description='Send email of the photo taken')
parser.add_argument('email', type=str,
            help='Specify the email adddress to send to')
args = parser.parse_args()
toaddr = args.email

fromaddr = "nik.app.developer@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Photo from Raspberry Pi"
 
body = "Photo taken: " + str(datetime.datetime.now())
 
msg.attach(MIMEText(body, 'plain'))
filename = "image.jpg"
attachment = open("/tmp/image.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "nikhilap1")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
