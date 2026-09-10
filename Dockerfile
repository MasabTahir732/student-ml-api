# Explicit base image tag (avoiding python:latest)
FROM python:3.10-slim

# Set non-root working directory
WORKDIR /app

# Optimize build caching by copying dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose internal listening port
EXPOSE 5000

# Run API server
CMD ["python", "app.py"]
