# Dockerfile 

FROM python:3.10-slim

WORKDIR /app

# Copy and install dependencies.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copy the application code
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
