# Dockerfile 

FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

# Copy and install dependencies.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copy the application code
COPY . .


