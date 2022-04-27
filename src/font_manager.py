# Imports
from tkinter import Toplevel, Frame, Listbox, Label, Button

# FontManager class
class FontManager(Toplevel):
    def __init__(self, master):
        # Initialization
        Toplevel.__init__(self, master)
        self.master = master
        self.master.is_font_manager_open = True
        self.title("Snakle - Fonts")
        self.geometry("600x400")
        self.protocol("WM_DELETE_WINDOW", self.handle_exit)

    def handle_exit(self):
        self.master.is_font_manager_open = False
        self.destroy()

