#!/bin/bash
#__author__ = "Mpho Mphego"
#__description__ = "Graphite System Autostart"
#__version__ = "$Revision: 1.0 $"
#__date__ = "$Date: 2015/01/17 12:11 $"
#__url__ = "mpho112.wordpress.com"
#__copyright__ = "Copyright (c) 2015 Mpho Mphego"
#__license__ = "Bash"

sleep 1m
screen -dmS graphite bash -c 'cd /opt/graphite; 
sudo rm /opt/graphite/storage/carbon-cache-a.pid ;
sudo ./bin/carbon-cache.py start;
sudo PYTHONPATH=/opt/graphite/whisper ./bin/run-graphite-devel-server.py --libs=/opt/graphite/webapp/ /opt/graphite/; exec bash'
bash /home/pi/DataCrawler/sysCrawler &
sudo python /home/pi/Scripts/Smart_DoorBell/WaitDoorbell.py &
sudo python /home/pi/Scripts/ClosetDoorWarning/WaitClosetDoor.py &
