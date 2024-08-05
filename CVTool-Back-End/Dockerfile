# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000
EXPOSE 50761

# Command to run the backend service
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "50761", "--reload"]
