# Imports
from tkinter import Tk, messagebox, PhotoImage  # window GUI and others
from config_loader import ConfigLoader
from theme_loader import ThemeLoader
from necessary_defaults import *
from main_menu import *
from settings_p1_screen import Settings
from settings_p2_screen import SettingsP2
from font_manager import FontManager
from test_screen import TestScreen
from pack_information_shower import PackInfoShower
from game_init_menu import GameInitMenu
from game_screen import GameScreen
from clearance_checker import ClearanceChecker


# Making the window
class App(Tk):
    def __init__(self):
        # Checking clearance
        ClearanceChecker(os.getcwd()+"\\packs\\").check_files()

        # Initialization of the window
        Tk.__init__(self)
        self.title("Legacy Snakle")

        # Getting configurations
        self.conf = ConfigLoader(CONF_PATH+CONF_FILE)
        self.WIDTH = self.conf.get("window")["resolutions"][self.conf.get("window")["default_resolution_index"]][0]
        self.HEIGHT = self.conf.get("window")["resolutions"][self.conf.get("window")["default_resolution_index"]][1]
        self.FONTS = self.conf.get("text")["fonts"]
        self.FONT = self.FONTS[self.conf.get("text")["default_font_family_index"]]
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.is_font_manager_open = False
        self.is_pack_information_shower_open = False

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

    def make_settings_p2(self):
        self.settings_p2 = SettingsP2(self, self.theme_loader.load_theme(THEMES_PATH + DEFAULT_THEME), self.conf)
        self.settings_p2.pack(expand=1, fill="both")

    def make_game_init_menu(self):
        self.game_init_menu = GameInitMenu(self, self.theme_loader.load_theme(THEMES_PATH+DEFAULT_THEME), self.conf)
        self.game_init_menu.pack(expand=1, fill="both")

    def make_game(self, word_pack, pack_file_name):
        self.game = GameScreen(self, self.theme_loader.load_theme(THEMES_PATH+DEFAULT_THEME), self.conf, word_pack, pack_file_name)
        self.game.pack(expand=1, fill="both")

    def make_test_screen(self):
        self.test_screen = TestScreen(self, self.theme_loader.load_theme(THEMES_PATH+DEFAULT_THEME), self.conf)
        self.test_screen.pack(expand=1, fill="both")

    def make_font_manager(self):
        if not self.is_font_manager_open:
            self.font_manager = FontManager(self)

    def make_pack_information_shower(self, pack_name):
        if not self.is_pack_information_shower_open:
            self.is_pack_information_shower_open = PackInfoShower(self, pack_name)

    def handle_exit(self):
        if messagebox.askyesno("Confirm exit", "Are you sure you want to exit?"):
            sys.exit()


# Creating the window instance
app = App()
app.mainloop()

