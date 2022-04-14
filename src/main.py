# Imports
from tkinter import Tk, messagebox, PhotoImage # window GUI
from config_loader import ConfigLoader
from theme_loader import ThemeLoader
from necessary_defaults import *
from main_menu import *
from settings_p1 import Settings

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

        # Setting the icon and making the main menu
        self.set_icon()
        self.make_main_menu()

    def set_icon(self):
        self.iconphoto(True, PhotoImage(file="images/snakle_icon_32x32.png"))

    def make_main_menu(self):
        self.main_menu = MainMenu(self, self.theme_loader.load_theme(THEMES_PATH+DEFAULT_THEME), self.conf)
        self.main_menu.pack(expand=1, fill="both")

    def make_settings(self):
        self.settings = Settings(self, self.theme_loader.load_theme(THEMES_PATH+DEFAULT_THEME), self.conf)
        self.settings.pack(expand=1, fill="both")

    def handle_exit(self):
        if messagebox.askyesno("Confirm exit", "Are you sure you want to exit?"):
            quit()
        

# Creating the window instance
app = App()
app.mainloop()
