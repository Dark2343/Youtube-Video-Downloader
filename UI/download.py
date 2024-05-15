# TODO:
# Progress bar (DONE)
# Message at the end (DONE)
# Return to main menu


# WORKS RIGHT NOW
import customtkinter as ctk
import Logic.logic as logic, threading

class Download(ctk.CTkFrame):
    def __init__(self, app, path, media, showWelcomeCall):
        super().__init__(app)
        
        # TODO: RETURN BACK TO MENU
        self.showWelcome = showWelcomeCall
        
        # Top padding
        spacerFrame = ctk.CTkLabel(self, text= "")
        spacerFrame.pack(pady=30)
        
        downloadingLabel = ctk.CTkLabel(app, text= f"Downloading: {media.default_filename}", font= ("", 15))
        downloadingLabel.pack(padx= 30, pady = 25, anchor='w')
        
        self.progressBar = ctk.CTkProgressBar(self, width=804, height=20,  orientation= "horizontal", mode= "determinate")
        self.progressBar.pack(padx= 30, pady = 15)
        
        self.downloadVideo(media, path)
    
    # Updates the progress every 100 ms until the download is finished
    def updateProgressBar(self, app):
        self.progressBar.set(logic.progress/ 100)
        if logic.progress < 100:
            app.after(100, self.updateProgressBar)
        else:
            # Show message at the end of download
            completeLabel = ctk.CTkLabel(self, text="Download Complete", font=("", 25))
            completeLabel.pack(padx= 20, pady= 45)
    
    # Starts downloading the video on a separate thread to ensure that the download and updating of progress bar don't interrupt each other
    def downloadVideo(self, media, path):
        def downloadAsync():
            logic.download(media, path, self.progressBar)
    
        # Starting the download on a new thread
        downloadThread = threading.Thread(target= downloadAsync)
        downloadThread.start()
        
        # Starts updating the progress bar
        self.updateProgressBar()
    
    def show(self):
        self.pack(fill= "both", expand= True)
        pass
        
    def hide(self):
        self.pack_forget()