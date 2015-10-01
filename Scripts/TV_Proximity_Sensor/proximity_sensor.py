import threading
import subprocess
from logger import LOGGER
try:
    import hcsr04sensor.sensor as sensor
except ImportError:
    import pip
    pip.main(['install', 'hcsr04sensor'])


class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.an_event = threading.Event()
        self._threshold = 20.0
        self._trig_pin = 20
        self._echo_pin = 21
        self._unit = 'metric'  # choices (metric or imperial)
        self._temperature = 20  # Celcius for metric, Fahrenheit for imperial
        self._round_to = 1  # report a cleaner rounded output.

    def notification()
        """
        This will sound a siren or notification to move away
        :return: <nothing>
        """
        print 'Notified'
        Logger.info('Someone was close to the TV.')

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
        while not self.an_event.is_set():
            if self.distance() <= self._threshold:
                print 'Distance {} is fine.'.format(self.distance())
            else:
                print 'Ring notification.'
            self.an_event.wait(.5)

thread = TimerClass()
thread.start()
