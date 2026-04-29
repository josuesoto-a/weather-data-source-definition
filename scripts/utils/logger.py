import os
import logging


def setup_logger():

    # --------------------------------------------------
    # BASE DIRECTORY DEL PROYECTO
    # --------------------------------------------------

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    # --------------------------------------------------
    # DIRECTORIO DE LOGS
    # --------------------------------------------------

    logs_dir = os.path.join(
        BASE_DIR,
        "logs"
    )

    os.makedirs(
        logs_dir,
        exist_ok=True
    )

    # --------------------------------------------------
    # ARCHIVO DE LOG
    # --------------------------------------------------

    log_file = os.path.join(
        logs_dir,
        "pipeline.log"
    )

    # --------------------------------------------------
    # CONFIGURACIÓN DE LOGGING
    # --------------------------------------------------

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging