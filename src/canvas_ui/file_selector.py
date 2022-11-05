# Imports
import os
import json
import toml
from .is_inside import is_inside
from sound_system import SoundSystem


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
            conf,
            file_type
    ):
        # Initialization
        # Widget attributes
        self.master = master
        self.init_coordinates = (x - (offset_x // 2), y - (offset_y // 2), x + (offset_x // 2), y + (offset_y // 2))
        self.x, self.y = x, y
        self.theme = theme
        self.conf = conf
        self.file_type = file_type
        self.sound_system = SoundSystem(self.conf)

        # Meta and special attributes
        self.file_name = file_name
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
        # Getting file type
        if self.file_type == "pack":
            self.file = json.load(open(os.getcwd() + "\\packs\\" + self.file_name, "r"))
            self.file_title = self.file["title"]
            self.file_date_created = self.file["dateCreated"]
            self.file_author = self.file["creator"]

        elif self.file_type == "theme":
            self.file = toml.load(os.getcwd() + "\\themes\\" + self.file_name)
            self.file_title = self.file["meta"]["name"]
            self.file_date_created = self.file["meta"]["date"]
            self.file_author = self.file["meta"]["author"]

        # Displays
        self.file_title_text = self.master.master.create_text(
            self.init_coordinates[0] + 140,
            self.init_coordinates[1] + 20,
            text=self.file_title if len(self.file_title) <= 20 else self.file_title[:20] + "...",
            font=[self.master.master.FONT, self.text_data["text_size_mid"]],
            justify="left"
        )

        self.file_date_text = self.master.master.create_text(
            self.init_coordinates[0] + 80,
            # might use proportions to figure out how long the X offset should be at line 46
            self.init_coordinates[3] - 20,
            text=self.file_date_created,
            font=[self.master.master.FONT, self.text_data["text_size_mid"]],
            justify="right"
        )

        self.file_creator_text = self.master.master.create_text(
            self.init_coordinates[2] - 50,
            # might use proportions to figure out how long the X offset should be at line 46
            self.init_coordinates[3] - 20,
            text=self.file_author,
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
        self.sound_system.play("file_selected")
        self.is_selected = True
        self.master.master.itemconfig(self.rect, fill=self.theme["selector_element_selected"])

    def deselect(self):
        self.is_selected = False
        self.master.master.itemconfig(self.rect, fill=self.theme["selector_element_fill"])

    def kill(self):
        self.is_selected = False
        self.master.master.delete(self.rect)
        self.master.master.delete(self.file_title_text)
        self.master.master.delete(self.file_date_text)
        self.master.master.delete(self.file_creator_text)

