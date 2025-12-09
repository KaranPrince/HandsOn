# Use official Python slim image
FROM python:3.11-slim

# create app directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose port (documentational)
EXPOSE 5000

# Start command
CMD ["python", "app.py"]
