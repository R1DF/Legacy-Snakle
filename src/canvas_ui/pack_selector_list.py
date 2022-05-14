# Imports
from tkinter import Canvas
from .file_selector import FileSelector
from .is_inside import is_inside
from os import getcwd, listdir

# PACKS PATH file
PACKS_PATH = getcwd() +"\\packs\\"

# Pack Selector List class
class PackSelectorList:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset_x,
            offset_y,
            conf,
            theme
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x-(offset_x//2), y-(offset_y//2), x+(offset_x//2), y+(offset_y//2))
        self.x, self.y, self.offset_x, self.offset_y = x, y, offset_x, offset_y
        self.theme = theme
        self.conf = conf
        self.packs = [x for x in listdir(PACKS_PATH) if x.split(".")[1] == "json"] # Only files with the JSOn extension in the "packs" directory are included
        self._selector_items = []

        # Drawing rectangle
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["selector_list_fill"])

        # Drawing out page
        self.draw_page(1)

    def draw_page(self, number):
        # Preparations before drawing
        print(type(self.theme))
        self.clear() # Clears the canvas
        packs_of_page = self.packs[((number-1) * 4):(number * 4 if number * 4 <= len(self.packs) else len(self.packs))] # Used slicing to get the correct part of the packs list to draw out

        # Drawing out
        for o in range(len(packs_of_page)): # o ---> order of item
            print(type(self.theme))
            self._selector_items.append(FileSelector(
                self,
                self.x,
                (self.y - self.offset_y) + (o * (self.offset_y/4)),
                self.offset_x,
                o * (self.offset_y / 4),
                file_name=packs_of_page[o],
                theme=self.theme,
                conf=self.conf
            ))

    def clear(self):
        pass

