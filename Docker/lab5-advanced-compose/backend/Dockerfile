FROM python:3.11-slim

WORKDIR /app

# Install wget and ca-certificates for healthcheck and SSL
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
