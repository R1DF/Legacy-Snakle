# Imports
from tkinter import Canvas, Tk

# Screen template
class Screen(Canvas):
    def __init__(self, master):
        self.master = master # make master available to class
        Canvas.__init__(self, self.master)

        # Drawing the screen
        self.initiate()
    
    def initiate(self):
        pass # Gets defined with every individual screen

