# Imports
from tkinter import Canvas
from .is_inside import is_inside
from sound_system import SoundSystem


# Scale class
class Scale:
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            number_rect_offset_x,
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
        self.sound_system = SoundSystem(self.conf)

        # Drawing
        self.number_rect = self.master.create_rectangle(
            x - number_rect_offset_x - input_field_offset_x,
            y - offset_y,
            x + number_rect_offset_x - input_field_offset_x,
            y + offset_y,
            fill=self.theme["scale_fill"]
        )

        self.up_input_field = self.master.create_rectangle(
            x + number_rect_offset_x - input_field_offset_x,
            y - offset_y,
            x + number_rect_offset_x + input_field_offset_x,
            y,
            fill=self.theme["scale_fill"]
        )

        self.down_input_field = self.master.create_rectangle(
            x + number_rect_offset_x - input_field_offset_x,
            y,
            x + number_rect_offset_x + input_field_offset_x,
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
            x + number_rect_offset_x,
            y - offset_y // 2,
            text="\u2191",
            fill=self.theme["text_fill"],
            font=[self.master.FONT, self.text_data["text_size_small"] - 3]
        )

        self.down_input_text = self.master.create_text(
            x + number_rect_offset_x,
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
        if is_inside(event, self.master.bbox(self.number_rect)):
            self.is_highlighted = True
            self.cycle_counter = 0
            self.master.itemconfig(self.number_rect, outline=self.theme["scale_cursor"])

        elif is_inside(event, self.master.bbox(self.up_input_field)):
            self.sound_system.play("selector_clicked")
            self.is_highlighted = False
            self.value = self.value + 1 if self.value != self.max_value else self.value
            self.master.itemconfig(self.value_number_text, text=str(self.value))
            self.master.itemconfig(self.number_rect, outline=self.theme["scale_border"])

            self.callback_up()
            self.validate_input()

        elif is_inside(event, self.master.bbox(self.down_input_field)) and self.has_valid_input():
            self.sound_system.play("selector_clicked")
            self.is_highlighted = False
            self.value = self.value - 1 if self.value != self.min_value else self.value
            self.master.itemconfig(self.value_number_text, text=str(self.value))
            self.master.itemconfig(self.number_rect, outline=self.theme["scale_border"])

            self.callback_down()
            self.validate_input()

        else:
            self.master.itemconfig(self.number_rect, outline=self.theme["scale_border"])
            self.is_highlighted = False

    def handle_type(self, event):
        if self.is_highlighted:
            if event.keysym.isdecimal() or event.keysym == "BackSpace": # must be a number or a backspace
                if event.char.isdigit():
                    self.value = int(str(self.value) + event.char) if int(
                        str(self.value) + event.char) <= self.max_value else self.value

                if event.keysym == "BackSpace":
                    if len(str(self.value)) > 1:
                        self.value = int(str(self.value)[:-1]) if len(str(self.value)) > 1 else self.value
                    elif len(str(self.value)) == 1:
                        self.value = 0

                # Validity checking
                self.validate_input()
                self.master.itemconfig(self.value_number_text, text=str(self.value))

    def highlight_cycle(self):
        if self.is_highlighted:
            self.cycle_counter = (self.cycle_counter + 1) % 2

            if self.cycle_counter == 1:
                self.master.itemconfig(self.number_rect, outline=self.theme["scale_cursor"])
            else:
                self.master.itemconfig(self.number_rect, outline=self.theme["scale_border"])

        self.master.after(self.conf.get("widgets")["scale_highlight_cycle_ms"], self.highlight_cycle)

    def validate_input(self):  # this function changes the text
        if self.value < self.min_value:
            self.master.itemconfig(self.value_number_text, fill=self.theme["text_invalid"])
        else:
            self.master.itemconfig(self.value_number_text, fill=self.theme["text_fill"])

    def has_valid_input(self) -> bool:
        return self.value >= self.min_value # this function returns a boolean

