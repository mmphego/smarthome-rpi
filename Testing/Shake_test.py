""" generated source for module test """
from __future__ import print_function
from abc import ABCMeta, abstractmethod

class ShakeEventListener(SensorEventListener):
    """ generated source for class ShakeEventListener """
    SHAKE_LIMIT = 15
    LITTLE_SHAKE_LIMIT = 5
    mSensorManager = None
    mAccel = 0.00
    mAccelCurrent = SensorManager.GRAVITY_EARTH
    mAccelLast = SensorManager.GRAVITY_EARTH
    listener = None

    class ShakeListener(object):
        """ generated source for interface ShakeListener """
        __metaclass__ = ABCMeta
        @abstractmethod
        def onShake(self):
            """ generated source for method onShake """

        @abstractmethod
        def onLittleShake(self):
            """ generated source for method onLittleShake """

    @overloaded
    def __init__(self, l):
        """ generated source for method __init__ """
        super(ShakeEventListener, self).__init__()
        a = l
        self.mSensorManager = a.getSystemService(Context.SENSOR_SERVICE)
        self.listener = l
        registerListener()

    @__init__.register(object, Activity, self.ShakeListener)
    def __init___0(self, a, l):
        """ generated source for method __init___0 """
        super(ShakeEventListener, self).__init__()
        self.mSensorManager = a.getSystemService(Context.SENSOR_SERVICE)
        self.listener = l
        registerListener()

    def registerListener(self):
        """ generated source for method registerListener """
        self.mSensorManager.registerListener(self, self.mSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER), SensorManager.SENSOR_DELAY_NORMAL)

    def unregisterListener(self):
        """ generated source for method unregisterListener """
        self.mSensorManager.unregisterListener(self)

    def onSensorChanged(self, se):
        """ generated source for method onSensorChanged """
        x = se.values[0]
        y = se.values[1]
        z = se.values[2]
        self.mAccelLast = self.mAccelCurrent
        self.mAccelCurrent = float(Floatsqrt(x * x + y * y + z * z))
        delta = self.mAccelCurrent - self.mAccelLast
        self.mAccel = self.mAccel * 0.9 + delta
        if self.mAccel > self.SHAKE_LIMIT:
            self.listener.onShake()
        elif self.mAccel > self.LITTLE_SHAKE_LIMIT:
            self.listener.onLittleShake()

    def onAccuracyChanged(self, sensor, accuracy):
        """ generated source for method onAccuracyChanged """
