import logging

def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(console)
    logger.addHandler(file_handler)
