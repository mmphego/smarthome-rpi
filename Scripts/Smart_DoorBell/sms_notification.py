import urllib
import time
username = 'mpho112@gmail.com'
password = '@Mpho100%'

def sendSMS(uname, pword, numbers, sender, message):
    params = {'uname': uname, 'pword': pword, 'selectednums': numbers,
        'message' : message, 'from': sender}
    f = urllib.urlopen('https://www.txtlocal.co.uk/sendsmspost.php?'
        + urllib.urlencode(params))
    return f.read()

def send_sms():
    resp = sendSMS(username, password, '+27761431543',
        'RPi', 'The was someone at the door on {}'.format(time.strftime("%c")))
