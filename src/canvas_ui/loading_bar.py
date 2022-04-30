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
        self.length = offset_x # x offset is the same as length
        self.current_state_x1 = self.current_state_x2 = x - (offset_x // 2) # used for showing the loading
        self.residue = [] # This array will contain the rectangles that display value changes.

        # Drawing out the widget
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2)


    def increment(self, change=1):
        """
        This function increments a loading bar's value and displays it on the screen.
        We draw a small, inscribed rectangle inside self.rect to display the change, filling it with the colour matching the theme.
        The Y positions of the inscribed rectangle are the same as the Y positions of the full widget (inscribed rectangle).

        The X positions are not the same, but using math they can be calculated.
        Since we can prove that the x offset is the same as the widget's length, we will use the terms interchangeably.
        We get the first X position (from the start) by knowing it's the same as the starting X position of self.rect.
        The first X position then becomes equal to the second X position in each change.
        The second X position is calculated by getting the first X position and adding the "change factor" -
        which is the length divided by the maximum value, then multiplied by how much the loading bar's value increases.
        """
        if self.value + change <= self.max_value:
            self.value += change
            self.current_state_x2 = self.current_state_x1 + ((self.length/self.max_value) * change)
            self.residue.append(self.master.create_rectangle(
                self.current_state_x1,
                self.master.bbox(self.rect)[1],
                self.current_state_x2,
                self.master.bbox(self.rect)[3],
                fill=self.theme["loading_bar_increase_fill"],
                width=0
            ))
            self.current_state_x1 = self.current_state_x2
            self.master.tag_raise(self.rect) # Must move the loading bar's rectangle to the front to make the border visible

    def decrement(self, change=1):
        pass