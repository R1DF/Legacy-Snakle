"""
The ClearanceChecker class shows how much a pack has been successfully cleared. It is used to display how much a
downloaded pack has been cleared for the viewer. It is also used to always verify clearance JSON files and make ones
that should exist for the game to use.

It runs on 3 occasions:
1. Game launch.
2. When the Play menu is opened.
3. When a pack's progress/clearance is being checked. (if an error may occur, then there could be no clearance file)
"""

# Imports
import json
import os

# Class
class ClearanceChecker:
    def __init__(self, packs_path):
        # Initialization
        self.packs_path = packs_path
        self.clearances_path = os.getcwd()+"\\clearance_data\\"

    def compare_progress(self, pack):
        """
        This function will compare a pack's clearance by dividing the amount of clear words in the clearance file and the
        amount of words in the pack file.
        """
        clear_words = json.load(open(self.clearances_path+f"c_{pack}", "r"))["clear_words"]
        all_words = json.load(open(self.packs_path+pack, "r"))["words"]
        return round(len(clear_words) / len(all_words), 2)

    def check_files(self):
        """
        This function will check if every existing pack file has its corresponding clearance file.
        If it does not, it automatically creates an empty one.
        """

        for pack in os.listdir(self.packs_path):
            if f"c_{pack}" not in os.listdir(self.clearances_path):
                json.dump({"file": pack, "clear_words": []}, open(self.clearances_path+f"c_{pack}", "w"))