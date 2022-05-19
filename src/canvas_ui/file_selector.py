## TODO: rename class to PackSelector, ThemeSelector will have something else

# Imports
import json  # For packs
import os
from .is_inside import is_inside

# File Selector class
class FileSelector:
    def __init__(
            self,
            master,
            x,
            y,
            offset_x,
            offset_y,
            file_name,
            theme,
            conf
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x - (offset_x // 2), y - (offset_y // 2), x + (offset_x // 2), y + (offset_y // 2))
        self.x, self.y = x, y
        self.file_name = file_name
        self.theme = theme
        self.conf = conf
        self.text_data = conf.get("text")
        self.file_title = ""
        self.is_selected = False

        # Drawing
        self.rect = self.master.master.create_rectangle(
            *self.init_coordinates,
            fill=self.theme["selector_element_fill"],
            width=2
        )

        # Displaying data
        self.configure_display()

        # Binding
        self.master.master.bind("<Motion>", self.handle_motion, add="+")

    def configure_display(self):
        # Getting file data
        self.file = json.load(open(os.getcwd() + "\\packs\\" + self.file_name, "r"))
        self.file_title = self.file["title"]

        # Displays
        self.pack_title_text = self.master.master.create_text(
            self.init_coordinates[0] + 140,
            self.init_coordinates[1] + 20,
            text=self.file["title"] if len(self.file["title"]) <= 20 else self.file["title"][:20]+"...",
            font=[self.master.master.FONT, self.text_data["text_size_mid"]],
            justify="left"
        )

        self.pack_date_text = self.master.master.create_text(
            self.init_coordinates[0] + 60, # might use proportions to figure out how long the X offset should be at line 46
            self.init_coordinates[3] - 20,
            text=self.file["dateCreated"],
            font=[self.master.master.FONT, self.text_data["text_size_mid"]],
            justify="right"
        )

        self.pack_creator_text = self.master.master.create_text(
            self.init_coordinates[2] - 50,
            # might use proportions to figure out how long the X offset should be at line 46
            self.init_coordinates[3] - 20,
            text=self.file["creator"],
            font=[self.master.master.FONT, self.text_data["text_size_mid"]],
            justify="right"
        )

    def handle_motion(self, event):
        if is_inside(event, self.init_coordinates):
            if not self.is_selected:
                self.master.master.itemconfig(self.rect, fill=self.theme["selector_element_highlight"])
        else:
            if not self.is_selected:
                self.master.master.itemconfig(self.rect, fill=self.theme["selector_element_fill"])
            else:
                self.master.master.itemconfig(self.rect, fill=self.theme["selector_element_selected"])

    def select(self):
        self.is_selected = True
        self.master.master.itemconfig(self.rect, fill=self.theme["selector_element_selected"])

    def deselect(self):
        self.is_selected = False
        self.master.master.itemconfig(self.rect, fill=self.theme["selector_element_fill"])

    def kill(self):
        self.is_selected = False
        self.master.master.delete(self.rect)
        self.master.master.delete(self.pack_title_text)
        self.master.master.delete(self.pack_date_text)
        self.master.master.delete(self.pack_creator_text)
