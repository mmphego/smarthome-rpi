#!/bin/bash

#Setting up pin mode
gpio mode 4 out

ping -c 1 172.18.20.195 > /dev/null 2>&1 
if [ $? -eq 0 ]; then 
echo "Samsung Fone detected"
gpio write 4 1
#flite -t "Welcome to the SANSA Office"
#sudo service cellDetect stop

else 
echo "Samsung Fone NOT detected"
gpio write 4 0
fi
