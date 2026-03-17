import mysql.connector

import logging
from config.settings import DB_CONFIG
from config.settings import EMAIL_CONFIG
from database_tools.db_connection import create_connection

''' SET UP LOGGING SYSTEM'''

# Declare file to log into
LOG_FILENAME = "C:\\Users\\jahna\\OneDrive\\Documents\\CS Stuff\\SQL\\SQL-Error-Alert-System\\logs\\system.log"
# LOG_FILENAME = "system.log"

# Create logger object

# Configure logging basics
logging.basicConfig(
        filename=LOG_FILENAME,
        encoding='utf-8',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
        datefmt='%m-%d-%y %H:%M:%S',
        force=True                   # must include this, as logging may have been configured in one of the imported libraries, and we want to use this configuration.
)

LOGGER = logging.getLogger(__name__)

# Wrap up task
LOGGER.info("Logging setup complete.\n")

# Connect to the database
DB_CONNECTION = create_connection(DB_CONFIG)

LOGGER.info("Successfully connected to MySQL database.\n")

# Run the SQL script(s)
# for now, it would be prudent to just run the stuff in the sql_scripts/ directory
CURSOR = DB_CONNECTION.cursor()

CURSOR.execute("SELECT * FROM parks_and_recreation.employee_demographics;")
result = CURSOR.fetchall()


for row in result:
        print(row)

# Wrap up task
LOGGER.info("Ran SQL script.\n")

#if successful, log/print it.
# Wrap up task

# if unsuccessful, send an email with the error information
# Wrap up task

# send email
# Wrap up task


# Wrap up program
LOGGER.info("Program complete.\n------------------------------------------------------------------------------------")
print("Program complete.")