import boto3
from dotenv import load_dotenv
import os

load_dotenv()

AWS_KEY = os.getenv("aws_key")
AWS_SECRET = os.getenv("aws_secret")
BUCKET_NAME = 'anyoneai-datasets'
PREFIX = 'credit-data-2010/'
local_downloads_folder = os.path.join(os.getcwd(), "datasets")
def start_download():
    s3 = boto3.resource(
        "s3",
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET,
        region_name="us-east-1",
    )
    if(not os.path.exists(local_downloads_folder)):
        os.makedirs(local_downloads_folder, exist_ok=True)
    bucket = s3.Bucket(BUCKET_NAME)

    for obj in bucket.objects.filter(Prefix=PREFIX):
        filename = obj.key.split("/")[-1]
        if filename:  
            local_path = os.path.join(local_downloads_folder, filename)
            print(f"Descargando {obj.key} a {local_path}")
            bucket.download_file(obj.key, local_path)