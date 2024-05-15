# TODO:
# 1- Create other frames (DONE)
# 2- Transition between them
# 3- Make UI look better
# 4- Fix FullScreen

from UI.app import App
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
app = App(root)
root.mainloop()