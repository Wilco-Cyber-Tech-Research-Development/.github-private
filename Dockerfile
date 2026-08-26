# ============================================================
# COSMICA ULTRA HYPER-AGI
# Dockerfile
# ============================================================

FROM python:3.11-slim

# ------------------------------------------------------------
# Runtime configuration
# ------------------------------------------------------------

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Engine home and data directories
ENV COSMICA_HOME=/app
ENV COSMICA_CONFIG=/app/config
ENV COSMICA_DATA=/app/data
ENV COSMICA_MEMORY=/app/memory
ENV COSMICA_MODELS=/app/models
ENV COSMICA_LOGS=/app/logs

# Optional: increase TensorFlow logging level if needed
# ENV TF_CPP_MIN_LOG_LEVEL=2

WORKDIR /app

# ------------------------------------------------------------
# System dependencies
# ------------------------------------------------------------

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    git \
    curl \
    ca-certificates \
    libglib2.0-0 \
    libgomp1 \
    libstdc++6 \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# Python dependencies
# ------------------------------------------------------------

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# ------------------------------------------------------------
# Application source
# ------------------------------------------------------------

COPY . /app

# ------------------------------------------------------------
# Runtime directories
# ------------------------------------------------------------

RUN mkdir -p \
    /app/config \
    /app/data \
    /app/memory \
    /app/models \
    /app/logs

# ------------------------------------------------------------
# Non‑root runtime user
# ------------------------------------------------------------

RUN useradd \
    --create-home \
    --shell /bin/bash \
    cosmica

RUN chown -R cosmica:cosmica /app

USER cosmica

# ------------------------------------------------------------
# Health check (verifies the engine can report status)
# ------------------------------------------------------------

HEALTHCHECK \
    --interval=30s \
    --timeout=10s \
    --start-period=60s \
    --retries=3 \
    CMD python main.py --status || exit 1

# ------------------------------------------------------------
# Default command – run the Ultra Hyper-AGI engine
# ------------------------------------------------------------

CMD ["python", "main.py"]