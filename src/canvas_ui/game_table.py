# Imports
from tkinter import Canvas
from .is_inside import is_inside

# Button class
class Button:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset,
            gap_x,
            conf,
            theme
    ):
        # Initialization
        self.master = master
        self.center_x, self.center_y = x, y
        self.square_width = offset
        self.gap_length = gap_x
        self.conf = conf
        self.theme = theme
        self.width = (5 * self.square_width) + (4 * self.gap_length)
        self.length = (6 * self.square_width) + (5 * self.gap_length)

