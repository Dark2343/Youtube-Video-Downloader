# Video info
# Choose Audio or Video
# Select quality
# Select file download location
# Press download

# TODO: Handle exception if the youtube api failed or network error
# Handle if quality doesn't exist

import logic, io
import tkinter as tk
import customtkinter as ctk
import urllib.request as lib
from PIL import Image
from tkinter import filedialog as fd

def show(app, url):
    link = logic.getData(url)
    
    #Title
    videoTitleLabel = ctk.CTkLabel(app, text= f"Title: {link.title}", font= ("", 15))
    videoTitleLabel.place(relx = 0.02, rely = 0.15)
    
    # Length
    videoLengthLabel = ctk.CTkLabel(app, text= f"Length: {round(link.length/60)} mins", font= ("", 15))
    videoLengthLabel.place(relx = 0.02, rely = 0.25)
    
    # Author
    videoAuthorLabel = ctk.CTkLabel(app, text= f"Author: {link.author}", font= ("", 15))
    videoAuthorLabel.place(relx = 0.02, rely = 0.35)
    
    # Thumbnail
    with lib.urlopen(link.thumbnail_url) as u:
        rawData = u.read()
            
    image = ctk.CTkImage(Image.open(io.BytesIO(rawData)), size=(350, 200))
    thumbnail = ctk.CTkLabel(app, text= "", image= image)
    thumbnail.place(relx = 0.57, rely = 0.15)
    
    # Function to update quality settings visibility
    def updateQualityOptions():
        # Check if Audio is chosen to hide video settings
        if typeRadio.get() == 1:
            qualityTypeLabel.place_forget()
            lowRadio.place_forget()
            mediumRadio.place_forget()
            highRadio.place_forget()
            directoryButton.place(relx = 0.3, rely = 0.9)
            getFileSize()
            
            # Checks if directory is chosen to show download button
            if directory.get() != "":
                pathLabel.configure(text= f"Path: {directory.get()}")
                pathLabel.place(relx = 0.25, rely = 0.8)
                downloadButton.place(relx = 0.5, rely = 0.9)
            
        # Check if Video is chosen to show settings
        elif typeRadio.get() == 2:
            qualityTypeLabel.place(relx = 0.23, rely = 0.7)
            lowRadio.place(relx = 0.3, rely = 0.7)
            mediumRadio.place(relx = 0.4, rely = 0.7)
            highRadio.place(relx = 0.5, rely = 0.7)
            
            # Checks if quality and directory are chosen to show download button
            if qualityRadio.get() != 0:
                getFileSize()
                directoryButton.place(relx = 0.3, rely = 0.9)
            else:
                directoryButton.place_forget()
                            
            if qualityRadio.get() != 0 and directory.get() != "":
                pathLabel.configure(text= f"Path: {directory.get()}")
                pathLabel.place(relx = 0.25, rely = 0.8)
                downloadButton.place(relx = 0.5, rely = 0.9)
            else:
                downloadButton.place_forget()
            
            
    global qualityRadio, qualityTypeLabel, lowRadio, mediumRadio, highRadio, downloadButton

    # File Type
    downloadTypeLabel = ctk.CTkLabel(app, text= f"Download as: ", font= ("", 15))
    downloadTypeLabel.place(relx = 0.18, rely = 0.6)

    fileSizeLabel = ctk.CTkLabel(app, font= ("", 15))
    
    # Gets the size of the video according to type and quality
    def getFileSize():
        media = None
        
        if typeRadio.get() == 1:
            media = link.streams.filter(mime_type="audio/mp4", abr="128kbps", type="audio").first()
        elif typeRadio.get() == 2:
            if qualityRadio.get() == 1:
                media = link.streams.filter(progressive=True, res="144p").first()
            elif qualityRadio.get() == 2:
                media = link.streams.filter(progressive=True, res="360p").first()
            elif qualityRadio.get() == 3:
                media = link.streams.filter(progressive=True, res="720p").first()
        
        if media:
            fileSizeLabel.configure(text=f"File Size: {round(media.filesize / 10 ** 6)} MBs")
        else:
            fileSizeLabel.configure(text="File Size: N/A")  # Handle NoneType gracefully
        fileSizeLabel.place(relx=0.69, rely=0.58)
    
    # Audio/Video
    typeRadio = tk.IntVar(value = 0)
    audioRadio = ctk.CTkRadioButton(app, text= "Audio", value= 1, variable= typeRadio, command=updateQualityOptions)
    audioRadio.place(relx = 0.3, rely = 0.6)
    videoRadio = ctk.CTkRadioButton(app, text= "Video", value= 2, variable= typeRadio, command=updateQualityOptions)
    videoRadio.place(relx = 0.4, rely = 0.6)
    
    # Quality Type
    qualityRadio = tk.IntVar(value = 0)
    qualityTypeLabel = ctk.CTkLabel(app, text= f"Quality: ", font= ("", 15))
    lowRadio = ctk.CTkRadioButton(app, text= "144p", variable= qualityRadio, value= 1, command= updateQualityOptions)
    mediumRadio = ctk.CTkRadioButton(app, text= "360p", variable= qualityRadio, value= 2, command= updateQualityOptions)
    highRadio = ctk.CTkRadioButton(app, text= "720p", variable= qualityRadio, value= 3, command= updateQualityOptions)
    
    # Select download location
    def selectDirectory():
        directory.set(fd.askdirectory())
        updateQualityOptions()
    
    directory = tk.StringVar(value= "")
    directoryButton = ctk.CTkButton(app, text= "Select Download Location", command= selectDirectory)
    pathLabel = ctk.CTkLabel(app, font= ("", 15))
    
    # Download button
    downloadButton = ctk.CTkButton(app, text= "Download")
    