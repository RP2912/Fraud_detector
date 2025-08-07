# Stage 1: Build dependencies
FROM python:3.9-slim as builder

WORKDIR /app

# Install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirement.txt

# Copy source code
COPY . .

# Stage 2: Distroless image
FROM gcr.io/distroless/python3:3.9

WORKDIR /app

# Copy installed Python packages from builder stage
COPY --from=builder /install /usr/local

# Copy app source code
COPY --from=builder /app /app

# Set the command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
