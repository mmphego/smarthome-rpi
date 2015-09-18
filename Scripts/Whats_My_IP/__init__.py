import logging

def _logging():
    """
    Tracking events that happen when some software runs
    """
    # create logger
    LOGGER = logging.getLogger('WhatsMy IP Logger')
    LOGGER.setLevel(logging.DEBUG) # log all escalated at and above DEBUG

    fh = logging.FileHandler('IP_Logger.csv')
    fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

    # create a formatter and set the formatter for the handler.
    frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    fh.setFormatter(frmt)

    # add the Handler to the logger
    LOGGER.addHandler(fh)