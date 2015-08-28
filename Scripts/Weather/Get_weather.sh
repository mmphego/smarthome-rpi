#!/bin/bash
#__author__ = "Mpho Mphego"
#__description__ = "Alarm and weather notifier"
#__version__ = "$Revision: 1.4 $"
#__date__ = "$Date: 2015/01/03 02:13 $"
#__url__ = "mpho112.wordpress.com"
#__copyright__ = "Copyright (c) 2015 Mpho Mphego"
#__license__ = "Bash"

cd  /home/pi/Scripts/Weather
#echo "executed at " `date`
weather -qm fapr > .weather_before.txt
python .weather.py 
#pico2wave -w speech1.wav "`cat .intro` `date "+%A %d %B"`" 
#pico2wave -w speech2.wav "`cat .intro3``date "+%H %M"`" 
#pico2wave -w speech3.wav "`cat .intro2` `cat .weather_after.txt`" 
#echo "Playing wav file"
#aplay speech1.wav speech2.wav speech3.wav
#rm speech1.wav speech2.wav speech3.wav
#echo "Done at " `date`
