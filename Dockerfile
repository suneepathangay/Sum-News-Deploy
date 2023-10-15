FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy your Flask application code into the container
COPY . /app

# Install dependencies (assuming you have a requirements.txt file)
RUN pip install -r requirements.txt

# Expose the port your Flask app is listening on
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "server.py"]