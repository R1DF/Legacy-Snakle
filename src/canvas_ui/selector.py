# Imports
from tkinter import Canvas
from .is_inside import is_inside


# Selector class
class Selector:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset_x,
            offset_y,
            left_offset,
            right_offset,
            conf,
            theme,
            default_value_index=0,
            values=[""]
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x - (offset_x // 2), y - (offset_y // 2), x + (offset_x // 2), y + (offset_y // 2))
        self.theme = theme
        self.text_data = conf.get("text")
        self.values = values
        self.default_value_index = default_value_index
        self.value_index = self.default_value_index
        self.value = self.values[self.default_value_index]
        self.left_offset = left_offset
        self.right_offset = right_offset

        # Drawing
        self.value_rect = self.master.create_rectangle(
            *self.init_coordinates,
            width=2,
            fill=self.theme["selector_fill"]
        )

        self.value_label = self.master.create_text(
            x,
            y,
            text=self.value,
            fill=self.theme["text_fill"],
            font=[self.master.FONT, self.text_data["text_size_mid"]]
        )

        self.left_input_field = self.master.create_rectangle(
            x - (offset_x // 2) - left_offset,
            y - (offset_y // 2),
            x - (offset_x // 2),
            y + (offset_y // 2),
            fill=self.theme["selector_fill"],
            width=2
        )

        self.left_input_text = self.master.create_text(
            x - (offset_x // 2) - (left_offset // 2),
            y,
            text="\u2190",
            font=[self.master.FONT, self.text_data["text_size_mid"]],
            fill=self.theme["text_fill"]
        )

        self.right_input_field = self.master.create_rectangle(
            x + (offset_x // 2) + right_offset,
            y - (offset_y // 2),
            x + (offset_x // 2),
            y + (offset_y // 2),
            fill=self.theme["selector_fill"],
            width=2
        )

        self.right_input_text = self.master.create_text(
            x + (offset_x // 2) + (right_offset // 2),
            y,
            text="\u2192",
            font=[self.master.FONT, self.text_data["text_size_mid"]],
            fill=self.theme["text_fill"]
        )

        # Binding
        self.master.bind("<Motion>", self.handle_motion, add="+")
        self.master.bind("<Button-1>", self.handle_lclick, add="+")

    def handle_motion(self, event):
        # this stuff smells like yandere dev code bruh - r1df
        if is_inside(event, self.init_coordinates):
            self.master.itemconfig(self.value_rect, fill=self.theme["selector_highlight"])
            self.master.itemconfig(self.right_input_field, fill=self.theme["selector_fill"])
            self.master.itemconfig(self.left_input_field, fill=self.theme["selector_fill"])
        elif is_inside(event, self.master.bbox(self.right_input_field)):
            self.master.itemconfig(self.value_rect, fill=self.theme["selector_fill"])
            self.master.itemconfig(self.right_input_field, fill=self.theme["selector_highlight"])
            self.master.itemconfig(self.left_input_field, fill=self.theme["selector_fill"])
        elif is_inside(event, self.master.bbox(self.left_input_field)):
            self.master.itemconfig(self.value_rect, fill=self.theme["selector_fill"])
            self.master.itemconfig(self.right_input_field, fill=self.theme["selector_fill"])
            self.master.itemconfig(self.left_input_field, fill=self.theme["selector_highlight"])
        else:
            self.master.itemconfig(self.value_rect, fill=self.theme["selector_fill"])
            self.master.itemconfig(self.right_input_field, fill=self.theme["selector_fill"])
            self.master.itemconfig(self.left_input_field, fill=self.theme["selector_fill"])

    def handle_lclick(self, event):
        if is_inside(event, self.master.bbox(self.left_input_field)):
            self.value_index = self.value_index if self.value_index == 0 else self.value_index - 1 # ternary condition to make sure you can't go back before 0
            self.value = self.values[self.value_index]
            self.master.itemconfig(self.value_label, text=self.value)
        elif is_inside(event, self.master.bbox(self.right_input_field)):
            self.value_index = self.value_index if self.value_index == len(self.values)-1 else self.value_index + 1 # basically same as above but to the right
            self.value = self.values[self.value_index]
            self.master.itemconfig(self.value_label, text=self.value)

