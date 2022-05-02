# Imports
import os

# Main code
class PackFinder:
    def __init__(self, master, location):
        self.master = master
        self.rel_path = location

    def get_amount_of_packs(self):
        return len(os.listdir(os.getcwd()+self.rel_path))
