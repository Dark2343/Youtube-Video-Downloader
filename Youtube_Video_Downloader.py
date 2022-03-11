from pytube import YouTube
from pytube.cli import on_progress

url = str(input("Enter the URL of the video you wish to download:\n"))
video = YouTube(url, on_progress_callback=on_progress)
print(f'\nTitle: {video.title}')
print(f'Length: {round(video.length/60)} mins')
print(f'Made by: {video.author}')
type = int(input("\nDo you want to download Video or Audio:\n 1- Video\n 2- Audio\n"))

if type == 1:
    quality = int(input("\nChoose your preferred quality:\n 1- 360p\n 2- 720p\n"))
    if quality == 1:
        video = video.streams.filter(progressive=True, res="360p").first()
        if video:
            print(f'\nFile size is: {video.filesize / 10 ** 6} MBs')
            download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

            if download == 1:
                video.download('/Downloads')
                print("File has been downloaded\n Enjoy :D\n")
            elif download == 2:
                pass
        elif not video:
            print("Sorry this quality is unavailable")

    elif quality == 2:
        video = video.streams.filter(progressive=True, res="720p").first()
        if video:
            print(f'\nFile size is: {round(video.filesize / 10 ** 6)} MBs')
            download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

            if download == 1:
                video.download('/Downloads')
                print("File has been downloaded\n Enjoy :D\n")
            elif download == 2:
                pass
        elif not video:
            print("Sorry this quality is unavailable")

elif type == 2:
    video = video.streams.filter(mime_type="audio/mp4", abr="128kbps", type="audio").first()
    if video:
        print(f'\nFile size is: {video.filesize / 10 ** 6} MBs')
        download = int(input("Do you wish to download this file ?\n 1-Yes\n 2-No\n"))

        if download == 1:
            video.download('/Downloads')
            print("File has been downloaded\n Enjoy :D\n")
        elif download == 2:
            pass
    elif not video:
        print("Sorry this format is unavailable")
