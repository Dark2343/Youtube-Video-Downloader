# TODO:
# Progress bar (DONE)
# Message at the end (DONE)
# Return to main menu

import Logic.logic as logic, threading
import customtkinter as ctk

def show(app, path, media, url):
    
    # Destroy the welcome widgets
    for widget in app.winfo_children():
        widget.destroy()
    
    downloadingLabel = ctk.CTkLabel(app, text= f"Downloading: {media.default_filename}", font= ("", 15))
    downloadingLabel.place(relx = 0.02, rely = 0.25)
    
    progressBar = ctk.CTkProgressBar(app, width=804, height=20,  orientation= "horizontal", mode= "determinate")
    progressBar.place(relx = 0.03, rely = 0.35)
    
    # Updates the progress every 100 ms until the download is finished
    def updateProgressBar():
        progressBar.set(logic.progress/ 100)
        if logic.progress < 100:
            app.after(100, updateProgressBar)
        else:
            # Show message at the end of download
            completeLabel = ctk.CTkLabel(app, text="Download Complete", font=("", 15))
            completeLabel.place(relx=0.02, rely=0.45)
    
    # Starts downloading the video on a separate thread to ensure that the download and updating of progress bar don't interrupt each other
    def downloadVideo():
        def downloadAsync():
            logic.download(media, path, progressBar)
    
        # Starting the download on a new thread
        downloadThread = threading.Thread(target= downloadAsync)
        downloadThread.start()
        # Starts updating the progress bar
        updateProgressBar()
    
    downloadVideo()