class FileSelector:
    def __init__(
            self,
            master,
            x,
            y,
            offset_x,
            offset_y,
            file_name,
            theme,
            conf
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x - (offset_x // 2), y - (offset_y // 2), x + (offset_x // 2), y + (offset_y // 2))
        self.file_name = file_name
        print(4, theme)
        self.theme = theme,
        self.conf = conf

        # Drawing
        print(type(self.theme))
        print(1, self.theme)
        self.rect = self.master.master.create_rectangle(
            *self.init_coordinates,
            fill=self.theme["selector_element_fill"],
            width=2
        )
