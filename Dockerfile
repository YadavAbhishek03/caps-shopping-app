# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY caps-app /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]

