# Imports
from tkinter import Canvas
from .is_inside import is_inside

# Button class
class Button:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset_x,
            offset_y,
            conf,
            theme,
            text="",
            callback=lambda: None
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x-(offset_x//2), y-(offset_y//2), x+(offset_x//2), y+(offset_y//2))
        self.theme = theme
        self.text_data = conf.get("text")
        self.text = text
        self.callback = callback
        
        # Drawing
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["button_fill"])
        self.label = self.master.create_text(x, y, text=self.text,
                                             fill=self.theme["text_fill"], font=[self.master.FONT,
                                                                                 self.text_data["text_size_mid"]])

        # Binding
        self.master.bind("<Motion>", self.handle_motion, add="+")
        self.master.bind("<Button-1>", self.handle_lclick, add="+")

    def handle_motion(self, event):
        if is_inside(event, self.init_coordinates):
            self.master.itemconfig(self.rect, fill=self.theme["button_highlight"])
        else:
            self.master.itemconfig(self.rect, fill=self.theme["button_fill"])

    def handle_lclick(self, event):
        if is_inside(event, self.init_coordinates):
            self.callback()

