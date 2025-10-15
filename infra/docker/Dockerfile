FROM python:3.11-slim

# System packages sometimes needed for building wheels or SSL/certificates
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential curl ca-certificates git \
    && rm -rf /var/lib/apt/lists/*

# Faster, cleaner Python installs
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install Python deps via pip using the exported requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# Copy app source last for better caching
COPY . .

EXPOSE 8000
CMD ["uvicorn","apps.api.main:app","--host","0.0.0.0","--port","8000"]
