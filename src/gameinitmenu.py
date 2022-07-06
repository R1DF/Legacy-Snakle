# Imports
from screen import *
from canvas_ui.button import Button
from canvas_ui.pack_selector_list import PackSelectorList
from necessary_defaults import THEMES_PATH, DEFAULT_THEME


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

        self.pack_selector_list = PackSelectorList(
            self,
            self.WIDTH // 2,
            425,
            425,
            100,
            conf=self.conf,
            theme=self.theme,
        )
