# Date: 8/3/2022
# A program to download videos from Youtube as either a video format or an audio one
# Allows you to choose the quality if you're downloading it as a video while also telling you the size of the download


import time
from pytube import YouTube
from pytube.cli import on_progress

url = str(input("Enter the URL of the video you wish to download:\n"))
video = YouTube(url, on_progress_callback=on_progress)
print(f'\nTitle: {video.title}')
print(f'Length: {round(video.length/60)} mins')
print(f'Made by: {video.author}')
type = int(input("\nDo you want to download Video or Audio:\n 1- Video\n 2- Audio\n"))

if type == 1:
    quality = int(input("\nChoose your preferred quality:\n 1- 144p\n 2- 360p\n 3- 720p\n"))
    if quality == 1:
        video = video.streams.filter(progressive=True, res="144p").first()
        if video:
            print(f'\nFile size is: {round(video.filesize / 10 ** 6)} MBs')
            download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

            if download == 1:
                print("Please wait, file is being downloaded...\n")
                video.download('/Downloads')
                print("File has been downloaded\n Enjoy :D\n")
            elif download == 2:
                print("Program has been terminated")
        elif not video:
            print("Sorry this quality is unavailable")

    elif quality == 2:
        video = video.streams.filter(progressive=True, res="360p").first()
        if video:
            print(f'\nFile size is: {round(video.filesize / 10 ** 6)} MBs')
            download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

            if download == 1:
                print("Please wait, file is being downloaded...\n")
                video.download('/Downloads')
                print("File has been downloaded\n Enjoy :D\n")
            elif download == 2:
                print("Program has been terminated")
        elif not video:
            print("Sorry this quality is unavailable")

    elif quality == 3:
        video = video.streams.filter(progressive=True, res="720p").first()
        if video:
            print(f'\nFile size is: {round(video.filesize / 10 ** 6)} MBs')
            download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

            if download == 1:
                print("Please wait, file is being downloaded...\n")
                video.download('/Downloads')
                print("File has been downloaded\n Enjoy :D\n")
            elif download == 2:
                print("Program has been terminated")
        elif not video:
            print("Sorry this quality is unavailable")

elif type == 2:
    video = video.streams.filter(mime_type="audio/mp4", abr="128kbps", type="audio").first()
    if video:
        print(f'\nFile size is: {round(video.filesize / 10 ** 6)} MBs')
        download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

        if download == 1:
            print("Please wait, file is being downloaded...\n")
            video.download('/Downloads')
            print("File has been downloaded\nEnjoy :D\n")
        elif download == 2:
            print("Program has been terminated")
    elif not video:
        print("Sorry this format is unavailable")

time.sleep(5)
