# Imports
from screen import *
from canvas_ui.button import Button
from necessary_defaults import THEMES_PATH, DEFAULT_THEME
from canvas_ui.file_selector_list import FileSelectorList
from os import getcwd
from tkinter import messagebox
import toml


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
            font=[self.FONT, self.TEXT_SIZES["huge"]]
        )

        self.create_line(  # Divider
            0,
            95,
            self.WIDTH,
            95,
            fill=self.theme["line_fill"],
            width=2
        )

        self.theme_selector_list = FileSelectorList(
            self,
            self.WIDTH // 2,
            self.HEIGHT // 2 - 30,
            425,
            270,
            getcwd() + "\\themes\\",
            conf=self.conf,
            theme=self.theme,
            file_type="theme",
            additional_callback=self.synchronize_selector,
            callback_upon_selected_click=self.switch_theme
        )

        self.selected_theme_shower = self.create_text(
            (self.WIDTH // 2) - 120,
            445,
            text="Selected theme:\nN/A",
            font=[self.FONT, self.TEXT_SIZES["mid"]],
            justify="center"
        )

        self.create_line(
            0,
            485,
            self.WIDTH,
            485,
            fill=self.theme["line_fill"],
            width=2
        )

        self.previous_page_button = Button(
            self,
            (self.WIDTH // 2) + 40,
            445,
            40,
            40,
            text="<",
            theme=self.theme,
            conf=self.conf,
            callback=self.previous_page
        )

        self.page_shower = self.create_text(
            (self.WIDTH // 2) + 120,
            445,
            text="Page 1",
            font=[self.FONT, self.TEXT_SIZES["mid"]],
        )

        self.next_page_button = Button(
            self,
            (self.WIDTH // 2) + 200,
            445,
            40,
            40,
            text=">",
            theme=self.theme,
            conf=self.conf,
            callback=self.next_page
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

    def synchronize_selector(self):
        if self.theme_selector_list.selected_selector is not None:
            self.itemconfig(
                self.selected_theme_shower,
                text=f"Selected theme:\n{self.theme_selector_list.selected_selector.file_title[:17]+'...'if len(self.theme_selector_list.selected_selector.file_title) > 17 else self.theme_selector_list.selected_selector.file_title}"
        )

        else:
            self.itemconfig(self.selected_theme_shower, text="Selected theme:\nN/A")

    def previous_page(self):
        if self.theme_selector_list.current_page > 1:
            # Drawing out the selectors
            self.theme_selector_list.clear()
            self.theme_selector_list.current_page -= 1
            self.theme_selector_list.draw_page(self.theme_selector_list.current_page)

            # Modifying the page text
            self.itemconfig(self.page_shower, text=f"Page {self.theme_selector_list.current_page}")

    def next_page(self):
        if self.theme_selector_list.current_page < self.theme_selector_list.max_page_amount:
            # Drawing out the selectors
            self.theme_selector_list.clear()
            self.theme_selector_list.current_page += 1
            self.theme_selector_list.draw_page(self.theme_selector_list.current_page)

            # Modifying the page text
            self.itemconfig(self.page_shower, text=f"Page {self.theme_selector_list.current_page}")

    def switch_theme(self):
        selected_theme_file = self.theme_selector_list.selected_selector.file_name
        toml.dump({
            "default": selected_theme_file
        }, open(getcwd() + "\\default_theme.toml", "w"))
        messagebox.showinfo("Update detected", "Due to an update in the game data, the game must be restarted to "
                                               "apply the new settings. Click OK to proceed.")
        quit()