# Imports
from tkinter import Canvas
from .list_selector import ListSelector
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
        self.conf = conf
        self.theme = theme
        self.packs = [x for x in listdir(PACKS_PATH) if x.split(".")[1] == "json"] # Only files with the JSOn extension in the "packs" directory are included

        # Drawing rectangle
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["selector_list_fill"])

        # Drawing out page
        self.draw_page(1)

    def draw_page(self, number):
        pass

    def clear(self):
        pass

