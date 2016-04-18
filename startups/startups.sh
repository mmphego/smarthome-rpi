#!/bin/bash
(sleep 1; python /home/pi/Scripts/Smart_DoorBell/WaitDoorbell.py)&
(sleep 1; python /home/pi/Scripts/Temp_Relay_Cont/Indoor_Temp_Logger.py)&
(sleep 1; python /home/pi/Scripts/Website/Webserver.py)&
