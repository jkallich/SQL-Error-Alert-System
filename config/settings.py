from config.load_env import get_env_variable

DB_CONFIG = {
    "host" : get_env_variable("DB_HOST"),
    "user" : get_env_variable("DB_USER"),
    "password" : get_env_variable("DB_PASSWORD"),
    "database" : get_env_variable("DB_NAME"),
}

EMAIL_CONFIG = {
    "smtp_server": get_env_variable("EMAIL_SMTP"),
    "port": int(get_env_variable("EMAIL_PORT")),
    "sender_email": get_env_variable("EMAIL_SENDER"),
    "receiver_email": get_env_variable("EMAIL_RECEIVER"),
    "password": get_env_variable("EMAIL_PASSWORD")
}