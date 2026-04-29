import json
import os
import logging

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

os.makedirs(logs_dir, exist_ok=True)

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
# DIRECTORIOS
# --------------------------------------------------

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

PROCESSED_DIR = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)

# --------------------------------------------------
# FUNCIÓN PARA OBTENER EL ARCHIVO MÁS RECIENTE
# --------------------------------------------------

def get_latest_raw_file(data_dir):

    files = [
        f for f in os.listdir(data_dir)
        if f.startswith("weather_data_")
        and f.endswith(".json")
    ]

    if not files:
        return None

    files.sort(reverse=True)

    latest_file = files[0]

    return os.path.join(
        data_dir,
        latest_file
    )

# --------------------------------------------------
# FUNCIÓN PARA GENERAR NOMBRE DINÁMICO
# --------------------------------------------------

def generate_clean_filename(raw_file):

    filename = os.path.basename(raw_file)

    timestamp = filename.replace(
        "weather_data_",
        ""
    )

    clean_filename = f"clean_weather_data_{timestamp}"

    return os.path.join(
        PROCESSED_DIR,
        clean_filename
    )

# --------------------------------------------------
# FUNCIÓN PRINCIPAL
# --------------------------------------------------

def clean_data():

    logging.info("Clean script started")

    raw_file = get_latest_raw_file(DATA_DIR)

    if raw_file is None:

        logging.error("No raw data files found")
        print("No raw data files found")

        return

    logging.info(
        f"Processing latest file: {raw_file}"
    )

    try:

        with open(
            raw_file,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        logging.info(
            "Raw data loaded successfully"
        )

    except Exception as e:

        logging.error(
            f"Error reading JSON file: {e}"
        )

        print("Error reading JSON file")

        return

    if "current_weather" not in data:

        logging.error(
            "Unexpected JSON structure"
        )

        logging.error(
            json.dumps(data)
        )

        print("Unexpected JSON structure")

        return

    weather = data["current_weather"]

    cleaned_data = {}

    cleaned_data["latitude"] = data.get(
        "latitude"
    )

    cleaned_data["longitude"] = data.get(
        "longitude"
    )

    cleaned_data["elevation"] = data.get(
        "elevation"
    )

    cleaned_data["temperature"] = weather.get(
        "temperature"
    )

    cleaned_data["windspeed"] = weather.get(
        "windspeed"
    )

    cleaned_data["wind_direction"] = weather.get(
        "winddirection"
    )

    cleaned_data["weather_code"] = weather.get(
        "weathercode"
    )

    cleaned_data["timestamp"] = weather.get(
        "time"
    )

    logging.info(
        "Data transformation completed"
    )

    os.makedirs(
        PROCESSED_DIR,
        exist_ok=True
    )

    logging.info(
        "Processed directory verified"
    )

    clean_file = generate_clean_filename(
        raw_file
    )

    try:

        with open(
            clean_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                cleaned_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        logging.info(
            f"Cleaned data saved to {clean_file}"
        )

        print(
            "Cleaned data saved to:",
            clean_file
        )

    except Exception as e:

        logging.error(
            f"Error saving cleaned data: {e}"
        )

        print(
            "Error saving cleaned data"
        )

    logging.info(
        "Clean script finished"
    )


if __name__ == "__main__":

    clean_data()