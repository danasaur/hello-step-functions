"""write data to s3"""
import pandas as pd
import boto3


def write_data_to_csv(event, context):
    """
    convert data to a pandas dataframe and write to s3 as a csv file
    """

    # get the s3 bucket name from the event
    s3_bucket_name = event['s3_bucket_name']

    # get the data dictionary from the json event
    data_dict = event['data_dict']

    # get the current time so we can save the document with a timestamp
    time_now = event['time_now']
    filename = "{0}.csv".format(time_now)

    # convert to a pandas dataframe
    dataframe = pd.DataFrame(data_dict)
    dataframe.to_csv(filename, index=False)

    # Upload a new file
    s3 = boto3.resource('s3')
    data = open(filename, 'rb')
    s3.Bucket(s3_bucket_name).put_object(
        Key=filename,
        Body=data)

    return event

if __name__ == "__main__":
    event = {
        "s3_bucket_name": "bigdana",
        "data_dict": {
            'sunset': [5],
            'sunrise': [6]
            },
        "time_now": "08_23_2017_14-26-00"
        }
    context = {}

    write_data_to_csv(event, context)