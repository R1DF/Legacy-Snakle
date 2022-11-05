# Imports
import random
import os
import json
from screen import *
from canvas_ui.button import Button
from canvas_ui.game_table import WordTable


# Game initialization canvas
class GameScreen(Screen):
    def __init__(self, master, theme, conf, words_pack, pack_file_name):
        self.words_pack = words_pack
        self.words = self.words_pack["words"]
        self.valid_words = json.load(open(os.getcwd() + "\\configurations\\words_check.json", "r"))["words"]
        self.pack_file_name = pack_file_name
        self.clearance_file_path = os.getcwd() + "\\clearance_data\\" + f"c_{self.pack_file_name}"
        self.clearance_file_data = json.load(open(self.clearance_file_path, "r"))

        # Getting the word
        if len(self.clearance_file_data["clear_words"]) / len(self.words) == 1.0:
            # If the entire pack has been fully cleared, just get a random word
            self.word = random.choice(self.words)
        else:
            # If the entire pack WASN'T fully cleared, get a random word that hasn't been cleared
            set_intersection = set(self.words) ^ set(self.clearance_file_data["clear_words"])  # finds symmetric difference (!intersection)
            self.word = random.choice(list(set_intersection))

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
            word=self.word,
            valid_words=self.valid_words + self.words,  # Sets are being used so it doesn't matter if duplicates exist
            conf=self.conf,
            theme=self.theme,
            update_callback=self.check_on_enter
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

        self.new_game_button = Button(
            self,
            (self.WIDTH // 2) + 130,
            550,
            200,
            50,
            text="New Game",
            theme=self.theme,
            conf=self.conf,
            callback=self.make_new_game
        )

        self.new_game_button.hide()

    def back_to_menu(self):
        self.master.make_main_menu()
        self.destroy()

    def make_new_game(self):
        self.master.make_game(self.words_pack, self.pack_file_name)
        self.destroy()

    def add_to_clearance(self, word):
        new_data = self.clearance_file_data
        if word not in self.clearance_file_data["clear_words"]:
            new_data["clear_words"].append(word)
        json.dump(new_data, open(self.clearance_file_path, "w"))


    def check_on_enter(self, entered_text, attempt):
        # Updating attempt
        self.itemconfig(self.attempts_text, text=f"Attempts: {attempt}/6")

        # Checking exit cases
        if entered_text == self.word or attempt == 6:
            self.word_table.focused_on = False
            self.itemconfig(self.end_text, text="Congratulations! You win!" if entered_text == self.word else f"No attempts left! The word was {self.word}.")

            # if the player won, add a new word to the clearance file
            if entered_text == self.word:
                self.add_to_clearance(self.word)


            self.new_game_button.show()

            # Play sound lastly if there's sound on and there is no progressive reveal
            if not self.word_table.has_slow_reveal:
                self.update()
                self.word_table.sound_system.force_play("correct_match", True)

