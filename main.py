from youtube import YoutubeDownload

url = input("Give me the video's URL: ")

loop = True
while loop == True:
    option = int(input("""
    What would you download?
    1. Video
    2. Audio

    Type: """))

    if option == 1:
        pass
    elif option == 2:
        audio = YoutubeDownload(url)
        audio.download_audio()
        print("Download complete!")
        loop = False
