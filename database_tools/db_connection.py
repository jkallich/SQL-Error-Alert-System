from config.settings import DB_CONFIG
import mysql.connector

import logging

LOGGER = logging.getLogger(__name__)

def create_connection(db_config):
    '''
    Creates a connection to the MySQL database using the information in .env
    :return: A MySQL Connection object (used to create a Cursor object)
    '''

    LOGGER.info("Connecting to MySQL database.\n")

    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        LOGGER.error(f"Failed to connect to MySQL database: {err}")
        raise Exception(f"Ran into the following error while connecting to MySQL database:\n{format(err)}")