# Imports
from tkinter import Canvas
from sound_system import SoundSystem
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
        self.sound_system = SoundSystem(conf)
        self.shown = True
        
        # Drawing
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["button_fill"])
        self.label = self.master.create_text(x, y, text=self.text,
                                             fill=self.theme["text_fill"], font=[self.master.FONT,
                                                                                 self.text_data["text_size_mid"]])

        # Binding
        self.master.bind("<Motion>", self.handle_motion, add="+")
        self.master.bind("<Button-1>", self.handle_lclick, add="+")

    def hide(self):
        self.shown = False
        self.master.itemconfig(self.rect, state="hidden")
        self.master.itemconfig(self.label, state="hidden")

    def show(self):
        self.shown = True
        self.master.itemconfig(self.rect, state="normal")
        self.master.itemconfig(self.label, state="normal")

    def handle_motion(self, event):
        if is_inside(event, self.init_coordinates):
            self.master.itemconfig(self.rect, fill=self.theme["button_highlight"])
        else:
            self.master.itemconfig(self.rect, fill=self.theme["button_fill"])

    def handle_lclick(self, event):
        if is_inside(event, self.init_coordinates) and self.shown:
            self.callback()
            self.sound_system.play("button_clicked")

