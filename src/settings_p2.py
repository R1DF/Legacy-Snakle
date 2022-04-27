# Imports
from screen import *
from tkinter import messagebox
from canvas_ui.button import Button
from canvas_ui.selector import Selector
from canvas_ui.scale import Scale
from config_changer import ConfChange
from os import getcwd

# Main menu canvas
class SettingsP2(Screen):
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

        self.create_line(
            0,
            95,
            self.WIDTH,
            95,
            fill=self.theme["line_fill"],
            width=2
        )

        self.selected_font_text = self.create_text(
            self.WIDTH // 2,
            120,
            text="Selected Font:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.selected_font_selector = Selector(
            self,
            self.WIDTH // 2,
            160,
            390,
            50,
            40,
            40,
            self.conf,
            self.theme,
            values=[x if len(x) <= 22 else x[:-10]+"..." for x in self.master.FONTS], # so that the font names don't have to be very long
            default_value_index=self.conf.get("text")["default_font_family_index"]
        )

        self.text_sizes_text = self.create_text(
            self.WIDTH // 2,
            200,
            text="Text Sizes:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.huge_size_text = self.create_text(
            (self.WIDTH // 2) - 70,
            240,
            text="Huge:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.huge_size_scale = Scale(
            self,
            (self.WIDTH // 2) + 70,
            240,
            25,
            20,
            15,
            self.theme,
            self.conf,
            self.conf.get("text")["text_size_huge"],
            min_value=10,
            max_value=60
        )

        self.big_size_text = self.create_text(
            (self.WIDTH // 2) - 70,
            290,
            text="Big:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.big_size_scale = Scale(
            self,
            (self.WIDTH // 2) + 70,
            290,
            25,
            20,
            15,
            self.theme,
            self.conf,
            self.conf.get("text")["text_size_big"],
            min_value=10,
            max_value=60
        )

        self.mid_size_text = self.create_text(
            (self.WIDTH // 2) - 70,
            340,
            text="Medium:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.mid_size_scale = Scale(
            self,
            (self.WIDTH // 2) + 70,
            340,
            25,
            20,
            15,
            self.theme,
            self.conf,
            self.conf.get("text")["text_size_mid"],
            min_value=10,
            max_value=60
        )

        self.small_size_text = self.create_text(
            (self.WIDTH // 2) - 70,
            390,
            text="Small:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.small_size_scale = Scale(
            self,
            (self.WIDTH // 2) + 70,
            390,
            25,
            20,
            15,
            self.theme,
            self.conf,
            self.conf.get("text")["text_size_small"],
            min_value=10,
            max_value=60
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
            text="Page 2",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.manage_fonts_button = Button(
            self,
            (self.WIDTH // 2) + 70,
            455,
            200,
            40,
            text="Manage Fonts",
            conf=self.conf,
            theme=self.theme,
            callback=self.open_font_manager
        )

        self.previous_page_button = Button(
            self,
            (self.WIDTH // 2) - 200,
            455,
            40,
            40,
            text="<",
            conf=self.conf,
            theme=self.theme,
            callback=self.go_to_page_1
        )  # add a page counter

        self.create_line(  # this divider thing is getting boring man
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
            callback=self.save_p2_changes
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

    def open_font_manager(self):
        pass

    def go_to_page_1(self):
        self.master.make_settings()
        self.destroy()

    def save_p2_changes(self):
        conf_to_merge = {"text": {}} # The change-saving process is very similar to the one in P1, just changing different attributes

        # Gathering data
        conf_to_merge["text"]["fonts"] = self.selected_font_selector.values
        conf_to_merge["text"]["default_font_family_index"] = self.selected_font_selector.value_index

        conf_to_merge["text"]["text_size_huge"] = self.huge_size_scale.value
        conf_to_merge["text"]["text_size_big"] = self.big_size_scale.value
        conf_to_merge["text"]["text_size_mid"] = self.mid_size_scale.value
        conf_to_merge["text"]["text_size_small"] = self.small_size_scale.value

        # Using the Confchange class
        conf_change = ConfChange(self, self.conf.toml_data, conf_to_merge, getcwd() + "\\configurations")
        if conf_change.is_updated():
            conf_change.upload()
            messagebox.showinfo("Update detected", "Due to an update in the game data, the game must be restarted to "
                                                   "apply the new settings. Click OK to proceed.")
            quit()
        else:
            messagebox.showerror("No changes", "No changes were detected.")