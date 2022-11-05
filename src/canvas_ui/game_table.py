# Imports
from tkinter import Canvas
from .is_inside import is_inside

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

            elif event.keysym == "Return" and self.selected_row_number <= 6 and self.selected_letter_number == 6:
                # Verifying whether the entered word is valid
                entered_text = "".join([self.master.itemcget(x, "text") for x in self.texts[self.selected_row_number - 1]])
                if entered_text in self.valid_words:
                    # If valid, continue
                    self.selected_letter_number = 1
                    self.verify_row(entered_text)
                    self.update_callback(entered_text, self.selected_row_number)
                    if self.selected_row_number == 6:
                        self.focused_on = False
                    else:
                        self.selected_row_number += 1

    def verify_row(self, entered_text):
        boxes = self.boxes[self.selected_row_number - 1]  # Shortening
        # Checking each text
        for letter_index, letter in enumerate(entered_text):
            if letter not in self.word:
                self.master.itemconfig(boxes[letter_index], fill=self.theme["grid_square_incorrect"])
            elif letter != self.word[letter_index]:
                self.master.itemconfig(boxes[letter_index], fill=self.theme["grid_square_mismatched"])
            else:
                self.master.itemconfig(boxes[letter_index], fill=self.theme["grid_square_correct"])
