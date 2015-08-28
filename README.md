HomeAutoPi
# RPi_Home_Directory

Installation:
Do the normal
    sudo python setup.py install

Usage:
        sudo apt-get install $(grep -vE "^\s*#" apt-build-requirements.txt | tr "\n" " ")
        sudo pip insrall -r pip-build-requirements.txt
