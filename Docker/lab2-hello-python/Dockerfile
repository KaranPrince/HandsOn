# Step 1: Base OS
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy dependencies file
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the application
COPY app.py .

# Step 6: Expose port
EXPOSE 5000

# Step 7: Set the default command
CMD ["python", "app.py"]
