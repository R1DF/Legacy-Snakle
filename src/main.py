# Imports
from tkinter import Tk, messagebox # window GUI
from config_loader import ConfigLoader
from theme_loader import ThemeLoader
from necessary_defaults import *
from main_menu import *

# Making the window
class App(Tk):
    def __init__(self):
        # Initialization of the window
        Tk.__init__(self)
        self.title("Snakle")

        # Getting configurations
        self.conf = ConfigLoader(CONF_PATH+CONF_FILE)
        self.WIDTH = self.conf.get("window")["width"]
        self.HEIGHT = self.conf.get("window")["height"]
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)

        # Getting theme data
        self.theme_loader = ThemeLoader(self)

        # Loading protocol
        self.protocol("WM_DELETE_WINDOW", self.handle_exit)

        # Making the main menu
        self.make_main_menu()

    def make_main_menu(self):
        self.main_menu = MainMenu(self, self.theme_loader.load_theme(THEMES_PATH+DEFAULT_THEME), self.conf)
        self.main_menu.pack(expand=1, fill="both")

    def handle_exit(self):
        if messagebox.askyesno("Confirm exit", "Are you sure you want to exit?"):
            quit()
        

# Creating the window instance
app = App()
app.mainloop()
