# Example Python code using a hypothetical CrewAI SDK for multi-agent handling.
# This illustrative design includes:
# - A RootAgent that routes queries to a WeatherAgent or MathAgent.
# - WeatherAgent: Calls a sample weather API (e.g., Open-Meteo) for weather-related queries.
# - MathAgent: Performs a random math operation for other queries.

import random   # For generating random numbers and picking random operations
import requests # For making HTTP requests to a weather API (e.g., Open-Meteo)
import re       # For simple parsing of text (extracting locations or numbers)

# Stub base classes simulating the CrewAI SDK structures.
class CrewAgent:
    """Stub base class for an agent in the CrewAI SDK."""
    pass

class CrewTool:
    """Stub base class for an external tool/integration in the CrewAI SDK."""
    pass

class WeatherAgent(CrewAgent):
    """
    Agent 1: Handles weather-related queries.
    Uses a weather API (e.g., Open-Meteo) to fetch and return weather data.
    """
    def handle_query(self, query: str) -> str:
        # Very basic check for a location in the query (e.g., "in London")
        location_match = re.search(r'in ([A-Za-z ]+)', query)
        if location_match:
            location = location_match.group(1).strip()
        else:
            location = "New York"  # Default location if none found

        # Stub: Convert location to coordinates (latitude, longitude).
        # In a real implementation, use a geocoding API or database.
        coords = {
            "New York": (40.7128, -74.0060),
            "London": (51.5074, -0.1278),
            "Paris": (48.8566, 2.3522)
        }
        lat, lon = coords.get(location, coords["New York"])

        # Construct the Open-Meteo API URL (forecast endpoint as an example)
        api_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&hourly=temperature_2m"
        )
        try:
            response = requests.get(api_url)
            data = response.json()
            # Extract a sample piece of data (e.g., the first hourly temperature)
            temperature = data["hourly"]["temperature_2m"][0]
            return f"The current temperature in {location} is {temperature}°C."
        except Exception as e:
            # Handle errors (network issues, unexpected response format, etc.)
            return f"Sorry, I couldn't fetch the weather data: {e}"

class MathAgent(CrewAgent):
    """
    Agent 2: Handles non-weather (mathematical) queries.
    Performs a random operation on user-provided or random numbers.
    """
    def handle_query(self, query: str) -> str:
        # Find all numbers in the query (simple approach)
        numbers = re.findall(r'\d+', query)
        if numbers:
            nums = [float(num) for num in numbers]
        else:
            # If no numbers found, generate two random integers between 1 and 10
            nums = [random.randint(1, 10), random.randint(1, 10)]

        # Define possible operations
        operations = {
            'addition': lambda x, y: x + y,
            'multiplication': lambda x, y: x * y,
            'exponentiation': lambda x, y: x ** y
        }
        # Pick a random operation
        op_name, op_func = random.choice(list(operations.items()))

        # Ensure there are two numbers to operate on
        if len(nums) == 1:
            nums.append(random.randint(1, 5))
        x, y = nums[0], nums[1]
        result_value = op_func(x, y)
        return f"Performing {op_name} on {x} and {y} yields {result_value}."

class RootAgent(CrewAgent):
    """
    Root/Entry Agent: Routes natural language queries to the appropriate sub-agent.
    """
    def __init__(self):
        # Initialize sub-agents
        self.weather_agent = WeatherAgent()
        self.math_agent = MathAgent()

    def handle_query(self, query: str) -> str:
        # Determine which agent should handle the query.
        # If the query mentions 'weather', route to WeatherAgent; otherwise MathAgent.
        if 'weather' in query.lower():
            return self.weather_agent.handle_query(query)
        else:
            return self.math_agent.handle_query(query)

# Example usage demonstrating the routing logic:
if __name__ == "__main__":
    root_agent = RootAgent()

    example_queries = [
        "What's the weather in London?",
        "Tell me the weather forecast for tomorrow",
        "Add 7 and 5 for me",
        "Compute something interesting"
    ]
    for q in example_queries:
        print(f"Query: {q}")
        response = root_agent.handle_query(q)
        print(f"Response: {response}\n")
