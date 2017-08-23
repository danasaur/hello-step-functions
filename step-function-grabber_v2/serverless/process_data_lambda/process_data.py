"""convert timezones and put into a dataframe"""
from datetime import datetime, timedelta
from dateutil import tz
import pandas as pd


def convert_time(time_string):
    """
    a helper function for process_data which converts the time from UTC
    to Minnesota time
    """
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/Chicago')
    datetime_object = datetime.strptime(time_string, '%I:%M:%S %p')

    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    utc = datetime_object.replace(tzinfo=from_zone)

    # Convert time zone
    local = utc.astimezone(to_zone)

    # add an hour for daylight savings time because it's summer time
    # TO DO: check if it's summer
    summer_local = local + timedelta(hours=1)

    # get local time string
    local_time_string = summer_local.time().strftime("%H:%M:%S")
    return local_time_string


def process_data(event, context):
    """
    convert data to local time
    return event including a pandas data object
    """
    time_now = datetime.now().strftime("%m_%d_%Y_%H-%M-%S")
    sunrise = convert_time(event['data']['results']['sunrise'])
    sunset = convert_time(event['data']['results']['sunset'])

    data_dict = {"time_now": [time_now],
                 "sunrise": [sunrise],
                 "sunset": [sunset]}

    
    event['dataframe'] = dataframe
    event['time_now'] = time_now
    return event
