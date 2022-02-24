# Imports
import toml # the config file uses TOML
import os

# Default variables
CONF_PATH = os.getcwd() + "\\src\\configurations\\"
CONF_FILE = "config.toml"

# Configuration loader class
class ConfigLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.toml_data = toml.load(file_path)
    
    def get(self, key):
        return self.toml_data[key]
