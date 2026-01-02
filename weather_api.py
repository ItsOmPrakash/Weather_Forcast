import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return None

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["main"]
        }

    except Exception:
        return None


def get_weather_by_location():
    try:
        # Get location from IP
        loc_response = requests.get("https://ipinfo.io/json", timeout=5)
        loc_data = loc_response.json()

        latitude, longitude = loc_data["loc"].split(",")

        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return None

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["main"]
        }

    except Exception:
        return None


# Test backend independently
if __name__ == "__main__":
    print(get_weather("Delhi"))
