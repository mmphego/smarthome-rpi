import urllib
import time
from logger import LOGGER

username = 'mpho112@gmail.com'
password = '@Mpho100%'

LOGGER.info('Sending SMS notification')
def sendSMS(uname, pword, numbers, sender, message):
    try:
        LOGGER.info('Initiating handshake with SMS API')
        params = {'uname': uname, 'pword': pword, 'selectednums': numbers,
            'message' : message, 'from': sender}
        f = urllib.urlopen('https://www.txtlocal.co.uk/sendsmspost.php?'
            + urllib.urlencode(params))
        return f.read()
    except:
        LOGGER.error('Unable to send SMS at this time')
        raise RuntimeError('Unable to send SMS at this time')

def send_sms():
    resp = sendSMS(username, password, '+27761431543',
        'RPi', 'The was someone at the door on {}'.format(time.strftime("%c")))
