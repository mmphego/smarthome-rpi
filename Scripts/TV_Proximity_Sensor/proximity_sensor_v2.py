import numpy as np
import subprocess
import time
import sys
try:
    from logger import LOGGER
except ImportError:
    LOGGER = None
from datetime import datetime
from yamlConfigFile import configFile
from pushnotify import send_pushbullet
sys.path.insert(1, '/home/pi/Scripts/Relay_Control/')
from relay_control import *

mp3_player = '/usr/bin/mpg123 '
mp3_file = '/home/pi/Scripts/TV_Proximity_Sensor/close_to_tv.mp3'
play_over_ssh = configFile()['remote_audio_conf'] # cmd
remote_play = configFile()['remote_play']  #  Bool


class TimerClass(object):
    def __init__(self):
        self.sleep_time = configFile()['TVProximity']['RefreshRate']
        self.wait_time = configFile()['TVProximity']['WaitTime']
        self._threshold = configFile()['TVProximity']['Distance']
        self.sample_size = configFile()['TVProximity']['NoSamples']

    def notification(self, notify=False):
        """
        This will sound a siren or notification to move away
        :return: <nothing>
        """
        if notify:
            if remote_play:
                subprocess.call ('cat {} | {}'.format(mp3_file, play_over_ssh), shell=True)
            else:
                with open(subprocess.os.devnull, 'rb') as devnull:
                    subprocess.Popen(mp3_player + mp3_file,
                                     shell=True, stdout=devnull,
                                     stderr=devnull, ).communicate()
            ##print 'Warning: Too close to the TV: {} cm.'.format(self.distance())
            alert = 'TV Proximity Warning notification'
            message = 'The person was warned at {}'.format(str(datetime.now()))
            send_pushbullet(alert, message)
            time.sleep(self.wait_time)
            return True

    def tv_On(self):
        alert = 'TV Proximity Notification'
        message = 'TV was switched on at {}'.format(str(datetime.now()))
        send_pushbullet(alert, message)
        #relay_off(Relay1)
        # TODO: Configure relay via Arduino

    def tv_Off(self):
        alert = 'TV Proximity Notification'
        message = 'TV was switched Off at {}'.format(str(datetime.now()))
        #print (message)
        #relay_on(Relay1)
        send_pushbullet(alert, message)
        if LOGGER is not None:
            LOGGER.info('Someone was too close to the TV and TV was switched off.')
        # TODO: Configure relay via Arduino

    def distance(self):
        """
        Gets distance in Centimeter and returns it.
        :return: Float
        """
        samples = []

        for i in xrange(self.sample_size):
            time.sleep(self.sleep_time)
            _distance = float(subprocess.Popen(
                'sudo /home/pi/Scripts/TV_Proximity_Sensor/proximity_sensor',
                shell=True, stdout=subprocess.PIPE, ).communicate()[0])
            #print 'X:',_distance
            samples.append(_distance)
        return np.average(samples)

    def run(self):
        """
        :type self: None
        """
        count = 0
        tvoff = False
        while True:
            if self.distance() <= self._threshold:
                count += 1
                if count == 2:
                    if self.notification(notify=True):
                        count += 1
                elif count > 3:
                    self.tv_Off()
                    tvoff = True
                    count = 0
                else:
                    pass
            else:
                if tvoff:
                    self.tv_On()
                    tvoff = False
               # print 'Distance {}cm.'.format(round(self.distance()))
            time.sleep(0.01)


thread = TimerClass()
thread.run()
