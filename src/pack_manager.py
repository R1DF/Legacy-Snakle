# Imports
from screen import *
from canvas_ui.button import Button

# Main menu canvas
class PacksManager(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)  # check out if this line is necessary

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Drawing out widgets
        self.back_button = Button(
            self,
            (self.WIDTH // 2) - 130,
            540,
            200,
            70,
            text="Back to Settings",
            conf=self.conf,
            theme=self.theme,
            callback=self.return_to_settings
        )

    def return_to_settings(self):
        self.master.make_settings()
        self.destroy()

