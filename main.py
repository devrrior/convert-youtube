from youtube import YoutubeDownload

def main():
    url = input("Give me the video's URL: ")

    loop = True
    while loop == True:
        option = int(input("""
        What would you download?
        1. Video
        2. Audio
        3. Change URL
        4. Exit

        Type: """))

        if option == 1:
            video = YoutubeDownload(url)
            video.download_video()
            print("\nDownload complete!")
        elif option == 2:
            audio = YoutubeDownload(url)
            audio.download_audio()
            print("\nDownload complete!")
            loop = False
        elif option == 3:
            url = input("Give me the video's URL: ")
        elif option == 4:
            loop = False
        else:
            print("Type one option")

if __name__ == "__main__":
    main()
