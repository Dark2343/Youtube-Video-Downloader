# TODO:
# Handle if any error occurs
# Add playlist download support
# Check if you can fix some resolutions being unavailable
# Check if you can use mp3 for all audio downloads

from UI.app import App
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
app = App(root)
root.mainloop()