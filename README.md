# Raspberry Pi Smart Home Automation Project

This repository contains everything to do with my BTech project that I submitted in 2016 at the Tshwane University of Technology while based in Cape Town.

I have also added my thesis which will give you a more detailed overview of what this repository is all about.

Thesis titled: [Designing A Smart Home Automation With Voice Recognition Using Raspberry Pi And Arduino](Thesis.pdf)


## Usage [archive/deprecated]
Not sure the usage anymore but ideally one would copy all files into `/home/pi`. Update `Backup_configs/wpa_supplicant.conf` with your WiFi connections and move all files to `/etc`

```
sudo apt-get install $(grep -vE "^\s*#" Apts/apt-build-requirements.txt | tr "\n" " ")
sudo pip insrall -r Apts/pip-build-requirements.txt
```

Alternatively, checkout `Scripts` directory and mangle around.
Note: This code is over 4 yrs old as of 12/2019

## Demo

About a year ago I blogged about the project due to the amount of hits I received I then decided why not upload this on my GitHub (Who knows maybe someone might find this stuff useful), I've listed the content of the blog post below. Alternatively you can click [here](https://blog.mphomphego.co.za/blog/2018/06/13/Smart-Home-Automation-Project-Using-A-Raspberry-Pi.html)

### [Project] Smart Home Automation using Raspberry Pi and Arduino

About 2 years ago, as part of my requirement to obtain my degree I came up, designed and development a project titled: [Smart Home Automation using Raspberry Pi and Arduino](https://goo.gl/yuYdRq) and fortunately enough I made a demo about it.

[Youtube Playlist](https://goo.gl/yuYdRq)

## 1. Some Intro + Smart Alarm

*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/visOkFoL3eo/1.jpg)](http://www.youtube.com/watch?v=visOkFoL3eo "")

## 2. Android Application Control

*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/EACmoIVu0B8/1.jpg)](https://www.youtube.com/embed/EACmoIVu0B8 "")

## 3. Android Gesture Control

[Update: 26/11/19] This was one the coolest feature I came up with, and referenced these papers.

- [Detecting Falls Using Accelerometers by Adaptive Thresholds in Mobile Devices](http://www.jcomputers.us/vol9/jcp0907-07.pdf)
- [Detecting User Activities using the Accelerometer on Android Smartphones](https://ptolemy.berkeley.edu/projects/truststc/education/reu/10/Papers/DasGreenPerezMurphy_Paper.pdf)

*I guess more text should go here to explain whatever is going on!!!*


[![](http://img.youtube.com/vi/QxTiL1fr8xY/1.jpg)](https://www.youtube.com/embed/QxTiL1fr8xY)

## 4. [Somewhat] Web Interface

*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/qj6tPWBQvXs/1.jpg)](https://www.youtube.com/embed/qj6tPWBQvXs)

## 5. Presence Detector using IP Sniffing

*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/85OM4R5eAa4/1.jpg)](https://www.youtube.com/embed/85OM4R5eAa4)

## 6. TV Proximity Detector

*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/AR9MUh2L1uY/1.jpg)](https://www.youtube.com/embed/AR9MUh2L1uY)

## 7. Smart Doorbell

*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/s6tBE6cGTYk/1.jpg)](https://www.youtube.com/embed/s6tBE6cGTYk)

# Additional Features [Amazon Echo/Alexa]

Including interfacing [Amazon's Alexa](https://en.wikipedia.org/wiki/Amazon_Alexa) running on a Raspberry Pi.

## 1. Interfacing DHT11 via ESP8266 to Amazon Alexa

[![](http://img.youtube.com/vi/Rpn-UgJLBdY/1.jpg)](https://www.youtube.com/embed/Rpn-UgJLBdY)

## 2. Amazon Alexa Skill - Intro
*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/nqD50LRBTbE/1.jpg)](https://www.youtube.com/embed/nqD50LRBTbE)

## 3. Amazon Alexa Skill - About Homely
*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/70d2L8aHXzU/1.jpg)](https://www.youtube.com/embed/70d2L8aHXzU)

## 4. Amazon Alexa Skill - News Retrieval
*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/T59mvy_dyEc/1.jpg)](https://www.youtube.com/embed/T59mvy_dyEc)

## 5. TV Ambient Lighting
*I guess more text should go here to explain whatever is going on!!!*

[![](http://img.youtube.com/vi/O9x91SrcjoE/1.jpg)](https://www.youtube.com/embed/O9x91SrcjoE)

---------------------------------------

*I will try to detail the design and etc on another post - soon.*

All code is available, just drop me a mail. I have been procrastinating on hosting the code to [GitHub](https://github.com/mmphego/smarthome-rpi).

# Donations/Thanks

If you like this and want to buy me a cup of coffee/beef/bottled water, Here's my paypal link: https://paypal.me/mmphego ☕

Also you can click if you'd like to [saythanks](https://saythanks.io/to/mmphego)... :) else *Star* it.
