# Use an official Python base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy app code
COPY fraud_detection_app /app

# Install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Expose the API port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
