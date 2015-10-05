import logging.handlers

HOST = 'localhost'
PORT = logging.handlers.DEFAULT_TCP_LOGGING_PORT

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file-debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/debug.log',
            'formatter': 'standard',
            'backupCount': 5,
            'maxBytes': 100000
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/info.log',
            'formatter': 'standard',
            'backupCount': 5,
            'maxBytes': 100000
        },
    },
    'loggers': {
        '__main__': {
            'propagate': False,
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        '': {
            'propagate': False,
            'handlers': ['console', 'file-debug'],
            'level': 'DEBUG',
        },
    }
}

