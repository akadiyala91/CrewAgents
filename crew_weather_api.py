# crew_weather_math.py

import random
import requests

from config import Config

# Get API key from configuration
OPENWEATHER_API_KEY = Config.OPENWEATHER_API_KEY

# Simple routing without AI - we'll handle this in the Flask app
def simple_query_router(query):
    """Simple keyword-based routing without AI"""
    weather_keywords = ["weather", "temperature", "forecast", "climate", "rain", "snow", "sunny", "cloudy", "wind"]
    query_lower = query.lower()
    
    for keyword in weather_keywords:
        if keyword in query_lower:
            return "weather"
    
    return "math"

# Function for the weather agent to call the OpenWeather API
def get_weather(location: str) -> str:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    try:
        res = requests.get(base_url, params=params)
        data = res.json()
        if data.get("cod") != 200:
            return f"Error: {data.get('message', 'Unknown error')}."
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Weather in {location}: {desc}, temperature {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {e}"

# Function for the math agent to perform various calculations
def do_math_calculation(query: str = None) -> str:
    """Perform math calculations based on query or generate random ones"""
    
    # If query contains mathematical expressions, try to evaluate them
    if query:
        import re
        
        # Look for mathematical expressions in the query
        # Simple patterns: "5 + 3", "10 * 7", "15 / 3", etc.
        math_pattern = r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)'
        matches = re.findall(math_pattern, query)
        
        if matches:
            results = []
            for match in matches:
                num1, operator, num2 = match
                num1, num2 = float(num1), float(num2)
                
                try:
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        if num2 != 0:
                            result = num1 / num2
                        else:
                            return "Error: Division by zero!"
                    
                    # Format result nicely
                    if result == int(result):
                        result = int(result)
                    
                    results.append(f"{num1} {operator} {num2} = {result}")
                except Exception as e:
                    results.append(f"Error calculating {num1} {operator} {num2}: {str(e)}")
            
            return "; ".join(results)
    
    # Generate random math problems if no specific calculation found
    operation_type = random.choice(['basic', 'advanced', 'word_problem'])
    
    if operation_type == 'basic':
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        op = random.choice(['+', '-', '*'])
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
            
        return f"{a} {op} {b} = {result}"
    
    elif operation_type == 'advanced':
        operations = [
            ('square', lambda x: x**2, 'squared'),
            ('cube', lambda x: x**3, 'cubed'),
            ('factorial', lambda x: 1 if x <= 1 else x * factorial(x-1) if x <= 10 else 'too large', 'factorial')
        ]
        
        op_name, op_func, op_desc = random.choice(operations)
        num = random.randint(2, 10)
        
        try:
            result = op_func(num)
            if op_name == 'factorial':
                return f"{num}! = {result}"
            else:
                return f"{num} {op_desc} = {result}"
        except:
            return f"Cannot compute {num} {op_desc}"
    
    else:  # word_problem
        scenarios = [
            ("apples", "basket"),
            ("books", "shelf"),
            ("cars", "parking lot"),
            ("students", "classroom")
        ]
        
        item, container = random.choice(scenarios)
        initial = random.randint(5, 20)
        change = random.randint(1, 10)
        
        if random.choice([True, False]):  # addition
            result = initial + change
            return f"There were {initial} {item} in the {container}. {change} more were added. Total: {result} {item}"
        else:  # subtraction
            change = min(change, initial)  # don't go negative
            result = initial - change
            return f"There were {initial} {item} in the {container}. {change} were removed. Remaining: {result} {item}"

def factorial(n):
    """Helper function for factorial calculation"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Simple standalone functions for weather and math - no CrewAI dependency needed
def main():
    """Simple test function"""
    queries = [
        "What's the weather in London?",
        "Calculate 15 + 25",
        "Temperature in Paris",
        "What is 5 * 8?",
        "Give me a random math problem",
    ]
    
    for query in queries:
        print(f"\nQuery: \"{query}\"")
        query_type = simple_query_router(query)
        
        if query_type == "weather":
            # Extract location
            words = query.split()
            location = "London"
            for i, word in enumerate(words):
                if word.lower() in ["in", "at", "for"] and i + 1 < len(words):
                    location = words[i + 1].strip("?.!")
                    break
                elif word.lower() in ["weather", "temperature", "forecast"] and i + 1 < len(words):
                    location = words[i + 1].strip("?.!")
                    break
            
            print(f"Routed to: Weather Agent")
            print(f"Response: {get_weather(location)}")
        else:
            print(f"Routed to: Math Agent")
            print(f"Response: {do_math_calculation(query)}")

if __name__ == "__main__":
    main()
