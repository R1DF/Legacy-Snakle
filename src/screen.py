# Imports
from tkinter import Canvas, Tk

# Screen template
class Screen(Canvas):
    def __init__(self, master, theme: dict, conf):
        self.master = master # make master available to class
        self.theme = theme["data"]
        self.theme_metadata = theme["meta"]

        # Initializing variables to not write too much code
        self.conf = conf
        self.WIDTH = self.conf.get("window")["resolutions"][self.conf.get("window")["default_resolution_index"]][0]
        self.HEIGHT = self.conf.get("window")["resolutions"][self.conf.get("window")["default_resolution_index"]][1]
        self.FONTS = self.conf.get("text")["fonts"]
        self.FONT = self.FONTS[self.conf.get("text")["default_font_family_index"]]
        self.TEXT_SIZES = {
            "huge": self.conf.get("text")["text_size_huge"],
            "big": self.conf.get("text")["text_size_big"],
            "mid": self.conf.get("text")["text_size_mid"],
            "small": self.conf.get("text")["text_size_small"]
        }

        # Calling the parent constructor
        Canvas.__init__(self, self.master)

        # Drawing the screen
        self.initiate()
    
    def initiate(self):
        pass # Gets defined with every individual screen

