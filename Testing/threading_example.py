import time
import subprocess
from threading import Thread

def sample():
    _distance = float(subprocess.Popen(
        'sudo /home/pi/Scripts/TV_Proximity_Sensor/proximity_sensor',
        shell=True, stdout=subprocess.PIPE, ).communicate()[0])
    time.sleep(1)
    print _distance
def myfunc(i):
    print "sleeping 5 sec from thread %d" % i
    time.sleep(1)
    print "finished sleeping from thread %d" % i


for i in range(5):
    #t = Thread(target=myfunc, args=(i,))
    t = Thread(target=sample, args=())
    t.start()
