# Imports
from screen import *
from canvas_ui.button import Button
from necessary_defaults import THEMES_PATH, DEFAULT_THEME
from themes import Themes
from settings_p1 import Settings

# Main menu canvas
class MainMenu(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf) # check out if this line is necessary
    
    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Drawing out widgets
        self.intro_text = self.create_text(
            self.WIDTH//2,
            50,
            text="Snakle",
            font=[self.FONT_FAMILY, self.TEXT_SIZES["huge"]]
        )

        self.start_button = Button(
            self,
            self.WIDTH//2,
            160,
            400,
            70,
            conf=self.conf,
            theme=self.theme,
            text="New Snakle"
        )

        self.themes_button = Button(
            self,
            self.WIDTH // 2,
            250,
            400,
            70,
            conf=self.conf,
            theme=self.theme,
            text="Themes",
            callback=self.manage_themes
        )

        self.settings_button = Button(
            self,
            self.WIDTH // 2,
            340,
            400,
            70,
            conf=self.conf,
            theme=self.theme,
            text="Settings",
            callback=self.show_settings
        )

        self.exit_button = Button(
            self,
            self.WIDTH // 2,
            430,
            400,
            70,
            conf=self.conf,
            theme=self.theme,
            text="Exit",
            callback=exit
        )

        self.version_text = self.create_text(
            self.WIDTH-55,
            self.HEIGHT-20,
            text="unreleased",
            font=[self.FONT_FAMILY, self.TEXT_SIZES["small"]]
        )

    def manage_themes(self):
        self.master.themes = Themes(self.master, self.master.theme_loader.load_theme(THEMES_PATH + DEFAULT_THEME),
                                        self.conf)
        self.master.themes.pack(expand=1, fill="both")
        self.destroy()

    def show_settings(self):
        self.master.make_settings()
        self.destroy()

