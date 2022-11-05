# Imports
from tkinter import Toplevel, Frame, Listbox, Scrollbar, Label, Button
from os import getcwd
from subprocess import Popen
from clearance_checker import ClearanceChecker
import json

PACKS_PATH = getcwd() + "\\packs\\"


# FontManager class
class PackInfoShower(Toplevel):
    def __init__(self, master, pack_name):
        # Initialization
        Toplevel.__init__(self, master)
        self.master = master
        self.pack_name = pack_name
        self.pack_data = json.load(open(PACKS_PATH + self.pack_name, "r"))
        self.showing_description = False
        self.title(self.pack_data["title"])
        self.resizable(False, False)

        # Delection protocol
        self.protocol("WM_DELETE_WINDOW", self.handle_exit)

        # Drawing widgets
        self.main_frame = Frame(self)
        self.main_frame.pack()

        self.left_frame = Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1)

        # Left frame
        self.words_introduction_label = Label(self.left_frame, text="Words List")
        self.words_introduction_label.pack()

        # Listbox and scrollbar configuration
        self.listbox_frame = Frame(self.left_frame)
        self.listbox_frame.pack()

        self.words_listbox = Listbox(self.listbox_frame, height=17)
        self.words_listbox.pack(side="left")

        self.words_listbox_scrollbar = Scrollbar(self.listbox_frame)
        self.words_listbox_scrollbar.pack(side="right", fill="both")

        self.words_listbox.config(yscrollcommand=self.words_listbox_scrollbar.set)
        self.words_listbox_scrollbar.config(command=self.words_listbox.yview)

        # Right frame

        self.information_intro_label = Label(self.right_frame, text="Information")  # testing purposes just to see GUI change
        self.information_intro_label.pack()

        self.created_by_label = Label(self.right_frame, text=f"Created by: {self.pack_data['creator']}")
        self.created_by_label.pack()

        self.created_on_label = Label(self.right_frame, text=f"Date created: {self.format_date(self.pack_data['dateCreated'])}")
        self.created_on_label.pack()

        self.progress_label = Label(self.right_frame, text=f"Progress: {ClearanceChecker(PACKS_PATH).compare_progress(self.pack_name)}%")
        self.progress_label.pack()

        self.find_in_explorer_button = Button(self.right_frame, text="Find in Explorer", width=20, command=lambda: Popen(f"explorer /select,{PACKS_PATH+self.pack_name}"))
        self.find_in_explorer_button.pack(pady=5)

        self.show_description_button = Button(self.right_frame, text="Show Description", width=20, command=self.handle_description_toggle)
        self.show_description_button.pack(pady=5)

        self.description_label = Label(self.right_frame, text=self.format_description(self.pack_data["description"]))  # Description always hidden by default

        # Adding words
        self.add_pack_words()

    def format_date(self, date):
        day, month, year = [int(x) for x in self.pack_data["dateCreated"].split(".")]

        #  Getting ordinal number
        match int((str(day) if day > 9 else "0" + str(day))[1:]):
            case 1:
                ordinal_number = str(day) + "st"
            case 2:
                ordinal_number = str(day) + "nd"
            case 3:
                ordinal_number = str(day) + "rd"
            case _:
                ordinal_number = str(day) + "th"

        # Getting month name
        month_name = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }[month]

        return f"{ordinal_number} {month_name}, {year}"

    def format_description(self, description):
        new_description = ""
        latest_break = 0
        for letter_index in range(0, len(description)):
            if letter_index - latest_break > 24 and description[letter_index] == " ":
                new_description += "\n"
                latest_break = letter_index
            else:
                new_description += description[letter_index]
        return new_description

    def handle_description_toggle(self):
        if self.showing_description:
            self.description_label.pack_forget()
            self.show_description_button.config(text="Show Description")
        else:
            self.description_label.pack()
            self.show_description_button.config(text="Hide Description")

        self.showing_description = not self.showing_description

    def add_pack_words(self):
        for word in self.pack_data["words"]:
            self.words_listbox.insert("end", word)

    def handle_exit(self):
        self.master.is_pack_information_shower_open = False
        self.destroy()

