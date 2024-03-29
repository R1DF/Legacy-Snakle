# Imports
import sys
from tkinter import Listbox
from font_mng_windows import *
from config_changer import ConfChange
from os import getcwd


# FontManager class
class FontManager(Toplevel):
    def __init__(self, master):
        # Initialization
        Toplevel.__init__(self, master)
        self.master = master
        self.master.is_font_manager_open = True
        self.title("Fonts")
        self.conf = self.master.conf
        self.opened_window_parameters = {
            "add": False,
            "rename": False
        }
        self.resizable(False, False)

        # Deletion protocol
        self.protocol("WM_DELETE_WINDOW", self.handle_exit)

        # Building widgets
        self.left_frame = Frame(self, padx=20)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = Frame(self, padx=20)
        self.right_frame.grid(row=0, column=1)

        # Left frame (fonts overview)
        self.fonts_label = Label(self.left_frame, text="List of fonts:")
        self.fonts_label.pack()

        self.fonts_listbox = Listbox(self.left_frame, width=50, height=23)
        self.fonts_listbox.pack(expand="1")

        # Right frame (control panel)
        self.control_panel_label = Label(self.right_frame, text="Manage fonts:")
        self.control_panel_label.pack(anchor="center")

        self.add_font_button = Button(self.right_frame, text="Add", width=20, command=self.show_font_adder)
        self.add_font_button.pack(anchor="center", pady=5)

        self.delete_font_button = Button(self.right_frame, text="Delete", width=20, command=self.delete_selected_font)
        self.delete_font_button.pack(anchor="center", pady=5)

        self.rename_font_button = Button(self.right_frame, text="Rename", width=20, command=self.show_font_renamer)
        self.rename_font_button.pack(anchor="center", pady=5)

        self.save_changes_font_button = Button(self.right_frame, text="Save", width=20, command=self.save_changes)
        self.save_changes_font_button.pack(anchor="center", pady=5)

        self.fonts_amount_text = Label(self.right_frame, text="Amount of fonts: .../10")
        self.fonts_amount_text.pack()

        self.selected_font_text = Label(self.right_frame, text="Selected font:\nN/A", font=["Arial", 12])
        self.selected_font_text.pack()

        # Load fonts and update the counter
        self.load_fonts()
        self.update_font_amount()

        # Tracing selection changes
        self.fonts_listbox.bind("<<ListboxSelect>>", self.handle_fonts_listbox_selection)

    def show_font_adder(self):
        if self.fonts_listbox.size() >= 10:
            messagebox.showerror("Font limit reached", "You can only have 10 fonts.")
        else:
            if not self.opened_window_parameters["add"]:
                self.add_font_win = FontAdder(self)

    def show_font_renamer(self):
        if not self.opened_window_parameters["rename"]:
            if self.fonts_listbox.curselection() == ():
                messagebox.showerror("No font selected", "Please select a font to rename from the list.")
            else:
                self.rename_font_win = FontRenamer(self, self.fonts_listbox.curselection()[0])

    def handle_exit(self):
        self.master.is_font_manager_open = False
        self.destroy()

    def delete_selected_font(self):
        if self.fonts_listbox.curselection() == ():
            messagebox.showerror("No font selected", "Please select a font to delete from the list.")
        else:
            self.fonts_listbox.delete(self.fonts_listbox.curselection())
            self.update_font_amount()
            self.selected_font_text.config(text="Selected font:\nN/A", font=["Arial", 12]) # because the selection automatically disappears

    def save_changes(self):
        if self.fonts_listbox.get(0, "end") == ():
            messagebox.showerror("Empty list", "Please add some fonts.")
        elif self.fonts_listbox.get(0, "end") == self.conf.get("text")["fonts"]:
            return
        else:
            # If the index is too high and fonts were deleted, set the index automatically to 0 to prevent bugs
            fonts = self.fonts_listbox.get(0, "end")
            new_default_font_family_index = self.conf.get("text")["default_font_family_index"]
            if new_default_font_family_index >= len(fonts):
                new_default_font_family_index = 0

            # Getting conf_to_merge and ConfChange class, then uploading
            conf_to_merge = {"text": {
                "fonts": fonts,
                "default_font_family_index": new_default_font_family_index,
                "text_size_huge": self.conf.get("text")["text_size_huge"],
                "text_size_big": self.conf.get("text")["text_size_big"],
                "text_size_mid": self.conf.get("text")["text_size_mid"],
                "text_size_small": self.conf.get("text")["text_size_small"],
                "text_size_tiny": 10  # constant default
            }}
            conf_change = ConfChange(self, self.conf.toml_data, conf_to_merge, getcwd()+"\\configurations")
            conf_change.upload()

            # Mandatory shutdown
            messagebox.showinfo("Update detected", "Due to an update in the game data, the game must be restarted to "
                                                   "apply the new settings. Click OK to proceed.")
            sys.exit()

    def load_fonts(self):
        for font in self.conf.get("text")["fonts"]:
            self.fonts_listbox.insert("end", font)
        self.fonts_amount_text.config(text=f"Amount of fonts: {len(self.conf.get('text')['fonts'])}/10")

    def update_font_amount(self):
        self.fonts_amount_text.config(text=f"Amount of fonts: {self.fonts_listbox.size()}/10")
        if self.fonts_listbox.size() in [0, 10]:
            self.fonts_amount_text.config(fg="RED")
        else:
            self.fonts_amount_text.config(fg="BLACK")

    def handle_fonts_listbox_selection(self, event):
        if self.fonts_listbox.curselection() == ():
            self.selected_font_text.config(text="Selected font:\nN/A", font=["Arial", 12])
        else:
            self.selected_font_text.config(text=f"Selected font:\n{self.fonts_listbox.get(self.fonts_listbox.curselection())}",
                                           font=[self.fonts_listbox.get(self.fonts_listbox.curselection()), 12])

