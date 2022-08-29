"""
This is a test screen. (Screens are the menus that open and close when you click a button, e.g. the main menu, the settings menu,
the "start game" menu, the list goes on).
The purpose of this screen is to let you (or me, pfft) to mess around with the canvas_ui widgets and see how they interact.
If you wish to mess around, go to line 19 and write whatever you want. Do not go beyond the lower comment that warns you. (line 21)

To open up the screen, first ensure that in configurations/config.toml, "allow_test_screen" is equal to "true".
Then, in the main menu, press the number 8 on your keyboard.
"""

# Imports
from screen import *
from canvas_ui.file_selector_list import FileSelectorList
# Main menu canvas
class TestScreen(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)  # check out if this line is necessary

    def initiate(self):
        # Screen details
        self.warning = self.create_text(
            self.WIDTH // 2,
            20,
            text="This is a test screen. Press Tab to return."
            )

        # EXPERIMENT WITH CODE HERE!
        self.pack_selector_list = FileSelectorList(
            self,
            self.WIDTH // 2,
            self.HEIGHT // 2,
            300,
            500,
            "packs",
            self.conf,
            self.theme,
            extension="json"
        )


        # DO NOT CODE BELOW UNLESS YOU KNOW WHAT YOU'RE DOING!
        # Binding return function
        self.master.bind("<Tab>", self.back, add="+")

    def back(self, event=None):
        self.master.unbind("<Tab>")
        self.master.make_main_menu()
        self.destroy()


