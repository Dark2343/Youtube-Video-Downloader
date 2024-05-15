# TODO:
# Welcome message (DONE)
# Enter URL (DONE)

import UI.videoInfo as videoInfo
import customtkinter as ctk

def show(app):
    welcome = ctk.CTkLabel(app, text= "Welcome to Youtube Video Downloader", font= ("", 15))
    welcome.place(relx = 0.5, rely = 0.2, anchor = ctk.CENTER)

    inputLabel = ctk.CTkLabel(app, text= "Please enter the URL of the video you wish to download", font= ("", 15))
    inputLabel.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)

    urlData = ctk.CTkEntry(app, placeholder_text= "URL", width= 250)
    urlData.place(relx = 0.5, rely = 0.5, anchor= ctk.CENTER)
    
    def findVideo():
        videoInfo.show(app, urlData.get()) 
    
    getVideoButton = ctk.CTkButton(app, text= "Get video", command= findVideo)
    getVideoButton.place(relx = 0.5, rely = 0.6, anchor= ctk.CENTER)