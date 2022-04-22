# Configurations changing module
class ConfChange:
    def __init__(self, master, old_data, data_to_merge, location):
        """
        The ConfChange class is used to add functionality to the "save changes" buttons in the settings;
        This file will use old config.toml data and take data from the updated settings screen to obtain a dict that will
        contain the fully updated configurations, later to overwrite config.toml.

        Warning: Any comments in the previous config.toml will be deleted due to how the process works. I might have to
        abuse a loophole to still insert the top warning comment though. (-R1DF, 21.04.22)
        """

        # Initialization
        self.master = master
        self.old_data, self.data_to_merge = old_data, data_to_merge
        self.location = location

