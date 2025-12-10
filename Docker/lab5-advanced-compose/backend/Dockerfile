FROM python:3.11-slim

WORKDIR /app

# minimal system deps for SSL/requests
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

# Healthcheck implemented in image (Python) so it works across platforms
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import sys,urllib.request; \
    req=urllib.request.Request('http://127.0.0.1:5000/api/hello'); \
    import socket; \
    try: r=urllib.request.urlopen(req, timeout=2); sys.exit(0 if r.getcode()==200 else 1) \
    except Exception: sys.exit(1)"

CMD ["python", "app.py"]
