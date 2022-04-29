# Imports
from screen import *
from canvas_ui.button import Button
from canvas_ui.loading_bar import LoadingBar

# Main menu canvas
class PacksManager(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)  # check out if this line is necessary
        self.event = None # contains x and y mouse position

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])

        # Drawing out widgets
        self.intro_text = self.create_text(
            self.WIDTH // 2,
            50,
            text="Packs",
            font=[self.FONT, self.TEXT_SIZES["huge"]]
        )

        #Drawing out the loader
        self.loader_intro = self.create_text(
            self.WIDTH // 2,
            (self.HEIGHT // 2) - 50,
            text="Loading...",
            font=[self.FONT, self.TEXT_SIZES["small"]]
        )

        self.loader_loading_bar = LoadingBar(
            self,
            self.WIDTH // 2,
            self.HEIGHT // 2,
            400,
            40,
            self.theme,
            self.conf
        )

        self.create_line(  # Divider
            0,
            95,
            self.WIDTH,
            95,
            fill=self.theme["line_fill"],
            width=2
        )

        self.create_line(  # Divider
            0,
            505,
            self.WIDTH,
            505,
            fill=self.theme["line_fill"],
            width=2
        )

        self.back_button = Button(
            self,
            (self.WIDTH // 2),
            550,
            400,
            60,
            text="Back to Settings",
            conf=self.conf,
            theme=self.theme,
            callback=self.return_to_settings
        )

        # Binding a mouse hovering because if it clicks on the settings button, it needs to pass the event
        self.bind("<Motion>", self.handle_motion, add="+")

    def return_to_settings(self):
        self.master.make_settings()
        self.master.settings.back_button.handle_motion(self.event)
        self.master.settings.save_changes_button.handle_motion(self.event)
        self.destroy()

    def handle_motion(self, event):
        self.event = event

