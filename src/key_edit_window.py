# Imports
from tkinter import Toplevel, Label, Entry, Frame, Button
from os import getcwd

# Making the adder window
class URLConfigurator(Toplevel):
    def __init__(self, master):
        # Initialization
        Toplevel.__init__(self, master)
        self.master = master
        self.title("Configure URL")
        self.master.opened_url_configurator = True
        self.geometry("470x70")
        self.resizable(False, False)

        # Drawing
        self.intro_label = Label(self, text="Enter URL")
        self.intro_label.pack()

        self.url_entry = Entry(self)
        self.url_entry.pack(fill="x")

        self.buttons_frame = Frame(self)
        self.buttons_frame.pack()

        self.close_button = Button(self.buttons_frame, text="Close", command=self.close, padx=15)
        self.close_button.grid(row=0, column=0)

        self.play_button = Button(self.buttons_frame, text="Play", command=self.play, padx=15)
        self.play_button.grid(row=0, column=1)

        # Inserting default URL
        self.insert_default_url()

    def close(self):
        self.master.url_configurator = None
        self.master.opened_url_configurator = False
        self.destroy()

    def play(self):
        pass

    def insert_default_url(self):
        self.url_entry.insert(0, open(getcwd() + "\\configurations\\key.txt", "r").read().strip())

