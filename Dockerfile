FROM python:3.9

WORKDIR /app

# Copy application code
COPY fraud_detection_app/ /app/

# Copy model folder to the exact location expected by code
COPY fraud_detection_app/app/model /app/model

# Install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
