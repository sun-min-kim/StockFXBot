# Official python runtime as parent image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file and .env file and installs dependencies
COPY requirements.txt .

COPY .env /app/.env

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy rest of code into container
COPY . .

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Command to run bot
CMD ["python3", "bot_loop.py"]
