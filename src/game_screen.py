# Imports
import random
from screen import *
from canvas_ui.button import Button
from canvas_ui.game_table import WordTable

# Game initialization canvas
class GameScreen(Screen):
    def __init__(self, master, theme, conf, words_pack):
        self.words_pack = words_pack
        self.word = random.choice(self.words_pack["words"])
        Screen.__init__(self, master, theme, conf)

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Widgets
        self.word_table = WordTable(
            self,
            self.WIDTH // 2,
            100,
            50,
            20,
            self.conf,
            self.theme
        )

        self.attempts_text = self.create_text(
            self.WIDTH // 2,
            450,
            text="Attempts: 0/6",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.end_text = self.create_text(
            self.WIDTH // 2,
            490,
            text="",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.back_button = Button(
            self,
            (self.WIDTH // 2) - 130,
            550,
            200,
            50,
            text="Back",
            theme=self.theme,
            conf=self.conf,
            callback=self.back_to_menu
        )

        self.new_button = Button(
            self,
            (self.WIDTH // 2) + 130,
            550,
            200,
            50,
            text="New Game",
            theme=self.theme,
            conf=self.conf
        )

        self.new_button.hide()
        print(self.word)

    def back_to_menu(self):
        self.master.make_main_menu()
        self.destroy()