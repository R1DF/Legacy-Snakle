# Imports
from screen import *
from canvas_ui.button import Button
from canvas_ui.selector import Selector
from necessary_defaults import THEMES_PATH, DEFAULT_THEME
from pack_manager import PacksManager
from config_changer import ConfChange
from tkinter import messagebox
from os import getcwd

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
            font=[self.FONT, self.TEXT_SIZES["huge"]]
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
            font=[self.FONT, self.TEXT_SIZES["mid"]]
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
            values=[f"{x}x{y}" for x, y in self.conf.get("window")["resolutions"]], # list comprehensions save the world.
            default_value_index=self.conf.get("window")["default_resolution_index"]
        )

        self.manage_sound_text = self.create_text(
            self.WIDTH // 2,
            220,
            text="Toggle Audio:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
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
            font=[self.FONT, self.TEXT_SIZES["mid"]]
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

        self.create_text(
            (self.WIDTH // 2) - 105,
            455,
            text="Page 1",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.manage_packs_button = Button(
            self,
            (self.WIDTH // 2) + 70,
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
            theme=self.theme,
            callback=self.go_to_page_2
        )

        self.create_line(
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
            theme=self.theme,
            callback=self.save_p1_changes
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

    def go_to_page_2(self):
        self.master.make_settings_p2()
        self.destroy()

    def save_p1_changes(self):
        conf_to_merge = {"window": {}, "game": {}} # This file contains the data straight from the window

        # Below we are creating new config file with merged data from the old file and the new inputs
        # Because in config.toml resolutions are represented by [L, Y] and in selectors by "LxW", we need to reformat the select res values

        # Might try to make this a list comprehension
        formatted_resolutions = []
        for resolution in self.game_resolution_selector.values:
            formatted_resolutions.append([int(x) for x in resolution.split("x")])

        conf_to_merge["window"]["resolutions"] = formatted_resolutions
        conf_to_merge["window"]["default_resolution_index"] = self.game_resolution_selector.value_index

        # Checking if the sound has been toggled
        conf_to_merge["game"]["has_sound"] = self.manage_sound_selector.value == "Sound ON"

        # Checking if the word animation has been toggled
        conf_to_merge["game"]["has_animation"] = self.manage_animation_selector.value == "Animated"

        # Getting the ConfChange class, determining if a restart is required and checking if there's been actual changes
        conf_change = ConfChange(self, self.conf.toml_data, conf_to_merge, getcwd()+"\\configurations")
        if conf_change.is_updated():
            conf_change.upload()
            messagebox.showinfo("Update detected", "Due to an update in the game data, the game must be restarted to "
                                                   "apply the new settings. Click OK to proceed.")
            quit()
        else:
            messagebox.showerror("No changes", "No changes were detected.")
