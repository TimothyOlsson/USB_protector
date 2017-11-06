#Ip fetch
from netifaces import interfaces, ifaddresses, AF_INET,AF_INET6
import socket
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
import ipgetter

ipsave=[]

ip=ipgetter.myip()
ipsave.append([ip])

for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )] #Regular
    ipsave.append(addresses)
    
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET6, [{'addr':'No IP addr'}] )] #Regular
    ipsave.append(addresses)

computername=socket.gethostname()


#Mailsend
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("temptib@gmail.com", "apsulfat112")


msg = MIMEMultipart()
msg.attach(MIMEText(''.join(str(x+'\n') for y in ipsave for x in y)))
msg['Subject'] = computername


server.sendmail("temptib@gmail.com", "temptib@gmail.com", msg.as_string())
server.quit()

