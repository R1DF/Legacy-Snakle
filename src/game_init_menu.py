# Imports
import json
from screen import *
from canvas_ui.button import Button
from canvas_ui.file_selector_list import FileSelectorList
from clearance_checker import ClearanceChecker
from os import getcwd


# Game initialization canvas
class GameInitMenu(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)
        self.opened_url_configurator = False
        ClearanceChecker(getcwd() + "\\packs\\").check_files()  # make sure all clearance files are intact

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Drawing out widgets
        self.create_text(
            self.WIDTH // 2,
            30,
            text="Select offline pack:",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.pack_selector_list = FileSelectorList(
            self,
            self.WIDTH // 2,
            210,
            425,
            300,
            overlooked_directory= getcwd() + "\\packs\\",
            conf=self.conf,
            theme=self.theme,
            extension="json",
            file_type="pack",
            additional_callback=self.synchronize_selector,
            callback_upon_selected_click=self.play
        )

        self.selected_pack_shower = self.create_text(
            (self.WIDTH // 2) - 120,
            400,
            text="Selected pack:\nN/A",
            font=[self.FONT, self.TEXT_SIZES["mid"]],
            justify="center"
        )

        self.previous_page_button = Button(
            self,
            (self.WIDTH // 2) + 40,
            400,
            40,
            40,
            text="<",
            theme=self.theme,
            conf=self.conf,
            callback=self.previous_page
        )

        self.page_shower = self.create_text(
            (self.WIDTH // 2) + 120,
            400,
            text="Page 1",
            font=[self.FONT, self.TEXT_SIZES["mid"]],
        )

        self.next_page_button = Button(
            self,
            (self.WIDTH // 2) + 200,
            400,
            40,
            40,
            text=">",
            theme=self.theme,
            conf=self.conf,
            callback=self.next_page
        )

        self.create_line(  # Divider
            0,
            440,
            self.WIDTH,
            440,
            fill=self.theme["line_fill"],
            width=2
        )

        self.words_amount_text = self.create_text(
            self.WIDTH // 2,
            480,
            text="Words: N/A",
            font=[self.FONT, self.TEXT_SIZES["mid"]]
        )

        self.back_button = Button(
            self,
            self.WIDTH // 2,
            550,
            400,
            60,
            text="Back",
            theme=self.theme,
            conf=self.conf,
            callback=self.return_to_main_menu
        )

    def return_to_main_menu(self):
        self.master.make_main_menu()
        self.destroy()

    def synchronize_selector(self):
        if self.pack_selector_list.selected_selector is not None:
            words = len(
                json.load(open(getcwd() + "\\packs\\" + self.pack_selector_list.selected_selector.file_name))["words"])
            self.itemconfig(self.words_amount_text, text=f"Words: {words}")

            self.itemconfig(
                self.selected_pack_shower,
                text=f"Selected pack:\n{self.pack_selector_list.selected_selector.file_title[:17]+'...'if len(self.pack_selector_list.selected_selector.file_title) > 17 else self.pack_selector_list.selected_selector.file_title}"
        )
        else:
            self.itemconfig(self.words_amount_text, text="Words: N/A")
            self.itemconfig(self.selected_pack_shower, text="Selected pack:\nN/A")

    def next_page(self):
        if self.pack_selector_list.current_page < self.pack_selector_list.max_page_amount:
            # Drawing out the selectors
            self.pack_selector_list.clear()
            self.pack_selector_list.current_page += 1
            self.pack_selector_list.draw_page(self.pack_selector_list.current_page)

            # Modifying the page text
            self.itemconfig(self.page_shower, text=f"Page {self.pack_selector_list.current_page}")

    def previous_page(self):
        if self.pack_selector_list.current_page > 1:
            # Drawing out the selectors
            self.pack_selector_list.clear()
            self.pack_selector_list.current_page -= 1
            self.pack_selector_list.draw_page(self.pack_selector_list.current_page)

            # Modifying the page text
            self.itemconfig(self.page_shower, text=f"Page {self.pack_selector_list.current_page}")

    def play(self):
        self.master.make_game(json.load(open(getcwd() + "\\packs\\" + self.pack_selector_list.selected_selector.file_name, "r")), self.pack_selector_list.selected_selector.file_name)
        self.destroy()

