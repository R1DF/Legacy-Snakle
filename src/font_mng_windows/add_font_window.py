# Imports
from tkinter import Toplevel, Frame, Label, Entry, Button, font, messagebox

# Making the adder window
class FontAdder(Toplevel):
    def __init__(self, master):
        # Initialization
        Toplevel.__init__(self, master)
        self.master = master
        self.title("Add font")
        self.master.opened_window_parameters["add"] = True

        # building widgets
        self.font_intro_frame = Frame(self)
        self.font_intro_frame.pack()

        self.font_name_label = Label(self.font_intro_frame, text="Font name:")
        self.font_name_label.grid(row=0, column=0)

        self.font_name_entry = Entry(self.font_intro_frame, width=30)
        self.font_name_entry.grid(row=0, column=1)

        self.add_font_button = Button(self, text="Add", command=self.add_font)
        self.add_font_button.pack()

        # Adding protocol to modify when
        self.protocol("WM_DELETE_WINDOW", self.handle_exit)

    def add_font(self):
        if self.font_name_entry.get().strip() == "":
            messagebox.showerror("Empty input", "Please enter a font.")
        elif self.font_name_entry.get().strip().lower() not in [x.lower() for x in font.families()]:
            messagebox.showerror("Invalid font", "The entered font does not exist.")
        elif self.font_name_entry.get().strip().lower() in [x.lower() for x in self.master.fonts_listbox.get(0, "end")]: # There isn't a direct function where you get all Listbox values
            messagebox.showerror("Font already used", "You already have this font used.")
        else:
            font_position_in_list = [x.lower() for x in font.families()].index(self.font_name_entry.get().strip().lower()) # this might look over convoluted but it's to avoid case-sensitive problems
            self.master.fonts_listbox.insert("end", font.families()[font_position_in_list]) # the inputted font is auto-formatted
            self.master.update_font_amount()
            self.handle_exit()

    def handle_exit(self):
        self.master.opened_window_parameters["add"] = False
        self.destroy()

