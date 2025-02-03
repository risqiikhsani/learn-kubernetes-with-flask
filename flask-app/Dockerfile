# # Use a lightweight Python image
# FROM python:3.9-slim

# # Set the working directory
# WORKDIR /app

# # Copy the application files
# COPY . .

# # Install dependencies
# RUN pip install -r requirements.txt

# # Expose the port the Flask app runs on
# EXPOSE 5000

# # Run the Flask app
# CMD ["python", "app.py"]

# Use a lightweight Python image
FROM python:3.9-slim

# Set up environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
