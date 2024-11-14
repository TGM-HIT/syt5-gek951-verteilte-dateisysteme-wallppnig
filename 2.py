from minio import Minio
from dotenv import load_dotenv
import os


load_dotenv()
LOCAL_FILE_PATH = ""
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
BUCKET_NAME = "bucket"
MINIO_API_HOST = "http://localhost:9000"
MINIO_CLIENT = Minio("localhost:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

def main():
    found = MINIO_CLIENT.bucket_exists(BUCKET_NAME)
    if not found:
        print("ERROR: Bucket not found!!!")
        return

    print("Bucket found")

    MINIO_CLIENT.fput_object(BUCKET_NAME, "requirements.txt", LOCAL_FILE_PATH)
    print("It is successfully uploaded to bucket")


main()
