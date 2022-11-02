# Imports
from tkinter import Canvas
from .is_inside import is_inside

# Box class
class Box:
    def __init__(self, master, x, y):
        pass

# Table class
class WordTable:
    def __init__(
            self,
            master: Canvas,
            x,
            starting_y,
            offset,
            gap_x,
            conf,
            theme
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

        # Drawing
        self.boxes = []
        for y_index in range(1, 7):
            row = []
            for x_index in range(5):
                # WARNING: LOOKING AT THE CODE BELOW MIGHT MAKE YOU LOSE YOUR SANITY.
                row.append(self.master.create_rectangle(
                    (x_index * self.square_width) + (x_index * self.gap_length) + (self.center_x - (self.width // 2)),
                    (y_index * self.square_width) + (y_index * self.gap_length) + (self.center_x - (self.height // 2)) + (self.start_y - (self.height // 2)),
                    (x_index * self.square_width) + (x_index * self.gap_length) + (self.center_x - (self.width // 2)) + self.square_width,
                    (y_index * self.square_width) + (y_index * self.gap_length) + (self.center_x - (self.height // 2)) + (self.start_y - (self.height // 2)) + self.square_width,
                    width=2,
                    fill=self.theme["grid_square_fill"],
                    outline=self.theme["grid_square_border"]
                ))
            self.boxes.append(row)

