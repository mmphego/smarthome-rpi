import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import urllib2
import time

time.sleep(10)

gmail_user = "homeauto112@gmail.com"
gmail_password = "Livhuwani$12"
to  = "mpho112@gmail.com"

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()

arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
extipaddr = urllib2.urlopen("http://icanhazip.com").read()
my_ip = 'Local address: %s\nExternal address: %s' % (ipaddr, extipaddr)

msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
