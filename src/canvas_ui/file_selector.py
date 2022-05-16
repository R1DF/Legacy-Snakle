## TODO: rename class to PackSelector, ThemeSelector will have something else

# Imports
import json  # For packs
import os

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

        # Drawing
        self.rect = self.master.master.create_rectangle(
            *self.init_coordinates,
            fill=self.theme["selector_element_fill"],
            width=2
        )

        # Displaying data
        self.configure_display()

    def configure_display(self):
        # Getting file data
        self.file = json.load(open(os.getcwd() + "\\packs\\" + self.file_name, "r"))

        # Displays
        self.pack_title_text = self.master.master.create_text(
            self.x - 70, #self.init_coordinates[0] + (len(self.file["title"][:20] * 6) * 1.1),
            self.init_coordinates[1] + 20,
            text=self.file["title"] if len(self.file["title"]) <= 20 else self.file["title"][:20]+"...",
            font=[self.master.master.FONT, self.text_data["text_size_mid"]],
            justify="left"
        )

