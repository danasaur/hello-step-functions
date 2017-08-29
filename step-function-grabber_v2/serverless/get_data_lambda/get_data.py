"""get data from the sunrise-sunset api"""
import json
import requests


def get_data(event, context):
    """
    get data from an api endpoint
    return event including a json data object
    """
    response = requests.get(
        "https://api.sunrise-sunset.org/json?lat=44.977753&lng=-93.265011&date=today")
    event['data'] = json.loads(response.content)
    event['status'] = response.status_code
    return event
