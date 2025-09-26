# Weather & Math Assistant

A professional web interface that provides intelligent weather information and smart math calculations with automatic query routing.

## Features

- **Smart Query Routing**: Automatically routes weather queries to Weather functions and math queries to Math functions
- **Weather Information**: Fetches current weather data from OpenWeatherMap API (optional - works without API key)
- **Advanced Math Operations**: Performs calculations, solves expressions, generates word problems
- **Modern Web Interface**: Clean, responsive design with real-time feedback
- **Agent Status Monitoring**: Visual indicators showing which function is active
- **Quick Actions**: Pre-defined buttons for common queries
- **No AI Dependencies**: Works completely offline without external AI APIs

## Architecture

The application consists of:

1. **Simple Python Backend**: Lightweight functions with smart keyword-based routing
2. **Flask Web Server**: RESTful API for handling requests
3. **Modern Frontend**: Responsive web interface with JavaScript
4. **Function System**:
   - **Smart Router**: Routes queries based on keywords
   - **Weather Functions**: Fetches weather data from OpenWeatherMap
   - **Math Functions**: Performs calculations, expressions, and word problems

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (get yours at [platform.openai.com](https://platform.openai.com/api-keys))
- OpenWeatherMap API key (free at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/akadiyala91/CrewAgents.git
   cd CrewAgents
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```bash
   # OpenAI API Key (Required for AI agents)
   OPENAI_API_KEY=your_openai_api_key_here
   
   # OpenWeatherMap API Key (Required for weather functionality)
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   
   # Flask Configuration
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

### Web Interface

1. **Ask Questions**: Type natural language queries in the input field
   - Weather queries: "What's the weather in London?", "Temperature in Paris"
   - Math queries: "Calculate something random", "Give me a math problem"

2. **Quick Actions**: Use the pre-defined buttons for common queries

3. **View Results**: See responses with agent attribution and timestamps

### API Endpoints

- `POST /api/query` - Main query endpoint
- `GET /api/weather/<location>` - Direct weather lookup
- `GET /api/math` - Direct math calculation

## Example Queries

### Weather Queries
- "What's the weather in New York?"
- "Temperature and forecast for London"
- "How's the weather in Tokyo?"

### Math Queries
- "Calculate something random"
- "Give me a math problem"
- "Do some random math"

## Configuration

The application can be configured through environment variables:

- `OPENWEATHER_API_KEY`: Your OpenWeatherMap API key
- `FLASK_DEBUG`: Enable/disable debug mode
- `SECRET_KEY`: Flask secret key for sessions

## Project Structure

```
CrewAgents/
├── app.py                 # Flask web application
├── crew_weather_api.py    # CrewAI agent definitions
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── app.js        # Frontend JavaScript
└── README.md             # This file
```

## Technologies Used

- **Backend**: Python, Flask, CrewAI
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)
- **API**: OpenWeatherMap

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please open an issue on the GitHub repository.
