LOCATION_FILE = "/home/erik/PycharmProjects/pythonEmail.txt"

def load_config():
    config = {}
    with open(LOCATION_FILE) as file:
        for line in file:
            line = line.strip().replace('"', '')
            if " = " in line:
                key, value = line.split(" = ", 1)
                config[key] = value
    return config

config_data = load_config()

def get_stock_key():
    return config_data.get("alphavantage_stock_key", "")

def get_news_key():
    return config_data.get("news_key", "")

def get_twillio_sid():
    return config_data.get("account_sid_twillio", "")

def get_twillio_messaging_sid():
    return config_data.get("messaging_service_sid_twillio", "")

def get_twillio_token():
    return config_data.get("twillio_token", "")