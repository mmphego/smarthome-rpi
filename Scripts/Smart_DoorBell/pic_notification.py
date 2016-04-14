import subprocess
import os
from logger import LOGGER


def take_pic():
    """


    :rtype : None
    """
    filename = '/home/pi/Scripts/Smart_DoorBell/image.jpg'
    try:
        devnull = open(os.devnull, 'rb')
        subprocess.Popen(
            'avconv -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2  {}'.format(filename)
            , shell=True, stdout=devnull, stderr=devnull ).communicate()
        devnull.close()
    except Exception as e:
        LOGGER.error('Failed to capture the image')
        pass
