# Dockerfile
FROM python:3.12

# Install any required packages here
# RUN pip install --no-cache-dir your-packages

# Copy your code or scripts into the container
# COPY . /app
WORKDIR /app

# Optional: specify the default command for the container
CMD bash -c "wget https://dl.min.io/server/minio/release/linux-arm64/minio && \
    chmod +x minio && \
    mv minio /usr/local/bin/ && \
    mkdir minio_folder && \
    minio server minio_folder"
