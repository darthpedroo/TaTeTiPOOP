# Use the official Python image with the desired version
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first (optional, create this if necessary)
COPY requirements.txt .

# Install any necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the default command to run the main.py script
CMD ["python", "main.py"]
