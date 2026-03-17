from dotenv import load_dotenv
import logging
import os

# loads variables from .env into the environment
load_dotenv()

def get_env_variable(var_name):
    '''
    Retrieves the given variable from the environment variables.
    :param var_name: the name of the variable to retrieve
    :return: the value of the environment variable
    '''

    logging.info(f"Getting environment variable {var_name}")

    value = os.getenv(var_name)

    if value is None:
        logging.warning(f"Missing environment variable {var_name}")
        raise Exception(f"Missing environment variable {var_name}")

    return value

