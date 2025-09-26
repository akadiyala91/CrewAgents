import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # OpenWeatherMap API Key (optional - app works without it)
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'YOUR_API_KEY_HERE')
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
