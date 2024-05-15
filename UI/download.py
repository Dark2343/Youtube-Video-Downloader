# TODO:
# Progress bar (DONE)
# Message at the end (DONE)
# Return to main menu (DONE)

import customtkinter as ctk
import Logic.logic as logic, threading

class Download(ctk.CTkFrame):
    def __init__(self, app, path, media, showWelcomeCall):
        super().__init__(app)
        
        self.app = app
        self.showWelcome = showWelcomeCall
        
        # Top padding
        spacerFrame = ctk.CTkLabel(self, text= "")
        spacerFrame.pack(pady=30)
        
        # Putting it on a different frame to give a better look
        downloadingLabel = ctk.CTkLabel(self.app, text= f"Downloading: {media.default_filename}", font= ("", 25))
        downloadingLabel.pack(padx= 30, pady = 25, anchor='w')
        
        self.progressBar = ctk.CTkProgressBar(self, width=804, height=20,  orientation= "horizontal", mode= "determinate")
        self.progressBar.pack(padx= 30, pady = 15)
                
        self.downloadVideo(media, path)

    # Shows the frame
    def show(self):
        self.pack(fill= "both", expand= True)
        pass
        
    # Hides the frame
    def hide(self):
        self.pack_forget()
    
    # Updates the progress every 100 ms until the download is finished
    def updateProgressBar(self):
        self.progressBar.set(logic.progress/ 100)
        if logic.progress < 100:
            self.app.after(100, self.updateProgressBar)
        else:
            # Show message at the end of download
            completeLabel = ctk.CTkLabel(self, text="Download Complete", font=("", 25))
            completeLabel.pack(padx= 20, pady= 45)
            
            # Show button to go back to menu
            self.backToMenuButton = ctk.CTkButton(self, text="Back to Menu", font=("", 20), command=self.showWelcome, width=200, height=50, corner_radius= 10)
            self.backToMenuButton.pack(padx = 15, pady = 10)
    
    # Starts downloading the video on a separate thread to ensure that the download and updating of progress bar don't interrupt each other
    def downloadVideo(self, media, path):
        def downloadAsync():
            logic.download(media, path, self.progressBar)
    
        # Starting the download on a new thread
        downloadThread = threading.Thread(target= downloadAsync)
        downloadThread.start()
        
        # Starts updating the progress bar
        self.updateProgressBar()
    