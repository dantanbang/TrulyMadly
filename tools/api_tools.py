import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str):
    """Calls OpenWeatherMap API."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "city": city
        }
    except Exception as e:
        return {"error": f"Weather error: {str(e)}"}

def search_github(query: str):
    """Calls GitHub Search API."""
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        items = response.json().get("items", [])[:3] 
        return [{"name": r["full_name"], "stars": r["stargazers_count"], "url": r["html_url"]} for r in items]
    except Exception as e:
        return {"error": f"GitHub error: {str(e)}"}
