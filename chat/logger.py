#!/usr/bin/python3
import logging

#
# Logger
#
class Logger(object):
    #
    # Ctor
    #
    def __init__(self, log_name):
        # TODO
        pass

#
# Createa a logger with a given file_name
#
def create_logger(file_name, log_file=None):

    logger = logging.getLogger(file_name)
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('[%(name)s: %(levelname)s]    '\
                    '%(funcName)s():%(lineno)s    ' \
                    '%(message)s')
    if log_file == None:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
    else:
        if len(log_file) > 0:
            handler = logging.FileHandler(log_file)
            handler.setFormatter(formatter)
        else:
            raise Exception("Log file name is 0 length.")


    logger.addHandler(handler)
    return logger


#
# Main
#
def main():
    pass

#
# Module check
#
if __name__ == "__main__":
    main()
