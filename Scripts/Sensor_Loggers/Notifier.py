import smtplib

try:
    from pushbullet import Pushbullet
except ImportError:
    import pip
    pip.main(['install', 'pushbullet.py'])
finally:
    from pushbullet import Pushbullet
    from email.mime.text import MIMEText
    from yamlConfigFile import configFile
    from logger import LOGGER

class Notification(object):
    def __init__(self, gmail_user=None, gmail_password=None, send_to=None, api_key=None):
        self.gmail_password = gmail_password
        self.gmail_user = gmail_user
        self.send_to = send_to
        self.api_key = api_key

    def _email_config(self):
        try:
            self.mail_server = smtplib.SMTP('smtp.gmail.com', 587)
            self.mail_server.ehlo()
            self.mail_server.starttls()
            self.mail_server.login(self.gmail_user, self.gmail_password)
            return True
        except:
            LOGGER.exception("Failed to connnect.")
            return False

    def send_mail(self, alert=None, message=None):
        if self._email_config():
            msg = MIMEText(message)
            msg['Subject'] = alert
            msg['From'] = self.gmail_user
            msg['To'] = self.send_to
            self.mail_server.sendmail(self.gmail_user, [self.send_to], msg.as_string())
            self.mail_server.quit()
            return True

    def send_pushbullet(self, alert=None, message=None):
        push_success = False
        try:
           pb = Pushbullet(self.api_key)
        except :
            return False
        else:
            push_success = pb.push_note(alert, message)['active']

        if push_success:
            return True
        else:
            return False
