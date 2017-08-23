from datetime import datetime, timedelta
import json
import fastparquet
from dateutil import tz
import requests
import pandas as pd
import s3fs


def _convert_time(time_string):
    """
    a helper function for process_data which converts the time from UTC to Minnesota time
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


def get_data(event, context):
    """
    get data from an api endpoint
    return event including a json data object
    """
    response = requests.get(
    	"https://api.sunrise-sunset.org/json?lat=44.977753&lng=-93.265011&date=today")
    event['data'] = json.loads(response.content)
    return event


def process_data(event, context):
    """
    convert data to local time
    return event including a pandas data object
    """
    time_now = datetime.now().strftime("%m_%d_%Y_%H:%M:%S")
    sunrise = _convert_time(event['data']['results']['sunrise'])
    sunset = _convert_time(event['data']['results']['sunset'])

    data_dict = {"time_now": [time_now],
                 "sunrise": [sunrise],
                 "sunset": [sunset]}

    df = pd.DataFrame(data_dict)
    event['dataframe'] = df
    return event


def write_data(event, context):
    """
    write data to s3 in parquet format
    """
    df = event['dataframe']
    time_now = datetime.now().strftime("%m_%d_%Y_%H:%M:%S")
    s3 = s3fs.S3FileSystem()
    s3_connection = s3.open
    filepath = "bigdana/{0}.parq".format(time_now)
    fastparquet.write(filepath, df, open_with=s3_connection)
    return event

if __name__ == "__main__":
    event = {}
    context = {}
    event = get_data(event, context)
    event = process_data(event, context)
    event = write_data(event, context)