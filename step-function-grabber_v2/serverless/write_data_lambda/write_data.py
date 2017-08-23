import fastparquet
import pandas as pd
import s3fs

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