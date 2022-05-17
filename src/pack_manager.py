# Imports
from screen import *
from canvas_ui.button import Button
from pack_finder import PackFinder
from canvas_ui.pack_selector_list import PackSelectorList

# Main menu canvas
class PacksManager(Screen):
    def __init__(self, master, theme, conf):
        Screen.__init__(self, master, theme, conf)  # check out if this line is necessary
        self.event = None # contains x and y mouse position

    def initiate(self):
        # Filling with theme
        self.config(bg=self.theme["bg"])
        self.pack_finder = PackFinder(self, "\\packs")

        # Drawing out widgets
        self.intro_text = self.create_text(
            self.WIDTH // 2,
            50,
            text="Packs",
            font=[self.FONT, self.TEXT_SIZES["huge"]]
        )

        self.create_line(  # Divider
            0,
            95,
            self.WIDTH,
            95,
            fill=self.theme["line_fill"],
            width=2
        )

        self.pack_selector_list = PackSelectorList(
            self,
            self.WIDTH // 2,
            self.HEIGHT // 2 - 30,
            425,
            300,
            conf=self.conf,
            theme=self.theme,
            additional_callback=self.synchronize_selector
        )

        self.selected_pack_shower = self.create_text(
            (self.WIDTH // 2) - 120,
            460,
            text="Selected pack:\nN/A",
            font=[self.FONT, self.TEXT_SIZES["mid"]],
            justify="center"
        )

        self.previous_theme_button = Button(
            self,
            (self.WIDTH // 2) + 40,
            460,
            40,
            40,
            text="<",
            theme=self.theme,
            conf=self.conf
        )

        self.page_shower = self.create_text(
            (self.WIDTH // 2) + 120,
            460,
            text="Page 1",
            font=[self.FONT, self.TEXT_SIZES["mid"]],
        )

        self.next_theme_button = Button(
            self,
            (self.WIDTH // 2) + 200,
            460,
            40,
            40,
            text=">",
            theme=self.theme,
            conf=self.conf
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

    def synchronize_selector(self):
        if self.pack_selector_list.selected is not None:
            self.itemconfig(
                self.selected_pack_shower,
                text=f"Selected pack:\n{self.pack_selector_list.selected.file_title[:17]+'...'if len(self.pack_selector_list.selected.file_title) > 17 else self.pack_selector_list.selected.file_title}"
        )
        else:
            self.itemconfig(self.selected_pack_shower, text="Selected pack:\nN/A")

