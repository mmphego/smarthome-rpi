__author__ = 'mmphego'

import logging


# create logger
LOGGER = logging.getLogger('Weather Forecast Logger')
LOGGER.setLevel(logging.DEBUG) # log all escalated at and above DEBUG

fh = logging.FileHandler('Weather_Logger.csv')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)

# add the Handler to the logger
LOGGER.addHandler(fh)
