import configparser


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('ecommerce/config/config.ini')

    def get_config(self):
        return self.config