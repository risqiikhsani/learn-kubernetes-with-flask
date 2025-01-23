from flask import Flask
import os
from dotenv import load_dotenv

import socket

# Load .env file
load_dotenv()

app = Flask(__name__)
# Read environment variables set by ConfigMap and Secret
FLASK_ENV = os.getenv('FLASK_ENV', 'development')  # Default to 'development' if not set
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'  # Convert to boolean
DATABASE_URL = os.getenv('DATABASE_URL')
DB_PASSWORD = os.getenv('DB_PASSWORD')
API_KEY = os.getenv('API_KEY')

@app.route("/")
def home():
    print("Home is accessed")
        # Getting the container's IP address
    container_ip = socket.gethostbyname(socket.gethostname())
    return f"""Connected to database: {DATABASE_URL}.
    Container IP: {container_ip}.
    FLASK_ENV: {FLASK_ENV},DEBUG: {DEBUG}, DB_PASSWORD: {DB_PASSWORD}, API_KEY: {API_KEY}"""

@app.route("/kitten")
def kitten():
    print("kitten is accessed")
    return "kitten"

@app.route("/cat")
def cat():
    print("Cat is accessed")
    return "Cat"

@app.route("/health")
def health():
    print("Health is accessed")
    return "OK"

@app.route("/version")
def version():
    print("Version is accessed")
    return "1.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
