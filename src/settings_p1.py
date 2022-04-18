# Imports
from screen import *
from canvas_ui.button import Button
from canvas_ui.selector import Selector
from necessary_defaults import THEMES_PATH, DEFAULT_THEME
from pack_manager import PacksManager

# Main menu canvas
class Settings(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)  # check out if this line is necessary

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Drawing out widgets
        self.intro_text = self.create_text(
            self.WIDTH // 2,
            50,
            text="Settings",
            font=[self.FONT_FAMILY, self.TEXT_SIZES["huge"]]
        )

        self.create_line( # This serves just as a divider between the title and settings
            0,
            95,
            self.WIDTH,
            95,
            fill=self.theme["line_fill"],
            width=2
        )

        self.game_resolution_text = self.create_text(
            self.WIDTH // 2,
            120,
            text="Window Resolution:",
            font=[self.FONT_FAMILY, self.TEXT_SIZES["mid"]]
        )

        self.game_resolution_selector = Selector(
            self,
            self.WIDTH // 2,
            160,
            190,
            50,
            40,
            40,
            self.conf,
            self.theme,
            values=[f"{x}x{y}" for x, y in self.conf.get("window")["resolutions"]] # list comprehensions save the world.

        )

        self.manage_sound_text = self.create_text(
            self.WIDTH // 2,
            220,
            text="Toggle Audio:",
            font=[self.FONT_FAMILY, self.TEXT_SIZES["mid"]]
        )

        self.manage_sound_selector = Selector(
            self,
            self.WIDTH // 2,
            270,
            190,
            50,
            40,
            40,
            self.conf,
            self.theme,
            values=["Sound ON", "Sound OFF"]

        )

        self.manage_animation_text = self.create_text(
            self.WIDTH // 2,
            330,
            text="Toggle Word Reveal Animation:",
            font=[self.FONT_FAMILY, self.TEXT_SIZES["mid"]]
        )

        self.manage_animation_selector = Selector(
            self,
            self.WIDTH // 2,
            380,
            190,
            50,
            40,
            40,
            self.conf,
            self.theme,
            values=["Animated", "Instant"]

        )

        self.create_line(  # Second divider
            0,
            425,
            self.WIDTH,
            425,
            fill=self.theme["line_fill"],
            width=2
        )

        self.manage_packs_button = Button(
            self,
            (self.WIDTH // 2),
            455,
            200,
            40,
            text="Word Packs",
            conf=self.conf,
            theme=self.theme,
            callback=self.go_to_pack_manager
        )

        self.next_page_button = Button(
            self,
            (self.WIDTH // 2) + 200,
            455,
            40,
            40,
            text=">",
            conf=self.conf,
            theme=self.theme
        ) # add a page counter

        self.create_line(  # Another divider woooow
            0,
            485,
            self.WIDTH,
            485,
            fill=self.theme["line_fill"],
            width=2
        )

        self.save_changes_button = Button(
            self,
            (self.WIDTH // 2) + 130,
            540,
            200,
            70,
            text="Save Changes",
            conf=self.conf,
            theme=self.theme
        )

        self.back_button = Button(
            self,
            (self.WIDTH // 2) - 130,
            540,
            200,
            70,
            text="Back to Menu",
            conf=self.conf,
            theme=self.theme,
            callback=self.return_to_menu
        )

    def return_to_menu(self):
        self.master.make_main_menu()
        self.destroy()

    def go_to_pack_manager(self):
        self.master.packs_manager = PacksManager(self.master, self.master.theme_loader.load_theme(THEMES_PATH+DEFAULT_THEME), self.conf)
        self.master.packs_manager.pack(expand=1, fill="both")
        self.destroy()

