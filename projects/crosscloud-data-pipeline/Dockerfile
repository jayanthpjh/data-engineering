FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       git \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first for Docker layer caching
COPY requirements.txt ./

RUN python -m pip install --upgrade pip setuptools wheel

# Prefer binary wheels to avoid building heavy C extensions from source
RUN pip install --prefer-binary -r requirements.txt

# Copy the rest of the project
COPY . /app

# Default command runs a quick smoke generator to validate the environment
CMD ["python", "src/generator.py"]
