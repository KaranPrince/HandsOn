# 1. Base Image: Start from an official image (e.g., Python)
FROM python:3.9-slim
# 2. Working Directory: Set the context for subsequent commands
WORKDIR /app
# 3. Copy Files: Move your application code into the image
COPY requirements.txt .
COPY . .
# 4. Install Dependencies: Use RUN to execute commands like pip install
RUN pip install --no-cache-dir -r requirements.txt
# 5. Expose Port: Inform Docker which port your app listens on
EXPOSE 8000
# 6. Command: Define the command to run when the container starts
CMD ["python", "app.py"]
