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

CLEAN_FILE = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "clean_weather_data.json"
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

    # Ordenar por nombre (timestamp)
    files.sort(reverse=True)

    latest_file = files[0]

    return os.path.join(
        data_dir,
        latest_file
    )

# --------------------------------------------------
# FUNCIÓN PRINCIPAL
# --------------------------------------------------

def clean_data():

    logging.info("Clean script started")

    # 1 — Encontrar el archivo más reciente

    raw_file = get_latest_raw_file(DATA_DIR)

    if raw_file is None:

        logging.error("No raw data files found")
        print("No raw data files found")

        return

    logging.info(
        f"Processing latest file: {raw_file}"
    )

    # 2 — Leer JSON

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

    # 3 — Validar estructura

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

    # 4 — Transformar datos

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

    # 5 — Crear carpeta processed

    os.makedirs(
        os.path.dirname(CLEAN_FILE),
        exist_ok=True
    )

    logging.info(
        "Processed directory verified"
    )

    # 6 — Guardar archivo limpio

    try:

        with open(
            CLEAN_FILE,
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
            f"Cleaned data saved to {CLEAN_FILE}"
        )

        print(
            "Cleaned data saved to:",
            CLEAN_FILE
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

# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":

    clean_data()