
# TODO
# Need to add GUI

# Date: 8/3/2022
# A program to download videos from YouTube as either a video format or an audio one
# Allows you to choose the quality if you're downloading it as a video while also telling you the size of the download

# Date: 26/4/2023
# Optimized it and removed repeated code... also broke it (Ver. 12)

# Date: 13/5/2023
# Code no longer broken (had to update the module Ver. 15), also added QoL improvements

import time, os
from pytube import YouTube
from pytube.cli import on_progress


def getData(url):
    link = YouTube(url, on_progress_callback=on_progress)
    return link

# print(f'Title: {link.title}\nLength: {round(link.length/60)} mins\nMade by: {link.author}')

# type = int(input("\nDo you want to download this as Audio or Video:\n 1- Audio\n 2- Video\n"))
# media = link.streams.filter(progressive=True, res="144p").first()


# if type == 1:
#     media = link.streams.filter(mime_type="audio/mp4", abr="128kbps", type="audio").first()

# elif type == 2:
#     quality = int(input("\nChoose your preferred quality:\n 1- 144p\n 2- 360p\n 3- 720p\n"))
    
#     if quality == 1:
#         media = link.streams.filter(progressive=True, res="144p").first()

#     elif quality == 2:
#         media = link.streams.filter(progressive=True, res="360p").first()

#     elif quality == 3:
#         media = link.streams.filter(progressive=True, res="720p").first()

# if media:
#     os.system('cls')
#     print(f'File size is: {round(media.filesize / 10 ** 6)} MBs')
#     download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

#     if download == 1:
#         os.system('cls')
#         print("Please wait, file is being downloaded...\n")
#         media.download('D:\\Downloads')
#         print("\n\nFile has been downloaded\nEnjoy :D\n")

#     elif download == 2:
#         print("Program has been terminated")

# elif not media:
#     print("Sorry this format is unavailable")

# time.sleep(5)
