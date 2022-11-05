# Imports
from tkinter import Toplevel, Frame, Label, Entry, Button, font, messagebox


# Making the adder window
class FontRenamer(Toplevel):
    def __init__(self, master, font_index):
        # Initialization
        Toplevel.__init__(self, master)
        self.master = master
        self.title("Rename")
        self.font_index = font_index  # This value is the index of the selected font in the list
        self.master.opened_window_parameters["rename"] = True
        self.resizable(False, False)

        # building widgets
        self.font_intro_frame = Frame(self)
        self.font_intro_frame.pack()

        self.old_font_name_label1 = Label(self.font_intro_frame, text="Old font name:")
        self.old_font_name_label1.grid(row=0, column=0)

        self.old_font_name_label2 = Label(self.font_intro_frame, text=self.master.fonts_listbox.get(font_index))
        self.old_font_name_label2.grid(row=0, column=1)

        self.new_font_name_label = Label(self.font_intro_frame, text="New font name:")
        self.new_font_name_label.grid(row=1, column=0)

        self.new_font_name_entry = Entry(self.font_intro_frame, width=30)
        self.new_font_name_entry.insert(0, self.master.fonts_listbox.get(font_index))
        self.new_font_name_entry.grid(row=1, column=1)

        self.rename_font_button = Button(self, text="Rename", command=self.rename_font)
        self.rename_font_button.pack()

        # Adding protocol to modify when
        self.protocol("WM_DELETE_WINDOW", self.handle_exit)

    def rename_font(self):
        if self.new_font_name_entry.get().strip() == "":
            messagebox.showerror("Empty input", "Please enter a font.")
        elif self.new_font_name_entry.get().strip().lower() not in [x.lower() for x in font.families()]:
            messagebox.showerror("Invalid font", "The entered font does not exist.")
        elif self.new_font_name_entry.get().strip().lower() in [x.lower() for x in self.master.fonts_listbox.get(0, "end")]:  # same case in add_font_window.py
            messagebox.showerror("Font already used", "You already have this font used.")
        else:
            font_position_in_list = [x.lower() for x in font.families()].index(self.new_font_name_entry.get().strip().lower())
            self.master.fonts_listbox.delete(self.font_index)
            self.master.fonts_listbox.insert(self.font_index, font.families()[font_position_in_list])  # same case here too just like in add_font_window.py
            self.handle_exit()

    def handle_exit(self):
        self.master.opened_window_parameters["rename"] = False
        self.destroy()

