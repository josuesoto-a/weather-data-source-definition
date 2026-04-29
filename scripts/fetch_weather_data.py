import requests
import json
from datetime import datetime
import os
import logging

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 9.93,
    "longitude": -84.08,
    "current_weather": True
}

# --------------------------------------------------
# Definir directorio raíz del proyecto
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# --------------------------------------------------
# Definir carpeta logs dentro del proyecto
# --------------------------------------------------

logs_dir = os.path.join(BASE_DIR, "logs")

# --------------------------------------------------
# Crear carpeta logs si no existe
# --------------------------------------------------

os.makedirs(logs_dir, exist_ok=True)

# --------------------------------------------------
# Definir archivo de log
# --------------------------------------------------

log_file = os.path.join(logs_dir, "pipeline.log")

# --------------------------------------------------
# Configurar logging
# --------------------------------------------------

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_weather_data():

    logging.info("Fetch weather data script started")

    try:

        logging.info("Sending request to weather API")

        response = requests.get(URL, params=params)

        if response.status_code == 200:

            logging.info("API request successful")

            data = response.json()

            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            data_dir = os.path.join(BASE_DIR, "data")

            os.makedirs(data_dir, exist_ok=True)

            filename = os.path.join(
                data_dir,
                f"weather_data_{timestamp}.json"
            )

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

            logging.info(
                f"Data saved successfully to {filename}"
            )

            print("Data saved to:", filename)

        else:

            logging.error(
                f"Request failed with status code {response.status_code}"
            )

            print("Request failed")
            print("Status code:", response.status_code)

    except Exception as e:

        logging.error(
            f"Unexpected error occurred: {e}"
        )

        print("An unexpected error occurred:", e)

    logging.info("Fetch weather data script finished")


if __name__ == "__main__":
    fetch_weather_data()