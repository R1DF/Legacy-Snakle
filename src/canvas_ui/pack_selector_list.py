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
        self.selected = None

        # Drawing rectangle
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["selector_list_fill"])

        # Drawing out page
        self.draw_page(1)

    def draw_page(self, number):
        # Preparations before drawing
        self.clear() # Clears the canvas
        packs_of_page = self.packs[((number-1) * 4):(number * 4 if number * 4 <= len(self.packs) else len(self.packs))] # Used slicing to get the correct part of the packs list to draw out

        # Drawing out
        for o in range(len(packs_of_page)): # o ---> order of item
            self._selector_items.append(FileSelector(
                self,
                self.x,
                ((o + 2) * self.offset_y//4) + 7,  # 7 is the magic number to make the space fully conquered
                self.offset_x,
                self.offset_y // 4,
                file_name=packs_of_page[o],
                theme=self.theme,
                conf=self.conf
            ))

            if len(packs_of_page) != 4:
                self.closing_line = self.master.create_line(
                    self.init_coordinates[0],
                    self._selector_items[len(self._selector_items) - 1].init_coordinates[3] + 1,
                    self.init_coordinates[2],
                    self._selector_items[len(self._selector_items) - 1].init_coordinates[3] + 1,
                    width=2
                )


    def clear(self):
        pass

    def select(self, selector: FileSelector):
        self.selected.deselect()
        self.selected = selector
        self.selected.select()

        # TODO: Nullify selector when the click area doesn't reach any selector

