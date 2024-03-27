'''Utils for handling time.'''
from datetime import datetime
import pytz


def seconds_to_formated_hours(seconds):
    '''Convert seconds to a formated time'''
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    formated_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    return formated_time


def now():
    '''Return current datetime with UTC 0'''
    return str(datetime.now(
        pytz.utc).isoformat())
