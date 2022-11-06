# Imports
from tkinter import Canvas
from .is_inside import is_inside
from sound_system import SoundSystem


# Table class
class WordTable:
    def __init__(
            self,
            master: Canvas,
            x,
            starting_y,
            offset,
            gap_x,
            word,
            valid_words,
            conf,
            theme,
            update_callback=lambda x, y: None
    ):
        # Initialization
        self.master = master
        self.center_x, self.start_y = x, starting_y  # start_y is the y position of the squares on the first row
        self.square_width = offset
        self.gap_length = gap_x
        self.conf = conf
        self.theme = theme
        self.width = (5 * self.square_width) + (4 * self.gap_length)
        self.height = (6 * self.square_width) + (5 * self.gap_length)
        self.selected_row_number = 1
        self.selected_letter_number = 1
        self.focused_on = True  # if this is is False then a WordTable object will not respond to typing at all
        self.valid_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                              "S", "T", "U", "V", "W", "X", "Y", "Z"]  # I totally know that I could have used ord() thank you very much
        self.word = word
        self.valid_words = set(valid_words)
        self.update_callback = update_callback
        self.sound_system = SoundSystem(self.conf)
        self.has_sound = self.conf.get("game")["has_sound"]
        self.has_slow_reveal = self.conf.get("game")["progressive_reveal_on_sound"]
        self.already_checking = False

        # Drawing
        self.boxes = []
        self.texts = []
        for y_index in range(1, 7):
            row_of_boxes = []
            row_of_texts = []
            for x_index in range(5):
                # WARNING: LOOKING AT THE CODE BELOW MIGHT MAKE YOU LOSE YOUR SANITY.
                row_of_boxes.append(self.master.create_rectangle(
                    (x_index * self.square_width) + (x_index * self.gap_length) + (self.center_x - (self.width // 2)),
                    (y_index * self.square_width) + (y_index * self.gap_length) + (self.center_x - (self.height // 2)) + (self.start_y - (self.height // 2)),
                    (x_index * self.square_width) + (x_index * self.gap_length) + (self.center_x - (self.width // 2)) + self.square_width,
                    (y_index * self.square_width) + (y_index * self.gap_length) + (self.center_x - (self.height // 2)) + (self.start_y - (self.height // 2)) + self.square_width,
                    width=2,
                    fill=self.theme["grid_square_fill"],
                    outline=self.theme["grid_square_border"]
                ))
                row_of_texts.append(self.master.create_text(
                    (x_index * self.square_width) + (x_index * self.gap_length) + (self.center_x - (self.width // 2)) + (self.square_width // 2),
                    (y_index * self.square_width) + (y_index * self.gap_length) + (self.center_x - (self.height // 2)) + (self.start_y - (self.height // 2)) + (self.square_width // 2),
                    text="",
                    fill=self.theme["grid_square_text_fill"],
                    font=[self.master.FONT, self.master.TEXT_SIZES["mid"]]
                ))
            self.boxes.append(row_of_boxes)
            self.texts.append(row_of_texts)

        # Binding
        self.master.master.bind("<KeyPress>", self.handle_type)

    def handle_type(self, event):
        if self.focused_on:
            if event.keysym == "BackSpace" and self.selected_letter_number >= 1:
                self.master.itemconfig(self.texts[self.selected_row_number - 1][self.selected_letter_number - 2], text="")
                if self.selected_letter_number != 1:
                    self.selected_letter_number -= 1

            elif event.keysym.upper() in self.valid_letters and self.selected_letter_number <= 5:
                letter = event.keysym.upper()
                self.master.itemconfig(self.texts[self.selected_row_number - 1][self.selected_letter_number - 1], text=letter)
                # if self.selected_letter_number != 6:
                self.selected_letter_number += 1

            elif event.keysym == "Return" and self.selected_row_number <= 6 and self.selected_letter_number == 6 and (not self.already_checking):
                self.already_checking = True
                # Verifying whether the entered word is valid
                entered_text = "".join([self.master.itemcget(x, "text") for x in self.texts[self.selected_row_number - 1]])
                if entered_text in self.valid_words:
                    # If valid, continue
                    self.verify_row(entered_text)
                    self.update_callback(entered_text, self.selected_row_number)
                    if self.selected_row_number != 6:
                        self.selected_row_number += 1
                        if self.has_sound:
                            self.erase_row_as_precaution()
                        self.selected_letter_number = 1
                self.already_checking = False

    def disable_type_handing(self):
        self.master.master.unbind("<KeyPress>")

    def enable_type_handling(self):
        self.master.master.bind("<KeyPress>", self.handle_type)

    def erase_row_as_precaution(self):
        # This function erases the next row always so that if the player typed whilst the program checked then their input is discarded
        for widget in self.texts[self.selected_row_number - 1]:
            self.master.update()
            self.master.itemconfig(widget, text="")

    def verify_play_sound(self, sound):
        if self.has_sound and self.has_slow_reveal:
            self.master.update()
            self.sound_system.force_play(sound, False)
            self.master.after(80)

    def verify_row(self, entered_text):
        boxes = self.boxes[self.selected_row_number - 1]  # Shortening
        # Checking each text
        for letter_index, letter in enumerate(entered_text):
            if letter not in self.word:
                self.master.itemconfig(boxes[letter_index], fill=self.theme["grid_square_incorrect"])
                self.verify_play_sound("incorrect_letter")
            elif letter != self.word[letter_index]:
                self.master.itemconfig(boxes[letter_index], fill=self.theme["grid_square_mismatched"])
                self.verify_play_sound("found_letter")
            else:
                self.master.itemconfig(boxes[letter_index], fill=self.theme["grid_square_correct"])
                self.verify_play_sound("correct_match")

