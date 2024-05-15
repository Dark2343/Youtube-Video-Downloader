# TODO:
# Welcome message (DONE)
# Enter URL (DONE)

# WORKS RIGHT NOW
from PIL import Image
import customtkinter as ctk

class Welcome(ctk.CTkFrame):
    def __init__(self, app, showVideoInfoCall):
        
        super().__init__(app)
        
        # Go to Video Info
        self.showVideoInfo = showVideoInfoCall
        
        # Load the image
        iconPath = "Images/YTD Logo.png"
        iconImage = Image.open(iconPath)
        iconImage = ctk.CTkImage(iconImage, size= (150, 93.75))
        
        # Put the image on screen
        iconLabel = ctk.CTkLabel(self, image= iconImage, text= "")
        iconLabel.configure(width = 100, height = 100)
        iconLabel.pack(pady= 10)
        
        welcomeLabel = ctk.CTkLabel(self, text= "Welcome to Youtube Video Downloader", font= ("", 25))
        welcomeLabel.pack(pady = 30)

        inputLabel = ctk.CTkLabel(self, text= "Please enter the URL of the video you wish to download", font= ("", 15))
        inputLabel.pack(pady = 10)

        self.urlData = ctk.CTkEntry(self, placeholder_text= "URL", width= 250)
        self.urlData.pack(pady = 10)

        getVideoButton = ctk.CTkButton(self, text= "Get video", command= self.findVideo)
        getVideoButton.pack(pady = 10)
        
    def show(self):
        self.pack(fill= "both", expand= True)
        
    def hide(self):
        self.pack_forget()
    
    def findVideo(self):
        self.showVideoInfo(self.urlData.get())