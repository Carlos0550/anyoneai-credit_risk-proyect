import boto3
from dotenv import load_dotenv
import os

load_dotenv()

AWS_KEY = os.getenv("aws_key")
AWS_SECRET = os.getenv("aws_secret")
BUCKET_NAME = 'anyoneai-datasets'
PREFIX = 'credit-data-2010/'
local_downloads_folder = os.path.join(os.getcwd(), "datasets")
os.makedirs(local_downloads_folder, exist_ok=True)
def download_files():
    s3 = boto3.resource(
        "s3",
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET,
        region_name="us-east-1",
    )

    bucket = s3.Bucket(BUCKET_NAME)
    print(bucket)
    for obj in bucket.objects.filter(Prefix=PREFIX):
        filename = obj.key.split("/")[-1]
        if filename:  
            local_path = os.path.join(local_downloads_folder, filename)
            print(f"Descargando {obj.key} a {local_path}")
            bucket.download_file(obj.key, local_path)

    print("Descarga completada.")

def extract_files():
    extracted_folder = os.path.join(os.getcwd(), "datasets", "extracted")
    os.makedirs(extracted_folder, exist_ok=True) 

    for filename in os.listdir(local_downloads_folder):
        if filename.endswith(".zip"):
            print(f"Extrayendo {filename}")
            zip_path = os.path.join(local_downloads_folder, filename)
            os.system(f'unzip -o "{zip_path}" -d "{extracted_folder}"')  
            os.remove(os.path.join(local_downloads_folder, filename))
if __name__ == "__main__":
    download_files()
    extract_files()
