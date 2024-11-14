# Dockerfile
FROM python:3.12

# Install any required packages here
# RUN pip install --no-cache-dir your-packages

# Copy your code or scripts into the container
# COPY . /app
WORKDIR /app

# Optional: specify the default command for the container
CMD bash -c "git clone https://github.com/TGM-HIT/syt5-gek951-verteilte-dateisysteme-wallppnig.git && \
    cd syt5-gek951-verteilte-dateisysteme-wallppnig && \
    pip install -r requirements.txt && \
    rm minio && \
    uvicorn main:app --reload"
