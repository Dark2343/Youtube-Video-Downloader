import customtkinter as ctk
from UI.welcome import Welcome
from UI.videoInfo import VideoInfo
from UI.download import Download

class App:
    def __init__(self, app):
        # App settings
        self.app = app
        self.app.geometry("854x480")
        self.app.title("Youtube Video Downloader")
        self.app.iconbitmap("Images/YTD Logo.ico")
        self.currentView = None
        
        # Frames for each view
        self.View1 = Welcome(self.app, self.showVideoInfo)
        self.View2 = None
        self.View3 = None
        
        self.showVideoInfo("https://www.youtube.com/watch?v=p1df_2NwEB8")
        
    def showView(self, view):
        if self.currentView:
            self.currentView.hide()
        self.currentView = view
        self.currentView.show()
        
    def showWelcome(self):
        self.View1 = Welcome(self.app, self.showVideoInfo)
        self.showView(self.View1)
        
    def showVideoInfo(self, url):
        self.View2 = VideoInfo(self.app, url, self.showWelcome, self.showDownload)
        self.showView(self.View2)
    
    def showDownload(self, path, media):
        self.View3 = Download(self.app, path, media, self.showWelcome)
        self.showView(self.View3)