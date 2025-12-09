FROM python:3.11-slim

# workdir
WORKDIR /app

# minimal system deps (ca-certificates so urllib works with HTTPS if needed)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app.py .

EXPOSE 5000

# healthcheck using python urllib (no extra package)
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import sys,urllib.request; \
  req=urllib.request.Request('http://127.0.0.1:5000/api/hello'); \
  try: r=urllib.request.urlopen(req, timeout=2); sys.exit(0 if r.getcode()==200 else 1) \
  except Exception: sys.exit(1)"

CMD ["python", "app.py"]
