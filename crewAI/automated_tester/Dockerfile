# ============================================================
# 1. Base image with Python
# ============================================================
FROM python:3.12-slim AS base

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# ============================================================
# 2. Define entrypoint for running the Crew job
# ============================================================
ENTRYPOINT ["python", "crew.py"]
