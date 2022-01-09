from datetime import datetime, date
import logging
from os import listdir, mkdir


# todo Need to add size check and deleting logs to prevent disk space issues
def check_logs():
    # Check for logging folder
    folder_itmes = listdir('./')
    if 'logs' not in folder_itmes:
        mkdir('./logs')

    logging.basicConfig(filename=f'./logs/{date.today()}_chores.log', level='DEBUG')

    return logging


def output(f_string, level=None):
    # Output to console
    print(f_string)

    # Check for folder and files and setup logging
    if level is not None:
        log = check_logs()

        # Write to log
        if level == 'debug':
            log.debug(f'{datetime.now()}:{f_string}')
        elif level == 'warning':
            log.warning(f'{datetime.now()}:{f_string}')
        elif level == 'error':
            log.error(f'{datetime.now()}:{f_string}')
        elif level == 'info':
            log.info(f'{datetime.now()}:{f_string}')
