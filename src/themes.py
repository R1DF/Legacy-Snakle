# Imports
from screen import *
from canvas_ui.button import Button
from necessary_defaults import THEMES_PATH, DEFAULT_THEME


# Main menu canvas
class Themes(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)  # check out if this line is necessary

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Drawing out widgets
        self.intro_text = self.create_text(
            self.WIDTH // 2,
            50,
            text="Themes",
            font=[self.FONT_FAMILY, self.TEXT_SIZES["huge"]]
        )

        self.back_button = Button(
            self,
            self.WIDTH // 2,
            540,
            400,
            70,
            text="Back to Menu",
            conf=self.conf,
            theme=self.theme,
            callback=self.return_to_menu
        )

    def return_to_menu(self):
        self.master.make_main_menu()
        self.destroy()
