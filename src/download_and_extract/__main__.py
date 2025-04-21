import boto3
from dotenv import load_dotenv
import os

from download_files import download_files
from extract_zip_files import extract_files

load_dotenv()

AWS_KEY = os.getenv("aws_key")
AWS_SECRET = os.getenv("aws_secret")
BUCKET_NAME = 'anyoneai-datasets'
PREFIX = 'credit-data-2010/'
local_downloads_folder = os.path.join(os.getcwd(), "datasets")

if __name__ == "__main__":
    download_files()
    extract_files()
