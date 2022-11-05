# Imports
import os
import sys
from screen import *
from canvas_ui.button import Button
from canvas_ui.selector import Selector
from necessary_defaults import THEMES_PATH, DEFAULT_THEME
from pack_manager_screen import PacksManager
from config_changer import ConfChange
from tkinter import messagebox


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

        self.create_line(  # This serves just as a divider between the title and settings
            0,
            95,
            self.WIDTH,
            95,
            fill=self.theme["line_fill"],
            width=2
        )

        self.delete_clearance_residue_text = self.create_text(
            self.WIDTH // 2,
            120,
            text="Delete Clearance Data:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.delete_clearance_residue_button = Button(
            self,
            (self.WIDTH // 2) - 120,
            170,
            230,
            50,
            self.conf,
            self.theme,
            text="Residue Only",
            callback=self.delete_clearance_residue
        )

        self.reset_clearance_data_button = Button(
            self,
            (self.WIDTH // 2) + 120,
            170,
            230,
            50,
            self.conf,
            self.theme,
            text="Reset All",
            callback=self.reset_clearance_data
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
            values=["Sound ON", "Sound OFF"],
            default_value_index=0 if self.conf.get("game")["has_sound"] else 1

        )

        self.manage_animation_text = self.create_text(
            self.WIDTH // 2,
            330,
            text="Reveal Type (only with sound):",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.reveal_on_sound_type = Selector(
            self,
            self.WIDTH // 2,
            380,
            190,
            50,
            40,
            40,
            self.conf,
            self.theme,
            values=["Progressive", "Instant"],
            default_value_index=0 if self.conf.get("game")["progressive_reveal_on_sound"] else 1

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

    def delete_clearance_residue(self):
        clearance_files = [x for x in os.listdir(os.getcwd() + "\\clearance_data\\") if x.endswith(".json") and x.startswith("c_")]
        for file in clearance_files:
            if not os.path.exists(os.getcwd() + "\\packs\\" + file[2:]):
                os.remove(os.getcwd() + "\\clearance_data\\" + file)
        messagebox.showinfo("Success", "All residue was deleted.")

    def reset_clearance_data(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to reset all clearance data? This means all your progress will be lost!"):
            files = [x for x in os.listdir(os.getcwd() + "\\clearance_data\\") if x.endswith(".json") and x.startswith("c_")]
            for file in files:
                os.remove(os.getcwd() + "\\clearance_data\\" + file)
            messagebox.showinfo("Success", "All progress was deleted.")

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
        # Resolution is a constant
        conf_to_merge["window"]["resolutions"] = [[500, 600]]
        conf_to_merge["window"]["default_resolution_index"] = 0

        # Checking if the sound has been toggled
        conf_to_merge["game"]["has_sound"] = self.manage_sound_selector.value == "Sound ON"

        # Checking if the word animation has been toggled
        conf_to_merge["game"]["progressive_reveal_on_sound"] = self.reveal_on_sound_type.value == "Progressive"

        # Adding constant value
        conf_to_merge["game"]["allow_test_screen"] = False

        # Getting the ConfChange class, determining if a restart is required and checking if there's been actual changes
        conf_change = ConfChange(self, self.conf.toml_data, conf_to_merge, os.getcwd()+"\\configurations")
        if conf_change.is_updated():
            conf_change.upload()
            messagebox.showinfo("Update detected", "Due to an update in the game data, the game must be restarted to "
                                                   "apply the new settings. Click OK to proceed.")
            sys.exit()
        else:
            messagebox.showerror("No changes", "No changes were detected.")

