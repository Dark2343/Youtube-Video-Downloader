# TODO:
# Handle exception if Youtube API failed or network error occurred

from PIL import Image
import Logic.logic as logic, io, tkinter as tk
import customtkinter as ctk, urllib.request as lib
from tkinter import DISABLED, NORMAL, filedialog as fd

class VideoInfo(ctk.CTkFrame):
    def __init__(self, app, url, showWelcomeCall, showDownloadCall):
        
        super().__init__(app)
        
        self.link = logic.getData(url)
        self.showWelcome = showWelcomeCall
        self.showDownload = showDownloadCall
        
        self.backToMenuButton = ctk.CTkButton(self, text= "Back to Menu", command= self.showWelcome)
        self.backToMenuButton.pack(padx = 15, pady = 10, side = "top", anchor = "nw")
        
        # Thumbnail
        with lib.urlopen(self.link.thumbnail_url) as u:
            rawData = u.read()
                
        image = ctk.CTkImage(Image.open(io.BytesIO(rawData)), size=(550, 300))
        thumbnail = ctk.CTkLabel(self, text= "", image= image)
        thumbnail.pack(pady = 15)
        
        # Frame for all settings
        detailsFrame = ctk.CTkFrame(self, fg_color= "#2B2B2B")
        detailsFrame.pack(padx=10, anchor = "nw", side = "left")
        
        # Frame for title, length, author
        infoFrame = ctk.CTkFrame(detailsFrame, fg_color= "#2B2B2B")
        infoFrame.pack(padx=10, side = "left")
        
        # Title
        videoTitleLabel = ctk.CTkLabel(infoFrame, text= f"Title: {self.link.title}", font= ("", 15))
        videoTitleLabel.configure(width= 20)
        videoTitleLabel.pack(padx = 20, pady = 2, anchor = "w")
        
        # Length
        videoLengthLabel = ctk.CTkLabel(infoFrame, text= f"Length: {round(self.link.length/60)} mins", font= ("", 15))
        videoLengthLabel.configure(width= 20)
        videoLengthLabel.pack(padx = 20, pady = 2, anchor = "w")
        
        # Author
        videoAuthorLabel = ctk.CTkLabel(infoFrame, text= f"Author: {self.link.author}", font= ("", 15))
        videoAuthorLabel.configure(width= 20)
        videoAuthorLabel.pack(padx = 20, pady = 2, anchor = "w")
                
        # Frame for file type and quality frames
        optionFrame = ctk.CTkFrame(detailsFrame, fg_color= "#2B2B2B")
        optionFrame.pack(padx=10, pady=20, side= "left")
        
        # Frame for file type
        typeFrame = ctk.CTkFrame(optionFrame, fg_color= "#2B2B2B")
        typeFrame.pack(padx=10, pady=20, anchor = "nw")
        
        # Download type label
        downloadTypeLabel = ctk.CTkLabel(typeFrame, text="Download as:", font=("Helvetica", 15))
        downloadTypeLabel.pack(side="left", padx= 15)
        
        # Audio/Video
        self.typeRadio = tk.IntVar(value=0)
        self.audioRadio = ctk.CTkRadioButton(typeFrame, text="Audio", value=1, variable=self.typeRadio, command=self.updateQualityOptions)
        self.audioRadio.pack(side="left")
        
        self.videoRadio = ctk.CTkRadioButton(typeFrame, text="Video", value=2, variable=self.typeRadio, command=self.updateQualityOptions)
        self.videoRadio.pack(side="left")
        
        # Frame for quality options
        qualityFrame = ctk.CTkFrame(optionFrame, fg_color= "#2B2B2B")
        qualityFrame.pack(padx=10, pady=20, anchor = "nw")

        # Quality Type
        self.qualityRadio = tk.IntVar(value = 0)
        self.qualityTypeLabel = ctk.CTkLabel(qualityFrame, text= f"Quality: ", font= ("", 15))
        self.qualityTypeLabel.pack(padx = 5, side = "left")
        self.lowRadio = ctk.CTkRadioButton(qualityFrame, text= "144p", variable= self.qualityRadio, value= 1, command= self.updateQualityOptions)
        self.lowRadio.pack(side = "left")
        self.mediumRadio = ctk.CTkRadioButton(qualityFrame, text= "360p", variable= self.qualityRadio, value= 2, command= self.updateQualityOptions)
        self.mediumRadio.pack(side = "left")
        self.highRadio = ctk.CTkRadioButton(qualityFrame, text= "720p", variable= self.qualityRadio, value= 3, command= self.updateQualityOptions)
        self.highRadio.pack(side = "left")

        # Disable the buttons
        self.lowRadio.configure(state = DISABLED)
        self.mediumRadio.configure(state = DISABLED)
        self.highRadio.configure(state = DISABLED)
        
        # Frame for file and download Frames
        downloadInfoFrame = ctk.CTkFrame(detailsFrame, fg_color= "#2B2B2B")
        downloadInfoFrame.pack(padx=10, pady=20, side = "left")
        
        # Frame for file size and directory button
        fileFrame = ctk.CTkFrame(downloadInfoFrame, fg_color= "#2B2B2B")
        fileFrame.pack(side = "top")
        
        # Frame for path and download button
        downloadFrame = ctk.CTkFrame(downloadInfoFrame, fg_color= "#2B2B2B")
        downloadFrame.pack(side = "bottom")
        
        # File Size
        self.fileSizeLabel = ctk.CTkLabel(fileFrame, font= ("", 15))
        
        # Download Directory
        self.directory = tk.StringVar(value= "")
        self.directoryButton = ctk.CTkButton(fileFrame, text= "Select Download Location", command= self.selectDirectory)
        self.pathLabel = ctk.CTkLabel(downloadFrame, font= ("", 15))
        
        # Download button
        self.downloadButton = ctk.CTkButton(downloadFrame, text= "Download", command= self.downloadVideo)
    
    # Shows the frame
    def show(self):
        self.pack(fill= "both", expand= True)
        
    # Hides the frame
    def hide(self):
        self.pack_forget()
    
    # Function to update quality settings visibility
    def updateQualityOptions(self):
        
        # Check if Audio is chosen to hide video settings
        if self.typeRadio.get() == 1:
            self.getFileSize()
            self.lowRadio.configure(state = DISABLED)
            self.mediumRadio.configure(state = DISABLED)
            self.highRadio.configure(state = DISABLED)
            self.directoryButton.pack()
            
            # Checks if directory is chosen to show download button
            if self.directory.get() != "":
                self.pathLabel.configure(text= f"Path: {self.directory.get()}")
                self.pathLabel.pack()
                self.downloadButton.pack()
            
        # Check if Video is chosen to show settings
        elif self.typeRadio.get() == 2:
            
            # Enable quality buttons
            self.lowRadio.configure(state = NORMAL)
            self.mediumRadio.configure(state = NORMAL)
            self.highRadio.configure(state = NORMAL)
            
            # Checks if quality and directory are chosen to show download button
            if self.qualityRadio.get() != 0:
                self.getFileSize()
                self.directoryButton.pack()
            else:
                self.directoryButton.pack_forget()
            
            if self.qualityRadio.get() != 0 and self.directory.get() != "":
                self.pathLabel.configure(text= f"Path: {self.directory.get()}")
                self.pathLabel.pack()
                self.downloadButton.pack()
            else:
                self.downloadButton.pack_forget()


    # Gets the size of the video according to type and quality
    def getFileSize(self):
        self.media = None
        
        # Audio
        if self.typeRadio.get() == 1:
            self.media = self.link.streams.filter(mime_type="audio/mp4", abr="128kbps", type="audio").first()
        
        # Video
        elif self.typeRadio.get() == 2:
            if self.qualityRadio.get() == 1:
                self.media = self.link.streams.filter(progressive=True, res="144p").first()
            elif self.qualityRadio.get() == 2:
                self.media = self.link.streams.filter(progressive=True, res="360p").first()
            elif self.qualityRadio.get() == 3:
                self.media = self.link.streams.filter(progressive=True, res="720p").first()
        
        # Can download
        if self.media:
            self.fileSizeLabel.configure(text=f"File Size: {self.media.filesize_mb} MBs")
        # Can't download
        else:
            self.fileSizeLabel.configure(text="File Size: N/A")
        self.fileSizeLabel.pack()

    # Select download location
    def selectDirectory(self):
        self.directory.set(fd.askdirectory())
        self.updateQualityOptions()

    # Downloads video
    def downloadVideo(self):
        self.showDownload(self.directory.get(), self.media)