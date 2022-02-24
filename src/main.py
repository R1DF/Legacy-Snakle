# Imports
from tkinter import Tk # window GUI
from config_loader import ConfigLoader, CONF_FILE, CONF_PATH

# Making the window
class App(Tk):
    def __init__(self):
        # Initialization of the window
        Tk.__init__(self)
        self.title("Snakle")

        # Adjusting to settings
        self.conf = ConfigLoader(CONF_PATH+CONF_FILE)
        self.geometry(self.conf.get("window")["width"] + "x" + self.conf.get("window")["height"])
        self.resizable(False, False) # must change to f-string
        

# Creating the window instance
app = App()
app.mainloop()
