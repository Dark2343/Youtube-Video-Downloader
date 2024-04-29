# Progress bar
# Message at the end
# Return to main menu

import logic
import customtkinter as ctk

def show(app, path, media, url):
    
    # Destroy the welcome widgets
    for widget in app.winfo_children():
        widget.destroy()
    
    downloadingLabel = ctk.CTkLabel(app, text= f"Downloading: {media.default_filename}", font= ("", 15))
    downloadingLabel.place(relx = 0.02, rely = 0.25)
    
    progressBar = ctk.CTkProgressBar(app, width=804, height=20,  orientation= "horizontal", mode= "determinate")
    progressBar.place(relx = 0.03, rely = 0.35)
    
    logic.download(media, path, progressBar)
    