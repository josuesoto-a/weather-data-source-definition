import os
import logging
import sys

# --------------------------------------------------
# AGREGAR LA CARPETA scripts AL PATH
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

SCRIPTS_DIR = os.path.join(
    BASE_DIR,
    "scripts"
)

sys.path.append(SCRIPTS_DIR)

# --------------------------------------------------
# IMPORTAR FUNCIONES
# --------------------------------------------------

from fetch_weather_data import fetch_weather_data
from clean_weather_data import clean_data

# --------------------------------------------------
# CONFIGURACIÓN DE LOGGING
# --------------------------------------------------

logs_dir = os.path.join(
    BASE_DIR,
    "logs"
)

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
# FUNCIÓN PRINCIPAL
# --------------------------------------------------

def run_pipeline():

    logging.info(
        "Pipeline execution started"
    )

    print(
        "Pipeline started"
    )

    try:

        # -------------------------
        # STEP 1 — FETCH
        # -------------------------

        logging.info(
            "Starting fetch step"
        )

        fetch_weather_data()

        logging.info(
            "Fetch step completed"
        )

        # -------------------------
        # STEP 2 — CLEAN
        # -------------------------

        logging.info(
            "Starting clean step"
        )

        clean_data()

        logging.info(
            "Clean step completed"
        )

        logging.info(
            "Pipeline executed successfully"
        )

        print(
            "Pipeline finished successfully"
        )

    except Exception as e:

        logging.error(
            f"Pipeline failed: {e}"
        )

        print(
            "Pipeline failed:",
            e
        )

# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":

    run_pipeline()