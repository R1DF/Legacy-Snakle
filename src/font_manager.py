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

        # Building widgets
        self.left_frame = Frame(self)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = Frame(self)
        self.right_frame.grid(row=0, column=1)

        # Left frame (fonts overview)
        self.fonts_label = Label(self.left_frame, text="List of fonts:")
        self.fonts_label.pack()

        self.fonts_listbox = Listbox(self.left_frame, width=50, height=23)
        self.fonts_listbox.pack(expand="1")

    def handle_exit(self):
        self.master.is_font_manager_open = False
        self.destroy()

