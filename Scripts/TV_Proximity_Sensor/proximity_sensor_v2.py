import os
import time
import subprocess
import multiprocessing
import numpy as np

#import lirc
"""
USAGE: Create ~/.lircrc and copy below code
begin
    prog = irexec
    button = KEY_1
    config = echo "You pressed one"
    repeat = 0
end
"""
#try:
    #from logger import LOGGER
#except Exception as e:
    #print 'Failed due to {}'.format(e)

class TimerClass(object):
    def __init__(self):
        self.sleep_time = 1
        self._threshold = 20.
        self.sample_size = 3
        #self.infrared = lirc.init('irexec')

    def notification(self):
        """
        This will sound a siren or notification to move away
        :return: <nothing>
        """
        #os.system('mpg123 close_to_tv.mp3')
        print 'Warning: Too close to the TV: {} cm.'.format(self.distance())
        #LOGGER.info('Someone was close to the TV.')
        pass

    def tv_On(self):
        print ('TV was switched on')
        pass

    def tv_Off(self):
        print ('TV was switched off')
        pass

        # TODO: MM 2015/11/04
        # Add IR instructions to switch TV off here
        #LOGGER.info('TV was switched off')
        #LOGGER.info('TV was switched on')

        #try:
            #print 'use lirc'
            #while True:
                #btn = lirc.nextcode()
                #if btn != []:
                    #print btn
        #except:
            #pass
    def distance(self, ):
        """
        Gets distance in Centimeter and returns it.
        :return: Float
        """
        samples = []
        for i in xrange(self.sample_size):
            time.sleep(0.01)
            _distance = float(subprocess.Popen(
                'sudo /home/pi/Scripts/TV_Proximity_Sensor/proximity_sensor',
                shell=True, stdout=subprocess.PIPE, ).communicate()[0])
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
                if count == 2   :
                    self.notification()
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
                #print 'Distance {}cm is fine.'.format(self.distance())
            time.sleep(self.sleep_time)

thread = TimerClass()
thread.run()
