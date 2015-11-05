import subprocess
from logger import LOGGER


def take_pic():
    """


    :rtype : None
    """
    try:
        subprocess.Popen(
            'avconv -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2  image.jpg'
            , shell=True, stdout=subprocess.PIPE, ).communicate()
    except Exception as e:
        LOGGER.error('Failed to capture the image')
        pass
