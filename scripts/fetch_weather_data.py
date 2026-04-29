import requests
import json
from datetime import datetime
import os
import logging

# --------------------------------------------------
# CONFIGURACIÓN API
# --------------------------------------------------

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 9.93,
    "longitude": -84.08,
    "current_weather": True
}

# --------------------------------------------------
# BASE DIRECTORY DEL PROYECTO
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# --------------------------------------------------
# CONFIGURACIÓN DE LOGGING
# --------------------------------------------------

logs_dir = os.path.join(BASE_DIR, "logs")

os.makedirs(
    logs_dir,
    exist_ok=True
)

log_file = os.path.join(
    logs_dir,
    "pipeline.log"
)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# DIRECTORIO DATA
# --------------------------------------------------

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)

# --------------------------------------------------
# FUNCIÓN PRINCIPAL
# --------------------------------------------------

def fetch_weather_data():

    logging.info(
        "Fetch script started"
    )

    try:

        logging.info(
            "Sending request to weather API"
        )

        response = requests.get(
            URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        logging.info(
            "API request successful"
        )

        data = response.json()

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        filename = os.path.join(
            DATA_DIR,
            f"weather_data_{timestamp}.json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        logging.info(
            f"Data saved successfully to {filename}"
        )

        print(
            "Data saved to:",
            filename
        )

    except requests.exceptions.Timeout:

        logging.error(
            "Request timed out"
        )

        print(
            "Request timed out"
        )

    except requests.exceptions.HTTPError as e:

        logging.error(
            f"HTTP error occurred: {e}"
        )

        print(
            "HTTP error occurred"
        )

    except Exception as e:

        logging.error(
            f"Unexpected error occurred: {e}"
        )

        print(
            "Unexpected error occurred:",
            e
        )

    logging.info(
        "Fetch script finished"
    )


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":

    fetch_weather_data()