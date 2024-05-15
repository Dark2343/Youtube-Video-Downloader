# TODO:
# 1- Create other frames (DONE)
# 2- Transition between them
# 3- Make UI look better
# 4- Fix FullScreen

import customtkinter as ctk
import UI.welcome as welcome

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("854x480")
app.title("Youtube Video Downloader")

welcome.show(app)

app.mainloop()