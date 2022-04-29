# Imports
from tkinter import Canvas
from .is_inside import is_inside

# Button class
class LoadingBar:
    def __init__(
            self,
            master,
            x,
            y,
            offset_x,
            offset_y,
            theme,
            conf,
            starting_value = 0,
            max_value=100
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x-(offset_x//2), y-(offset_y//2), x+(offset_x//2), y+(offset_y//2))
        self.theme = theme
        self.conf = conf
        self.value = starting_value
        self.max_value = max_value

        # Drawing out the widget
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2)

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

