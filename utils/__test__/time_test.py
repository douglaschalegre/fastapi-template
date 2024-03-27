'''Test time functions'''
from utils.time import seconds_to_formated_hours


def test_seconds_to_formated_hours():
    ''''Test seconds_to_formated_hours'''
    minute = 60
    hour = 60 * minute
    time = seconds_to_formated_hours(hour+minute+30)
    assert time == '01:01:30'
