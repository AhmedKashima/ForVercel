from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Use PostgreSQL in production (from DATABASE_URL env var)
    # and fallback to SQLite for local development.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', r"sqlite:///./db.sqlite")
    
    # Disable verbose SQL logging in production for better performance.
    SQLALCHEMY_ECHO = os.environ.get('FLASK_ENV') != 'production'