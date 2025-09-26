from flask import Flask, render_template, request, jsonify
import os
import sys
from crew_weather_api import simple_query_router, get_weather, do_math_calculation, get_api_data
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def handle_query():
    """Handle user queries and route to appropriate agent"""
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'No query provided'}), 400
        
        # Use simple routing logic without AI
        query_type = simple_query_router(query)
        
        if query_type == "weather":
            # Extract location from query
            words = query.split()
            location = "London"  # Default location
            for i, word in enumerate(words):
                if word.lower() in ["in", "at", "for"] and i + 1 < len(words):
                    location = words[i + 1].strip("?.!")
                    break
                elif word.lower() in ["weather", "temperature", "forecast"] and i + 1 < len(words):
                    location = words[i + 1].strip("?.!")
                    break
            
            agent_used = "Weather Agent"
            response = get_weather(location)
        elif query_type == "api":
            agent_used = "API Agent"
            response = get_api_data(query)
        else:
            agent_used = "Math Agent"
            response = do_math_calculation(query)
        
        return jsonify({
            'query': query,
            'agent_used': agent_used,
            'response': response,
            'success': True
        })
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'success': False
        }), 500

@app.route('/api/weather/<location>')
def get_weather_api(location):
    """Direct weather API endpoint"""
    try:
        response = get_weather(location)
        return jsonify({
            'location': location,
            'response': response,
            'success': True
        })
    except Exception as e:
        return jsonify({
            'error': f'Weather fetch error: {str(e)}',
            'success': False
        }), 500

@app.route('/api/math')
def get_math_api():
    """Direct math API endpoint"""
    try:
        response = do_math_calculation()
        return jsonify({
            'response': response,
            'success': True
        })
    except Exception as e:
        return jsonify({
            'error': f'Math calculation error: {str(e)}',
            'success': False
        }), 500

@app.route('/api/sample')
def get_sample_api():
    """Direct sample API endpoint"""
    try:
        response = get_api_data("random fact")
        return jsonify({
            'response': response,
            'success': True
        })
    except Exception as e:
        return jsonify({
            'error': f'API fetch error: {str(e)}',
            'success': False
        }), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
