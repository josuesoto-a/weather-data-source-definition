import requests
import json
from datetime import datetime
import os

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 9.93,
    "longitude": -84.08,
    "current_weather": True
}

def fetch_weather_data():

    response = requests.get(URL, params=params)

    if response.status_code == 200:

        data = response.json()

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Get project root directory
        BASE_DIR = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        data_dir = os.path.join(BASE_DIR, "data")

        os.makedirs(data_dir, exist_ok=True)

        filename = os.path.join(
            data_dir,
            f"weather_data_{timestamp}.json"
        )

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved to:", filename)

    else:

        print("Request failed")
        print("Status code:", response.status_code)

if __name__ == "__main__":
    fetch_weather_data()