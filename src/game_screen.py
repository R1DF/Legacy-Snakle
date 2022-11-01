# Imports
import random
from screen import *
from necessary_defaults import THEMES_PATH, DEFAULT_THEME
from os import getcwd

# Game initialization canvas
class GameScreen(Screen):
    def __init__(self, master, theme, conf, words_pack):
        Screen.__init__(self, master, theme, conf)
        self.words_pack = words_pack
        self.word = random.choice(self.words_pack["words"])

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Widgets

