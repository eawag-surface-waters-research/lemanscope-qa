import json
import boto3
import requests
from datetime import datetime, timezone

def download_metadata():
    response = requests.get(
        "https://www.eyeonwater.org/api/observations?period=120&offset=0&limit=10000&sort=desc&bbox=46.20%2C6.14%2C46.53%2C6.94&bboxVersion=1.3.0")
    if response.status_code == 200:
        data = response.json()
    else:
        raise ValueError("Failed to collect Eye on Water data")
    return data

def upload_metadata(data, bucket, aws_access_key_id, aws_secret_access_key):
    s3 = boto3.client("s3",
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    s3.put_object(
        Body=json.dumps({"time": maximum_datetime(data), "data": data}),
        Bucket=bucket,
        Key='lemanscope/data.json'
    )

def maximum_datetime(data):
    max_dt = datetime(1, 1, 1, tzinfo=timezone.utc)
    for obs in data:
        dt = datetime.strptime(obs["image"]["date_photo"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        if dt > max_dt:
            max_dt = dt
    return max_dt.isoformat()