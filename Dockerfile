
# =========================
# Build Stage
# =========================

FROM python:3.9-slim AS build

# Set working directory
WORKDIR /app

# Copy application file
COPY app.py .

# Install Flask
RUN pip install --no-cache-dir flask

# =========================
# Runtime Stage
# =========================

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy installed packages from build stage
COPY --from=build /usr/local/lib/python3.9 /usr/local/lib/python3.9

# Copy application from build stage
COPY --from=build /app /app

# Expose Flask port
EXPOSE 5000

# Environment variable
ENV PYTHONUNBUFFERED=1

# Start application
CMD ["python", "app.py"]
