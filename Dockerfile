# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies (if you have any requirements)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on (if needed, this is just an example)
EXPOSE 8080

# Run the Python script when the container starts
CMD ["python", "hangman.py"]
