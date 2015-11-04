import os
import time
from logger import LOGGER

try:
    import hcsr04sensor.sensor as sensor
except ImportError:
    import pip

    pip.main(['install', 'hcsr04sensor'])


class TimerClass(object):
    def __init__(self):
        self._threshold = 20.0
        self._trig_pin = 20
        self._echo_pin = 21
        self._unit = 'metric'  # choices (metric or imperial)
        self._temperature = 20  # Celcius for metric, Fahrenheit for imperial
        self._round_to = 1  # report a cleaner rounded output.

    def notification(self):
        """
        This will sound a siren or notification to move away
        :return: <nothing>
        """
        os.system('mpg123 close_to_tv.mp3')
        LOGGER.info('Someone was close to the TV.')


    def tv_Off(self):
        # TODO: MM 2015/11/04
        # Add IR instructions to switch TV off here
        LOGGER.info('TV was switched off')


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
        self.count = 0
        while True:
            if self.distance() <= self._threshold:
                print 'Too close to the TV: {} cm.'.format(self.distance())
                self.count += 1
                if self.count == 3:
                    self.notification()

                elif self.count > 3:
                    self.tv_Off()
                    self.count = 0
                else :
                    pass

            else:
                print 'Distance {}cm is fine.'.format(self.distance())


thread = TimerClass()
thread.run()
