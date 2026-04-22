import json
import os

# Base directory del script
BASE_DIR = os.path.dirname(__file__)

# Archivo RAW (entrada)
RAW_FILE = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "weather_data_2026-04-16_06-00-15.json"
)

# Archivo CLEAN (salida)
CLEAN_FILE = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "processed",
    "clean_weather_data.json"
)


def clean_data():

    # 1 — Verificar existencia del archivo raw

    if not os.path.exists(RAW_FILE):
        print("Raw data file not found")
        return

    # 2 — Leer JSON

    with open(RAW_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 3 — Validar estructura

    if "current_weather" not in data:
        print("Unexpected JSON structure:")
        print(json.dumps(data, indent=4))
        return

    weather = data["current_weather"]

    # 4 — Transformar datos

    cleaned_data = {}

    cleaned_data["latitude"] = data.get("latitude")
    cleaned_data["longitude"] = data.get("longitude")
    cleaned_data["elevation"] = data.get("elevation")

    cleaned_data["temperature"] = weather.get("temperature")
    cleaned_data["windspeed"] = weather.get("windspeed")
    cleaned_data["wind_direction"] = weather.get("winddirection")
    cleaned_data["weather_code"] = weather.get("weathercode")

    cleaned_data["timestamp"] = weather.get("time")

    # 5 — Crear carpeta processed si no existe

    os.makedirs(
        os.path.dirname(CLEAN_FILE),
        exist_ok=True
    )

    # 6 — Guardar archivo limpio

    with open(CLEAN_FILE, "w", encoding="utf-8") as file:

        json.dump(
            cleaned_data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("Cleaned data saved to:", CLEAN_FILE)


if __name__ == "__main__":
    clean_data()