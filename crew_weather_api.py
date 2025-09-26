# crew_weather_math.py

import random
import requests
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task

# Replace with your actual OpenWeatherMap API key
OPENWEATHER_API_KEY = "YOUR_API_KEY_HERE"

@CrewBase
class WeatherMathCrew:
    """Crew with a Root agent and two specialist agents (Weather and Math)."""

    @agent
    def root(self) -> Agent:
        return Agent(
            role="Root Router",
            goal="Receive a user query and route it to the appropriate agent (weather or math).",
            backstory="I route queries about weather to the Weather Agent and all other queries to the Math Agent.",
            allow_delegation=False,
            verbose=True  # Log detailed steps
        )

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            role="Weather Data Fetcher",
            goal="Fetch current weather information from OpenWeatherMap API.",
            backstory="I retrieve weather data when given a location query.",
            allow_code_execution=True,
            verbose=True
        )

    @agent
    def math_agent(self) -> Agent:
        return Agent(
            role="Random Math Operator",
            goal="Perform a random mathematical operation and return the result.",
            backstory="I generate random numbers, apply a random operation, and give the result.",
            allow_code_execution=True,
            verbose=True
        )

    @task
    def root_task(self) -> Task:
        return Task(
            description="Determine if query is about weather or math",
            expected_output="Which agent should handle the query (weather or math)",
            agent=self.root
        )

    @task
    def weather_task(self) -> Task:
        return Task(
            description="Fetch weather data for the specified location",
            expected_output="Current weather information in a human-readable format",
            agent=self.weather_agent
        )

    @task
    def math_task(self) -> Task:
        return Task(
            description="Compute a random math operation",
            expected_output="Result of the random math operation",
            agent=self.math_agent
        )

    @crew
    def crew(self) -> Crew:
        # Create crew with all agents and tasks, enabling memory and verbose logging
        return Crew(
            agents=[self.root, self.weather_agent, self.math_agent],
            tasks=[self.root_task, self.weather_task, self.math_task],
            process=Process.sequential,
            memory=True,
            verbose=True
        )

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

# Function for the math agent to perform a random calculation
def do_random_math() -> str:
    # Choose two random integers and an operation
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*', '**'])
    result = eval(f"{a} {op} {b}")
    return f"{a} {op} {b} = {result}"

# Override agent behavior by hooking into Crew callbacks
# Here, we manually route the tasks based on the root agent's decision.
def main():
    crew_obj = WeatherMathCrew().crew()

    # Sample queries to demonstrate routing
    queries = [
        "What's the weather in London?",
        "Calculate something random for me.",
        "Temperature and forecast, please.",
        "Give me a random math result.",
    ]
    for query in queries:
        print(f"\nUser query: \"{query}\"")

        # Determine routing (simple keyword check)
        if any(k in query.lower() for k in ["weather", "temperature", "forecast"]):
            agent_used = "Weather Agent"
            response = get_weather(query.split()[-1].strip("?.!"))
        else:
            agent_used = "Math Agent"
            response = do_random_math()

        print(f"Routed to: {agent_used}")
        print(f"Response: {response}")

if __name__ == "__main__":
    main()
