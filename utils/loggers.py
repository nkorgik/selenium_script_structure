import logging 


def setup_logger(logger_name: str, file_name: str, default_level=logging.INFO) -> logging.Logger:
    """Setups and returns new logger object"""

    formatter = logging.Formatter('%(asctime)s: %(message)s')
    handler = logging.FileHandler(filename=file_name)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name=logger_name)
    logger.setLevel(level=default_level)
    logger.addHandler(handler)
    
    return logger
