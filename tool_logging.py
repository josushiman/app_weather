import logging

def create_logger(app_name, log_filename):
    '''
    Takes in the app name, and log filename and returns a logging object to use in a project.
    '''
    # Setting up the logger
    logger = logging.getLogger(app_name)

    # Set logging level here
    logger.setLevel(logging.DEBUG)

    # Set format for the prefix of log outputs here
    log_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

    # Sets the filename variable here
    log_file_handler = logging.FileHandler(log_filename)
    log_file_handler.setFormatter(log_formatter)

    logger.addHandler(log_file_handler)

    return logger