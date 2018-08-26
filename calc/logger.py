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
def create_logger(file_name):
        logger = logging.getLogger(file_name)
        logger.setLevel(logging.WARNING)
        formatter = logging.Formatter('[%(name)s: %(levelname)s]    '\
                        '%(funcName)s():%(lineno)s    ' \
                        '%(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
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
