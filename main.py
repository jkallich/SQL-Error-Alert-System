import logging


''' SET UP LOGGING SYSTEM'''

# Declare file to log into
log_file = "C:\\Users\\jahna\\OneDrive\\Documents\\CS Stuff\\SQL\\SQL-Error-Alert-System\\logs\\system.log"

logging.basicConfig(
        filename=log_file,
        encoding='utf-8',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
        datefmt='%m-%d-%y %H:%M:%S'
)

logger = logging.getLogger(__name__)

logger.info("Logging setup complete.\n")

# Request the user for their SQL Workbench username and password, the host they're using, the database they need to connect to, and the email they want to send alerts to.
# for now, just using inputs and stuff.

# Wrap up task
logger.info("Configuration setup complete.\n")



# Connect to the database

# Wrap up task
logger.info("Connection to database complete.\n")


# Run the SQL script(s)
# for now, it would be prudent to just run the stuff in the sql_scripts/ directory

# Wrap up task
logger.info("Ran SQL script.\n")

#if successful, log/print it.
# Wrap up task
logger.info("SQL script ran successfully.\n")

# if unsuccessful, send an email with the error information
# Wrap up task
logger.info("SQL script ran unsuccessfully.\n")
# send email
# Wrap up task
logger.info("Alert complete.\n")


# Wrap up program
logger.info("Program complete.\n------------------------------------------------------------------------------------")
print("Program complete.")