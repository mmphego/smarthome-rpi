import time
#from logger import LOGGER
try:
    import smsapi
except ImportError:
    import pip
    pip.main(['install', 'smsapi'])
finally:
    from smsapi.client import SmsAPI
    from smsapi.responses import ApiError

#LOGGER.info('Sending SMS notification')

def send_SMSAPI(sendto, message):
    username = 'mpho112@gmail.com'
    password = '!nerd001'
    api = SmsAPI()

    api.set_username(username)
    api.set_password(password)

    #sending SMS
    try:
        api.service('sms').action('send')

        api.set_content('Hello [%1%]')
        api.set_params(message)
        api.set_to(sendto)
        api.set_from('Info') #Requested sender name

        result = api.execute()

        for r in result:
            return r.status

    except ApiError, e:
        print '%s - %s' % (e.code, e.message)

def send_sms():

    resp = send_SMSAPI('+27761431543',
        'The was someone at the door on {}'.format(time.strftime("%c")))
    return resp

import IPython;IPython.embed()
