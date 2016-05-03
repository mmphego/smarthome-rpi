__author__ = 'mmphego'
from os import path, environ
import yaml


def configFile():
    if 'CONFIGFILE' in environ.keys():
        config_link = environ['CONFIGFILE']
        if path.isfile(config_link):
            with open(config_link) as ymlfile:
                cfg = yaml.load(ymlfile)
    else:
        config_link = '/home/pi/config/config.yml'
        if path.isfile(config_link):
            with open(config_link) as ymlfile:
                cfg = yaml.load(ymlfile)
    return cfg
