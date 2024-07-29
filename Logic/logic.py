from pytubefix import YouTube

progress = 0

def onProgress(stream, chunk, remainingBytes):
    global progress
    
    totalSize = stream.filesize
    bytesDownloaded = totalSize - remainingBytes
    progress = int(bytesDownloaded / totalSize * 100)
    
def getData(url):
    link = YouTube(url)
    link.register_on_progress_callback(onProgress)
    return link

def download(media, path, progressBar):
    global progress
    
    progress = 0
    media.download(path)