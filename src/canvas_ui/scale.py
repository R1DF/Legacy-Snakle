# Imports
from tkinter import Canvas
from .is_inside import is_inside


# Scale class
class Scale:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            number_field_offset_x,
            offset_y,
            input_field_offset_x,
            theme,
            conf,
            default_value,
            min_value=1,
            max_value=99,
            value_increment=1,
            callback_up=lambda: None,
            callback_down=lambda: None
    ):
        # Initialization
        self.master = master
        self.theme = theme
        self.conf = conf
        self.text_data = conf.get("text")
        self.value = default_value
        self.min_value, self.max_value = min_value, max_value
        self.cycle_counter = 0
        self.is_highlighted = False
        self.callback_up = callback_up
        self.callback_down = callback_down

        # Drawing
        self.number_rect = self.master.create_rectangle(
            x - number_field_offset_x - input_field_offset_x,
            y - offset_y,
            x + number_field_offset_x - input_field_offset_x,
            y + offset_y,
            fill=self.theme["scale_fill"]
        )

        self.up_input_field = self.master.create_rectangle(
            x + number_field_offset_x - input_field_offset_x,
            y - offset_y,
            x + number_field_offset_x + input_field_offset_x,
            y,
            fill=self.theme["scale_fill"]
        )

        self.down_input_field = self.master.create_rectangle(
            x + number_field_offset_x - input_field_offset_x,
            y,
            x + number_field_offset_x + input_field_offset_x,
            y + offset_y,
            fill=self.theme["scale_fill"]
        )

        self.value_number_text = self.master.create_text(
            x - input_field_offset_x,
            y,
            text=str(self.value),
            fill=self.theme["text_fill"],
            font=[self.master.FONT, self.text_data["text_size_small"]]
        )

        self.up_input_text = self.master.create_text(
            x + number_field_offset_x,
            y - offset_y // 2,
            text="\u2191",
            fill=self.theme["text_fill"],
            font=[self.master.FONT, self.text_data["text_size_small"] - 3]
        )

        self.down_input_text = self.master.create_text(
            x + number_field_offset_x,
            y + offset_y // 2,
            text="\u2193",
            fill=self.theme["text_fill"],
            font=[self.master.FONT, self.text_data["text_size_small"] - 3]
        )

        # Keyboard binding
        self.master.bind("<Motion>", self.handle_motion, add="+")
        self.master.bind("<Button-1>", self.handle_lclick, add="+")
        self.master.master.bind("<KeyPress>", self.handle_type, add="+")

        # Highlighting cycle
        self.highlight_cycle()

    def handle_motion(self, event):
        if is_inside(event, self.master.bbox(self.number_rect)):
            self.master.itemconfig(self.number_rect, fill=self.theme["scale_highlight"])
            self.master.itemconfig(self.up_input_field, fill=self.theme["scale_fill"])
            self.master.itemconfig(self.down_input_field, fill=self.theme["scale_fill"])

        elif is_inside(event, self.master.bbox(self.up_input_field)):
            self.master.itemconfig(self.number_rect, fill=self.theme["scale_fill"])
            self.master.itemconfig(self.up_input_field, fill=self.theme["scale_highlight"])
            self.master.itemconfig(self.down_input_field, fill=self.theme["scale_fill"])

        elif is_inside(event, self.master.bbox(self.down_input_field)):
            self.master.itemconfig(self.number_rect, fill=self.theme["scale_fill"])
            self.master.itemconfig(self.up_input_field, fill=self.theme["scale_fill"])
            self.master.itemconfig(self.down_input_field, fill=self.theme["scale_highlight"])

        else:
            self.master.itemconfig(self.number_rect, fill=self.theme["scale_fill"])
            self.master.itemconfig(self.up_input_field, fill=self.theme["scale_fill"])
            self.master.itemconfig(self.down_input_field, fill=self.theme["scale_fill"])

    def handle_lclick(self, event):
        if is_inside(event, self.master.bbox(self.up_input_field)):
            pass

        elif is_inside(event, self.master.bbox(self.down_input_field)):
            pass

    def handle_type(self, event):
        pass

    def highlight_cycle(self):
        pass

