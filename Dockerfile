# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if any are needed for your specific packages)
# For now, slim is usually sufficient, but we might need build-essential for some libs
# RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for the app
EXPOSE 8000

# Define environment variables (Can be overridden by docker-compose or .env)
# We set python to run in unbuffered mode so logs show up immediately
ENV PYTHONUNBUFFERED=1

# Run the application
# We use the array form for safer signal handling
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
