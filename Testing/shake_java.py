""" generated source for module test """
from __future__ import print_function
from abc import ABCMeta, abstractmethod
#
#  * Listener that detects shake gesture.
#
class ShakeEventListener(SensorEventListener):
    """ generated source for class ShakeEventListener """
    #  Minimum movement force to consider.
    MIN_FORCE = 10

    #
    #    * Minimum times in a shake gesture that the direction of movement needs to
    #    * change.
    #
    MIN_DIRECTION_CHANGE = 3

    #  Maximum pause between movements.
    MAX_PAUSE_BETHWEEN_DIRECTION_CHANGE = 200

    #  Maximum allowed time for shake gesture.
    MAX_TOTAL_DURATION_OF_SHAKE = 400

    #  Time when the gesture started.
    mFirstDirectionChangeTime = 0

    #  Time when the last movement started.
    mLastDirectionChangeTime = long()

    #  How many movements are considered so far.
    mDirectionChangeCount = 0

    #  The last x position.
    lastX = 0

    #  The last y position.
    lastY = 0

    #  The last z position.
    lastZ = 0

    #  OnShakeListener that is called when shake is detected.
    mShakeListener = None

    #
    #    * Interface for shake gesture.
    #
    class OnShakeListener(object):
        """ generated source for interface OnShakeListener """
        __metaclass__ = ABCMeta
        #
        #      * Called when shake gesture is detected.
        #
        @abstractmethod
        def onShake(self):
            """ generated source for method onShake """

    def setOnShakeListener(self, listener):
        """ generated source for method setOnShakeListener """
        self.mShakeListener = listener

    def onSensorChanged(self, se):
        """ generated source for method onSensorChanged """
        #  get sensor data
        x = se.values[SensorManager.DATA_X]
        y = se.values[SensorManager.DATA_Y]
        z = se.values[SensorManager.DATA_Z]
        #  calculate movement
        totalMovement = abs(x + y + z - self.lastX - self.lastY - self.lastZ)
        if totalMovement > self.MIN_FORCE:
            #  get time
            now = System.currentTimeMillis()
            #  store first movement time
            if self.mFirstDirectionChangeTime == 0:
                self.mFirstDirectionChangeTime = now
                self.mLastDirectionChangeTime = now
            #  check if the last movement was not long ago
            lastChangeWasAgo = now - self.mLastDirectionChangeTime
            if lastChangeWasAgo < self.MAX_PAUSE_BETHWEEN_DIRECTION_CHANGE:
                #  store movement data
                self.mLastDirectionChangeTime = now
                self.mDirectionChangeCount += 1
                #  store last sensor data
                self.lastX = x
                self.lastY = y
                self.lastZ = z
                #  check how many movements are so far
                if self.mDirectionChangeCount >= self.MIN_DIRECTION_CHANGE:
                    #  check total duration
                    totalDuration = now - self.mFirstDirectionChangeTime
                    if totalDuration < self.MAX_TOTAL_DURATION_OF_SHAKE:
                        self.mShakeListener.onShake()
                        resetShakeParameters()
            else:
                resetShakeParameters()

    #
    #    * Resets the shake parameters to their default values.
    #
    def resetShakeParameters(self):
        """ generated source for method resetShakeParameters """
        self.mFirstDirectionChangeTime = 0
        self.mDirectionChangeCount = 0
        self.mLastDirectionChangeTime = 0
        self.lastX = 0
        self.lastY = 0
        self.lastZ = 0

    def onAccuracyChanged(self, sensor, accuracy):
        """ generated source for method onAccuracyChanged """
