"""write data to s3"""
import fastparquet
import pandas as pd
import s3fs


def write_data(event, context):
    """
    write data to s3 in parquet format
    """
    dataframe = event['dataframe']
    time_now = datetime.now().strftime("%m_%d_%Y_%H:%M:%S")
    s3_client = s3fs.S3FileSystem()
    s3_connection = s3_client.open
    filepath = "bigdana/{0}.parq".format(time_now)
    fastparquet.write(filepath, df, open_with=s3_connection)
    return event
