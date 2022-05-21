# Imports
from tkinter import Toplevel, Frame, Listbox, Label
from os import getcwd
import json

# TODO: Add PACKS_PATH attribute to main.py to reduce code in this file and pack_selector_list.py
PACKS_PATH = getcwd() +"\\packs\\"

# FontManager class
class PackInfoShower(Toplevel):
    def __init__(self, master, pack_name):
        # Initialization
        Toplevel.__init__(self, master)
        self.master = master
        self.pack_name = pack_name
        self.pack_data = json.load(open(PACKS_PATH + self.pack_name, "r"))
        self.title(f"Snakle - {self.pack_data['title']}")
        self.geometry("350x400")
        self.resizable(False, False)

        # Delection protocol
        self.protocol("WM_DELETE_WINDOW", self.handle_exit)

        # Drawing widgets
        self.main_frame = Frame(self)
        self.main_frame.pack()

        self.left_frame = Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1)

        # Left frame
        self.words_introduction_label = Label(self.left_frame, text="Words List")
        self.words_introduction_label.pack()

        self.test = Label(self.right_frame, text="test") # testing purposes just to see GUI change
        self.test.pack()

    def handle_exit(self):
        self.master.is_pack_information_shower_open = False
        self.destroy()

