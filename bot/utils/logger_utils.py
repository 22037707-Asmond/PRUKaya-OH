import logging

def setup_logger():
    logger = logging.getLogger('PRUKAYA_BOT')
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)

        logger.addHandler(console_handler)

    return logger
