from functions import choose_option, delete_cache, download_video_audio, merge_video_and_audio
from pytube import YouTube

class YoutubeDownload:

    def __init__(self,url):
        self.__url = url

    # Functions

    def download_audio(self):
        url = YouTube(self.__url)
        audio = url.streams.filter(only_audio=True,file_extension="mp4")
        audio[0].download("/Users/fernando/Downloads")

    def download_video(self):
        url = YouTube(self.__url)
        option = choose_option(url)
        download_video_audio(url,option)
        merge_video_and_audio(url)
        delete_cache(url)
        print("Paso la prueba")

    def get_url(self):
        return self.__url

    def set_url(self,new_url):
        self.__url = new_url
