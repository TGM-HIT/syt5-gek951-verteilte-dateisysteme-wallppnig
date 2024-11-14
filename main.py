from fastapi import FastAPI, File, UploadFile
from minio import Minio
from minio.error import S3Error
from fastapi.responses import JSONResponse
import io

app = FastAPI()

# MinIO Client-Setup
minio_client = Minio(
    "localhost:9000",  # MinIO-Service-Adresse
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False  # Setze True, wenn du HTTPS verwendest
)

BUCKET_NAME = "bucket"

# Bucket erstellen, wenn noch nicht vorhanden
# if not minio_client.bucket_exists("mybucket"):
#     minio_client.make_bucket("mybucket")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_contents = await file.read()
        minio_client.put_object(BUCKET_NAME, file.filename, io.BytesIO(file_contents), len(file_contents))
        file_url = f"http://minio-service:9000/{BUCKET_NAME}/{file.filename}"
        return {"message": "File uploaded successfully", "file_url": file_url}
    except S3Error as e:
        return JSONResponse(status_code=500, content={"message": f"Error: {str(e)}"})

@app.get("/getfile/{filename}")
async def get_file(filename: str):
    try:
        data = minio_client.get_object(BUCKET_NAME, filename)
        return JSONResponse(content={"file": data.read().decode()})
    except S3Error as e:
        return JSONResponse(status_code=404, content={"message": f"File not found: {str(e)}"})

@app.delete("/deletefile/{filename}")
async def delete_file(filename: str):
    try:
        minio_client.remove_object(BUCKET_NAME, filename)
        return {"message": f"File {filename} deleted successfully"}
    except S3Error as e:
        return JSONResponse(status_code=404, content={"message": f"File not found: {str(e)}"})
