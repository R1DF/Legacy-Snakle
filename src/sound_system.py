# Importing the sound playing library
import winsound  # Only works for Windows
import os


# The following class will automatically play a selected found. It will ignore functions if sound is toggled OFF.
class SoundSystem:
    def __init__(self, conf):
        self.enabled = conf.get("game")["has_sound"]

    def play(self, sound, is_async=True):
        if self.enabled:
            if is_async:
                winsound.PlaySound(os.getcwd() + "\\sounds\\" + sound + ".wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
            else:
                winsound.PlaySound(os.getcwd() + "\\sounds\\" + sound + ".wav", winsound.SND_ALIAS) # run asynchronously

    def force_play(self, sound, is_async):
        # Same as play but doesn't check
        if is_async:
            winsound.PlaySound(os.getcwd() + "\\sounds\\" + sound + ".wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        else:
            winsound.PlaySound(os.getcwd() + "\\sounds\\" + sound + ".wav", winsound.SND_ALIAS)

