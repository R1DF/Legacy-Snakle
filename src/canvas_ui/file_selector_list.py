# Imports
from tkinter import Canvas
from .file_selector import FileSelector
from .is_inside import is_inside
from os import getcwd, listdir
from math import ceil  # To get max page conversion

# File Selector List class
class FileSelectorList():
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset_x,
            offset_y,
            overlooked_directory,
            conf,
            theme,
            file_type,
            extension="toml",
            additional_callback=lambda: None,
            callback_upon_selected_click=lambda: None # the function that runs when you click an already selected file
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x-(offset_x//2), y-(offset_y//2), x+(offset_x//2), y+(offset_y//2))
        self.directory_path = overlooked_directory
        self.extension = extension
        self.theme = theme
        self.conf = conf
        self.directory_elements = [x for x in listdir(self.directory_path) if x.split(".")[1] == self.extension]
        self.x, self.y = x, y
        self.file_type = file_type # for FileSelectors

        # Functionality variables
        self.callback = additional_callback
        self.selected_callback = callback_upon_selected_click
        self.current_page = 1
        self.max_page_amount = ceil(len(self.directory_elements)/4)
        self.selected_selector = None
        self.selectors = []
        self.offset_x = self.init_coordinates[2] - self.init_coordinates[0]
        self.offset_y = self.init_coordinates[3] - self.init_coordinates[1]

        # Drawing out main rectangle and page
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["selector_list_fill"])
        self.draw_page(self.current_page)

        # Bindings
        self.master.bind("<Button-1>", self.handle_lclick, add="+")

    def draw_page(self, page_number):
        self.clear()
        packs = self.directory_elements[((page_number-1) * 4):(page_number * 4 if page_number * 4 <= len(self.directory_elements) else len(self.directory_elements))]
        self.current_page = page_number

        # Drawing out
        for o in range(len(packs)): # o ---> order of item
            self.selectors.append(FileSelector(
                self,
                self.x,
                self.master.bbox(self.rect)[1] + ((self.offset_y / 8) * ((2 * o) + 1)),  # 2n+1
                self.offset_x,
                self.offset_y / 4,
                file_name=packs[o],
                theme=self.theme,
                conf=self.conf,
                file_type=self.file_type
            ))

    def clear(self):
        for selector in self.selectors:
            selector.kill()
        self.selectors = []

    def select(self, selector: FileSelector):
        if self.selected_selector is not None:
            self.selected_selector.deselect()
        self.selected_selector = selector
        selector.select()

    def nullify_selection(self):
        if self.selected_selector is not None:
            self.selected_selector.deselect()
            self.selected_selector = None

    def handle_lclick(self, event):
        # Checking if a selected selector was selected again
        if self.selected_selector is not None:
            if is_inside(event, self.master.bbox(self.selected_selector.rect)):
                self.selected_callback()
                return

        # Otherwise...
        for selector in self.selectors:
            if is_inside(event, self.master.bbox(selector.rect)):
                self.select(selector)
                break
        else:  # yeah I use for-elses
            self.nullify_selection()
        self.callback()

