# ---- Base Image ----
FROM python:3.12-slim AS base

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential git && \
    rm -rf /var/lib/apt/lists/*

# Install uv (fast Python package installer / resolver)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:${PATH}"

# ---- App Layer ----
WORKDIR /app

# Copy dependency files first (for layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies exactly as locked
RUN uv sync --frozen --no-dev

# Copy the entire repo
COPY . .

# Expose a default working directory for generated tests
ENV TEST_DIR="/app/tests"

# Default command (user can override)
CMD ["python", "crew.py"]
