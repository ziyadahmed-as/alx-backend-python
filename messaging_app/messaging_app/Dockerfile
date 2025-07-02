# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port your app runs on (change if needed)
EXPOSE 8000

# Run Django app (adjust for your app start command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
