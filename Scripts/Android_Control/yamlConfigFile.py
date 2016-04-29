__author__ = 'mmphego'
import yaml
import os
def configFile():
    if 'CONFIGFILE' in os.environ.keys():
        config_link = os.environ['CONFIGFILE']
        if os.path.isfile(config_link):
            with open(config_link) as ymlfile:
                cfg = yaml.load(ymlfile)
    else:
        config_link = '/home/pi/config/config.yml'
        if os.path.isfile(config_link):
            with open(config_link) as ymlfile:
                cfg = yaml.load(ymlfile)
    return cfg
