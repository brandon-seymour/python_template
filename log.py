import logging
from logging.handlers import RotatingFileHandler

def debug(text):
    print(text)
    logging.debug('%s %s' % ('[DEBUG]', text))

def info(text):
    print(text)
    logging.debug('%s %s' % ('[INFO]', text))

def init(filename='main.log'):
    log_handler = RotatingFileHandler(filename, )
    formatter = logging.Formatter(
        '%(asctime)s template [pid%(process)d]: %(message)s',
        '%b %d %H:%M:%S'
    )
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)