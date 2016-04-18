import os
import time
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

try:
    import hcsr04sensor.sensor as sensor
except ImportError:
    import pip
    pip.main(['install', 'hcsr04sensor'])

BAUD = 9600
class TimerClass(object):
    def __init__(self):
        self._threshold = 20.0
        self._trig_pin = 20
        self._echo_pin = 21
        self._unit = 'metric'  # choices (metric or imperial)
        self._temperature = 20  # Celcius for metric, Fahrenheit for imperial
        self._round_to = 1  # report a cleaner rounded output.
        #self.infrared = lirc.init('irexec')

    def notification(self):
        """
        This will sound a siren or notification to move away
        :return: <nothing>
        """
        #os.system('mpg123 close_to_tv.mp3')
        #print 'Warning: Too close to the TV: {} cm.'.format(self.distance())
        #LOGGER.info('Someone was close to the TV.')
        pass

    def tv_On(self):
        #print ('TV was switched on')
        pass

    def tv_Off(self):
        #print ('TV was switched off')
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
    def distance(self):
        """
        Gets distance in Centimeter and returns it.
        :return: Float
        """
        #  Create a distance reading with the hcsr04 sensor module
        value = sensor.Measurement(self._trig_pin, self._echo_pin,
                                   self._temperature, self._unit,
                                   self._round_to)
        raw_measurement = value.raw_distance()

        # Calculate and return the distance in centimeters
        return value.distance_metric(raw_measurement)

    def run(self):
        """
        :type self: None
        """
        count = 0
        tvoff = False
        while True:
            time.sleep(.05)
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


thread = TimerClass()
thread.run()
