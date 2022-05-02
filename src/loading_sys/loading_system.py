# Imports
from tkinter import Canvas # Used for typing
import os

# Loading system class
class LoadingSystem:
    def __init__(
            self,
            master: Canvas,
            loading_bar,
            location_of_interest,
            ext="json"
    ):
        """
        This class will be used to manage gathered data increase while also incrementing loading bars to add a live effect.
        It has to be linked with a master screen and a loading bar.
        """
        # Initialization
        self.master = master
        self.linked_loading_bar = loading_bar
        self.location_of_interest = os.getcwd() + location_of_interest
        self.ext = ext

        self._output = [] # Gets increased with the recurring function, privatized

    def recur_start(self, index=0):
        """
        This function is used to start the system. Recursion is used here to remove the possibility of freezing the window.
        Every time this function is called, with a specified index, the system will add the item of a list it's checking (specified by index) to its own.
        However, if the index has reached beyond the maximum, the function stops to prevent an infinite loop.
        """
        if index == len(os.listdir(self.location_of_interest)):
            return self._output
        else:
            if os.listdir(self.location_of_interest)[index].split(".")[1] == self.ext:
                self._output.append(os.listdir(self.location_of_interest)[index])
            self.master.after(1000, lambda: self.linked_loading_bar.increment)
            self.recur_start(index+1)

