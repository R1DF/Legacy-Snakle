# Imports
from .is_inside import is_inside
from .theme_selector import ThemeSelector
from tkinter import Canvas
from os import listdir, getcwd
from math import ceil

# Themes path
THEMES_PATH = getcwd() + "\\themes\\"

# Theme Selector class
class ThemeSelectorList:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset_x,
            offset_y,
            conf,
            theme,
            additional_callback=lambda: None,
            callback_upon_selected_click=lambda: None  # the function that runs when you click an already selected pack
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x - (offset_x // 2), y - (offset_y // 2), x + (offset_x // 2), y + (offset_y // 2))
        self.x, self.y, self.offset_x, self.offset_y = x, y, offset_x, offset_y
        self.theme = theme
        self.conf = conf
        self.themes = [x for x in listdir(THEMES_PATH) if x.split(".")[
            1] == "toml"]  # Only files with the TOML extension in the "themes" directory are included
        self.selector_items = []
        self.selected = None
        self.callback = additional_callback
        self.selected_callback = callback_upon_selected_click
        self.page = 1
        self.max_pages = ceil(len(self.themes) / 4)

        # Drawing rectangle
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["selector_list_fill"])

        # Drawing out page
        self.draw_page(self.page)

        # Bindings
        self.master.bind("<Button-1>", self.handle_lclick, add="+")

    def draw_page(self, number):
        # Preparations before drawing
        self.clear()  # Clears the canvas
        themes_of_page = self.themes[((number - 1) * 4):(number * 4 if number * 4 <= len(self.themes) else len(
            self.themes))]  # Used slicing to get the correct part of the themes list to draw out

        # Drawing out
        for o in range(len(themes_of_page)):  # o ---> order of item
            self.selector_items.append(ThemeSelector(
                self,
                self.x,
                ((o + 2) * self.offset_y // 4) + 34,  # idk why but adding 34 makes the spacing work. god I'm a terrible coder
                self.offset_x,
                self.offset_y // 4,
                file_name=themes_of_page[o],
                theme=self.theme,
                conf=self.conf
            ))

            if len(themes_of_page) != 4:
                self.closing_line = self.master.create_line(
                    self.init_coordinates[0],
                    self.selector_items[len(self.selector_items) - 1].init_coordinates[3] + 1,
                    self.init_coordinates[2],
                    self.selector_items[len(self.selector_items) - 1].init_coordinates[3] + 1,
                    width=2
                )

    def clear(self):
        for selector in self.selector_items:
            # del self.selector_items[self.selector_items.index(selector)] mfw del doesn't work or else the program goes crazy
            selector.kill()

        self.selector_items = []

    def handle_lclick(self, event):
        # Checking if a selected selector was selected again
        if self.selected is not None:
            if is_inside(event, self.master.bbox(self.selected.rect)):
                self.selected_callback()
                return

        # Otherwise...
        for selector in self.selector_items:
            if is_inside(event, self.master.bbox(selector.rect)):
                self.select(selector)
                break
        else:  # yeah I use for-elses
            self.nullify_selector()
        self.callback()

    def select(self, selector: ThemeSelector):
        if self.selected is not None:
            self.selected.deselect()
        self.selected = selector
        self.selected.select()

    def nullify_selector(self):
        if self.selected is not None:
            self.selected.deselect()
            self.selected = None
