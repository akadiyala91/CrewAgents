#!/usr/bin/env python3
"""
CrewAI Weather & Math Assistant
Startup script for the web application
"""

import os
import sys
from app import app

if __name__ == '__main__':
    # Check if OpenWeatherMap API key is set (optional)
    if os.getenv('OPENWEATHER_API_KEY') == 'YOUR_API_KEY_HERE' or not os.getenv('OPENWEATHER_API_KEY'):
        print("⚠️  INFO: OpenWeatherMap API key not set.")
        print("Weather queries will return demo responses.")
        print("To get real weather data:")
        print("1. Get a free API key from: https://openweathermap.org/api")
        print("2. Set it as: OPENWEATHER_API_KEY=your_api_key_here")
        print("3. Or create a .env file with: OPENWEATHER_API_KEY=your_api_key_here")
        print("\nThe application will work without it - math features are fully functional!")
        print("-" * 60)
    
    print("🚀 Starting CrewAI Weather & Math Assistant...")
    print("📱 Web interface will be available at: http://localhost:8080")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)
