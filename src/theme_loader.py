# Imports
import toml


# Creating loader class
class ThemeLoader:
    def __init__(self, master_window):
        self.master_window = master_window  # could be used for future reference?

    def load_theme(self, theme_path):
        theme_data = toml.load(theme_path)
        return theme_data

