# Imports
from tkinter import Canvas, PhotoImage
from sound_system import SoundSystem
from .is_inside import is_inside


# ImageButton class
class ImageButton:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset_x,
            offset_y,
            conf,
            theme,
            image_path,
            callback=lambda: None
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x-(offset_x//2), y-(offset_y//2), x+(offset_x//2), y+(offset_y//2))
        self.theme = theme
        self.image_path = image_path
        self.callback = callback
        self.sound_system = SoundSystem(conf)

        # Drawing
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["button_fill"])
        self.image_object = PhotoImage(file=self.image_path)
        self.image = self.master.create_image(x, y, image=self.image_object)
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
            self.sound_system.play("button_clicked")

