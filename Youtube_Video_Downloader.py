import time
from pytube import YouTube
from pytube.cli import on_progress
import ssl

url = str(input("Enter the URL of the video you wish to download:\n"))
link = YouTube(url, on_progress_callback=on_progress)
print(f'\nTitle: {link.title}\nLength: {round(link.length/60)} mins\nMade by: {link.author}')
type = int(input("\nDo you want to download Video or Audio:\n 1- Video\n 2- Audio\n"))
media = link.streams.filter(progressive=True, res="144p").first()

if type == 1:
    quality = int(input("\nChoose your preferred quality:\n 1- 144p\n 2- 360p\n 3- 720p\n"))
    
    if quality == 1:
        media = link.streams.filter(progressive=True, res="144p").first()
    elif quality == 2:
        media = link.streams.filter(progressive=True, res="360p").first()
    elif quality == 3:
        media = link.streams.filter(progressive=True, res="720p").first()

elif type == 2:
    media = link.streams.filter(mime_type="audio/mp4", abr="128kbps", type="audio").first()

if media:
    print(f'\nFile size is: {round(media.filesize / 10 ** 6)} MBs')
    download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

    if download == 1:
        print("Please wait, file is being downloaded...\n")
        media.download('/Downloads')
        print("File has been downloaded\nEnjoy :D\n")
    elif download == 2:
        print("Program has been terminated")
elif not media:
    print("Sorry this format is unavailable")

time.sleep(5)
