# Imports
from screen import *
from canvas_ui.button import Button
from canvas_ui.file_selector_list import FileSelectorList
from necessary_defaults import THEMES_PATH, DEFAULT_THEME
from os import getcwd

# Game initialization canvas
class GameInitMenu(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Drawing out widgets
        self.intro_text = self.create_text(
            self.WIDTH // 2,
            50,
            text="Play",
            font=[self.FONT, self.TEXT_SIZES["huge"]]
        )
        "Select Online"
        self.create_text(
            self.WIDTH // 2,
            110,
            text="Select the pack you'd like to use:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.pack_selector_list = FileSelectorList(
            self,
            self.WIDTH // 2,
            self.HEIGHT // 2,
            425,
            300,
            overlooked_directory= getcwd() + "\\packs\\",
            conf=self.conf,
            theme=self.theme,
            extension="json",
            file_type="pack"
        )

