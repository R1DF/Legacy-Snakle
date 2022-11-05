# Imports
import toml  # the config file uses TOML


# Configuration loader class
class ConfigLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.toml_data = toml.load(file_path)
    
    def get(self, key):
        return self.toml_data[key]

