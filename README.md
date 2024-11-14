To get the minio executable for arm

```
curl -O https://dl.min.io/server/minio/release/darwin-arm64/minio
chmod +x ./minio
```

To start the minio server
```
minio server minio_folder
```

To access the minio server (standard credentials)
```
minioadmin
minioadmin
```

To run the CRUD fastapi python webserver
```
uvicorn main:app --reload
```
