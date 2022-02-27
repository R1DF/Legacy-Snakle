# Imports
import os, toml

# CONFIGURATIONS
CONF_PATH = os.getcwd() + "\\configurations\\"
CONF_FILE = "config.toml"

# THEMES
THEMES_PATH = os.getcwd() + "\\themes\\"
DEFAULT_THEME = toml.load("default_theme.toml")["default"]
