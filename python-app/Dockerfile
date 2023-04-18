# Use the official Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app.py file into the container
COPY app.py .

# Install any dependencies required by the app.py file
# For example, if your app.py uses Flask, you can install it using pip
RUN pip install Flask

# Expose the port on which the app will run
EXPOSE 8080

# Start the app.py script when the container is run
CMD ["python", "app.py"]
