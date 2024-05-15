# TODO:
# Video info (DONE)
# Choose Audio or Video (DONE)
# Select quality (DONE)
# Select file download location (DONE)
# Press download (DONE)

# FIXME:
# Handle if quality doesn't exist (DONE)
# Handle exception if the youtube api failed or network error


# COMPLETELY FUCKED AT THE MOMENT

from PIL import Image
from tkinter import filedialog as fd
import customtkinter as ctk, urllib.request as lib
import Logic.logic as logic, io, UI.download as download, tkinter as tk

class VideoInfo(ctk.CTkFrame):
    def __init__(self, app, url, showWelcomeCall, showDownloadCall):
        
        super().__init__(app)
        
        # TODO: ADD OPTION TO GO BACK TO WELCOME
        self.link = logic.getData(url)
        self.showWelcome = showWelcomeCall
        self.showDownload = showDownloadCall
        
        #Title
        videoTitleLabel = ctk.CTkLabel(app, text= f"Title: {self.link.title}", font= ("", 15))
        videoTitleLabel.configure(width= 20)
        videoTitleLabel.pack(padx = 2, pady = 2, anchor = 'w')
        
        # Length
        videoLengthLabel = ctk.CTkLabel(app, text= f"Length: {round(self.link.length/60)} mins", font= ("", 15))
        videoLengthLabel.configure(width= 20)
        videoLengthLabel.pack(padx = 2, pady = 2, anchor = 'w')
        
        # Author
        videoAuthorLabel = ctk.CTkLabel(app, text= f"Author: {self.link.author}", font= ("", 15))
        videoAuthorLabel.configure(width= 20)
        videoAuthorLabel.pack(padx = 2, pady = 2, anchor = 'w')
        
        # Thumbnail
        with lib.urlopen(self.link.thumbnail_url) as u:
            rawData = u.read()
                
        image = ctk.CTkImage(Image.open(io.BytesIO(rawData)), size=(350, 200))
        thumbnail = ctk.CTkLabel(app, text= "", image= image)
        thumbnail.pack(padx = 0.57, pady = 0.15, anchor = 'e')
                
        # File Type
        downloadTypeLabel = ctk.CTkLabel(app, text= f"Download as: ", font= ("", 15))
        downloadTypeLabel.pack(padx = 0.18, pady = 0.6)

        self.fileSizeLabel = ctk.CTkLabel(app, font= ("", 15))
        
        # Audio/Video
        self.typeRadio = tk.IntVar(value = 0)
        self.audioRadio = ctk.CTkRadioButton(app, text= "Audio", value= 1, variable= self.typeRadio, command= self.updateQualityOptions)
        self.audioRadio.pack(padx = 0.3, pady = 0.6)
        self.videoRadio = ctk.CTkRadioButton(app, text= "Video", value= 2, variable= self.typeRadio, command= self.updateQualityOptions)
        self.videoRadio.pack(padx = 0.4, pady = 0.6)
        
        # Quality Type
        self.qualityRadio = tk.IntVar(value = 0)
        self.qualityTypeLabel = ctk.CTkLabel(app, text= f"Quality: ", font= ("", 15))
        self.lowRadio = ctk.CTkRadioButton(app, text= "144p", variable= self.qualityRadio, value= 1, command= self.updateQualityOptions)
        self.mediumRadio = ctk.CTkRadioButton(app, text= "360p", variable= self.qualityRadio, value= 2, command= self.updateQualityOptions)
        self.highRadio = ctk.CTkRadioButton(app, text= "720p", variable= self.qualityRadio, value= 3, command= self.updateQualityOptions)
        

        self.directory = tk.StringVar(value= "")
        self.directoryButton = ctk.CTkButton(app, text= "Select Download Location", command= self.selectDirectory)
        self.pathLabel = ctk.CTkLabel(app, font= ("", 15))
                    
        # Download button
        self.downloadButton = ctk.CTkButton(app, text= "Download", command= self.downloadVideo)
    
    
    def show(self):
        self.pack(fill= "both", expand= True)
        
    def hide(self):
        self.pack_forget()
    
    # Function to update quality settings visibility
    def updateQualityOptions(self):
        # Check if Audio is chosen to hide video settings
        if self.typeRadio.get() == 1:
            self.qualityTypeLabel.pack_forget()
            self.lowRadio.pack_forget()
            self.mediumRadio.pack_forget()
            self.highRadio.pack_forget()
            self.directoryButton.pack(padx = 0.3, pady = 0.9)
            self.getFileSize()
            
            # Checks if directory is chosen to show download button
            if self.directory.get() != "":
                self.pathLabel.configure(text= f"Path: {self.directory.get()}")
                self.pathLabel.pack(padx = 0.25, pady = 0.8)
                self.downloadButton.pack(padx = 0.5, pady = 0.9)
            
        # Check if Video is chosen to show settings
        elif self.typeRadio.get() == 2:
            self.qualityTypeLabel.pack(padx = 0.23, pady = 0.7)
            self.lowRadio.pack(padx = 0.3, pady = 0.7)
            self.mediumRadio.pack(padx = 0.4, pady = 0.7)
            self.highRadio.pack(padx = 0.5, pady = 0.7)
            
            # Checks if quality and directory are chosen to show download button
            if self.qualityRadio.get() != 0:
                self.getFileSize()
                self.directoryButton.pack(padx = 0.3, pady = 0.9)
            else:
                self.directoryButton.pack_forget()
                            
            if self.qualityRadio.get() != 0 and self.directory.get() != "":
                self.pathLabel.configure(text= f"Path: {self.directory.get()}")
                self.pathLabel.pack(padx = 0.25, pady = 0.8)
                self.downloadButton.pack(padx = 0.5, pady = 0.9)
            else:
                self.downloadButton.pack_forget()


    # Gets the size of the video according to type and quality
    def getFileSize(self):
        self.media = None
        
        if self.typeRadio.get() == 1:
            self.media = self.link.streams.filter(mime_type="audio/mp4", abr="128kbps", type="audio").first()
        elif self.typeRadio.get() == 2:
            if self.qualityRadio.get() == 1:
                self.media = self.link.streams.filter(progressive=True, res="144p").first()
            elif self.qualityRadio.get() == 2:
                self.media = self.link.streams.filter(progressive=True, res="360p").first()
            elif self.qualityRadio.get() == 3:
                self.media = self.link.streams.filter(progressive=True, res="720p").first()
        
        if self.media:
            self.fileSizeLabel.configure(text=f"File Size: {self.media.filesize_mb} MBs")
        else:
            self.fileSizeLabel.configure(text="File Size: N/A")  # Handle NoneType gracefully
        self.fileSizeLabel.pack(padx=0.69, pady=0.58)

    # Select download location
    def selectDirectory(self):
        self.directory.set(fd.askdirectory())
        self.updateQualityOptions()

    # Downloads video
    def downloadVideo(self):
        self.showDownload(self.directory.get(), self.media)